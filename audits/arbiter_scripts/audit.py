#!/usr/bin/env python3
"""Arbiter independent audit, CH001-AUD-ARB. Read-only on decks."""
import json, gzip, re, sys, os, hashlib
R='/workspace/mtg'; S=R+'/sources/2026-10-14'
DECKS=['A_tokens','B_control','C_aristocrats','D_spellslinger']
ban=json.load(open(S+'/banlist.json')); gc=json.load(open(S+'/game_changers.json'))
BANNED={b['name'].lower() for b in ban['banned']}
GC={n.lower() for n in gc['all_cards']}
for c in gc['by_color'].values(): GC|={n.lower() for n in c['cards']}
GC.add("tergrid, god of fright // tergrid's lantern")
cards={}
for l in gzip.open(R+'/data/oracle.jsonl.gz','rt'):
    c=json.loads(l)
    if c.get('layout') in ('token','double_faced_token','emblem','art_series','vanguard','scheme','planar'): continue
    cards.setdefault(c['name'].lower(),c)
    if ' // ' in c['name']:
        for f in c['name'].split(' // '): cards.setdefault(f.lower(),c)
def otext(c):
    t=c.get('oracle_text','') or ''
    for f in c.get('card_faces',[]) or []: t+='\n'+(f.get('oracle_text') or '')
    return t
def tline(c):
    t=c.get('type_line','')
    return t
# curated 2-card infinite pairs (unordered), checked by name; plus heuristics below
COMBOS=[("Mystic Sanctuary","Ghostly Flicker"),("Ashnod's Altar","Nim Deathmantle"),("Niv-Mizzet, Parun","Curiosity"),
("Niv-Mizzet, Parun","Ophidian Eye"),("Niv-Mizzet, Parun","Tandem Lookout"),("Felidar Guardian","Saheeli Rai"),("Restoration Angel","Kiki-Jiki, Mirror Breaker"),
("Deceiver Exarch","Kiki-Jiki, Mirror Breaker"),("Pestermite","Kiki-Jiki, Mirror Breaker"),("Zealous Conscripts","Kiki-Jiki, Mirror Breaker"),
("Dramatic Reversal","Isochron Scepter"),("Mikaeus, the Unhallowed","Triskelion"),("Walking Ballista","Mikaeus, the Unhallowed"),
("Exquisite Blood","Sanguine Bond"),("Vito, Thorn of the Dusk Rose","Exquisite Blood"),("Heliod, Sun-Crowned","Walking Ballista"),
("Thassa's Oracle","Demonic Consultation"),("Thassa's Oracle","Tainted Pact"),("Underworld Breach","Lion's Eye Diamond"),("Dualcaster Mage","Twinflame"),
("Dualcaster Mage","Heat Shimmer"),("Splinter Twin","Pestermite"),("Splinter Twin","Deceiver Exarch"),("Peregrine Drake","Ghostly Flicker"),
("Basalt Monolith","Rings of Brighthearth"),("Basalt Monolith","Forsaken Monument"),("Grim Monolith","Power Artifact"),("Basalt Monolith","Power Artifact"),
("Worldgorger Dragon","Animate Dead"),("Bloom Tender","Freed from the Real"),("Devoted Druid","Vizier of Remedies"),("Food Chain","Eternal Scourge"),
("Teysa Karlov","Ashnod's Altar"),("Karmic Guide","Reveillark"),("Sun Titan","Fiend Hunter"),("Archangel of Thune","Spike Feeder"),
("Elas il-Kor, Sadistic Pilgrim","Exquisite Blood"),("Bastion of Remembrance","Exquisite Blood"),("Zulaport Cutthroat","Exquisite Blood"),
("Witherbloom Apprentice","Chain of Smog"),("Brago, King Eternal","Strionic Resonator"),("Ghostly Flicker","Archaeomancer"),("Ghostly Flicker","Mnemonic Wall"),
("Mirror Entity","Intruder Alarm"),("Felidar Retreat","Scute Swarm"),("Cathars' Crusade","Intruder Alarm"),("Divine Visitation","Intruder Alarm"),
("Agent of Treachery","Deadeye Navigator"),("Restoration Angel","Deadeye Navigator"),("Pitiless Plunderer","Ashnod's Altar"),("Yahenni, Undying Partisan","Ashnod's Altar"),
("Sifter of Skulls","Ashnod's Altar"),("Kaya's Ghostform","Ashnod's Altar"),("Mizzix's Mastery","Past in Flames"),("Storm-Kiln Artist","Haughty Djinn")]
COMBO_NOTE={("Teysa Karlov","Ashnod's Altar"),("Pitiless Plunderer","Ashnod's Altar"),("Yahenni, Undying Partisan","Ashnod's Altar"),("Sifter of Skulls","Ashnod's Altar"),("Kaya's Ghostform","Ashnod's Altar"),("Mizzix's Mastery","Past in Flames"),("Storm-Kiln Artist","Haughty Djinn"),("Sun Titan","Fiend Hunter")}  # decoy pairs: verified NOT infinite on their own
EXTRA=re.compile(r'extra turn',re.I)
MLD=re.compile(r'(destroy|exile|return|sacrifice)[^.]{0,40}\ball (nonbasic )?lands\b|each player sacrifices[^.]{0,30}lands?|lands? (don\'t|do not) untap|destroy all permanents|exile all permanents',re.I)
ANY=re.compile(r'a deck can have any number of cards named',re.I)
def audit(d):
    p=f'{R}/decks/{d}.txt'; raw=open(p,encoding='utf-8').read().splitlines()
    ents=[]; out={}; bad_parse=[]
    for i,l in enumerate(raw,1):
        if not l.strip() or l.strip().startswith('#'): continue
        m=re.match(r'^\s*(\d+)x?\s+(.+?)\s*$',l)
        if not m: bad_parse.append((i,l)); continue
        ents.append((i,l,int(m[1]),m[2]))
    total=sum(e[2] for e in ents)
    res={}
    unres=[(i,l) for i,l,n,nm in ents if nm.lower() not in cards]
    res['names']=(not unres and not bad_parse, unres+bad_parse)
    res['count']=(total==100, total)
    # singleton
    seen={}; sing=[]
    for i,l,n,nm in ents:
        c=cards.get(nm.lower())
        basic=c and 'Basic' in tline(c) and 'Land' in tline(c)
        anyn=c and ANY.search(otext(c))
        key=(c['name'] if c else nm).lower()
        if not(basic or anyn):
            if n>1: sing.append((i,l,'quantity >1'))
            if key in seen: sing.append((i,l,f'duplicate of line {seen[key]}'))
        seen.setdefault(key,i)
    res['singleton']=(not sing,sing)
    # commander = line 1 (deck convention); check partner
    ci,cl,cn,cname=ents[0]; cc=cards.get(cname.lower())
    t=tline(cc) if cc else ''; ot=otext(cc) if cc else ''
    elig=('Legendary' in t and ('Creature' in t or 'Vehicle' in t or ('Spacecraft' in t and cc.get('power')))) or 'can be your commander' in ot
    partner=bool(re.search(r'\bPartner\b|Choose a Background|Doctor\'s companion',ot))
    res['commander']=(elig and cn==1 and cc and cc['legalities'].get('commander') in ('legal',),
                      dict(line=ci,text=cl,type=t,partner=partner,legality=cc['legalities'].get('commander') if cc else None))
    cid=set(cc.get('color_identity',[])) if cc else set()
    ciout=[]
    for i,l,n,nm in ents[1:]:
        c=cards.get(nm.lower())
        if c and not set(c.get('color_identity',[]))<=cid: ciout.append((i,l,''.join(c['color_identity'])))
    res['color_identity']=(not ciout, (''.join(sorted(cid)) or 'C', ciout))
    bans=[]
    for i,l,n,nm in ents:
        c=cards.get(nm.lower()); 
        if nm.lower() in BANNED or (c and c['name'].lower() in BANNED): bans.append((i,l,'banlist.json'))
        elif c and c['legalities'].get('commander')!='legal': bans.append((i,l,'Scryfall commander='+c['legalities'].get('commander')))
        # category bans (ante, conspiracy, dexterity, offensive)
        elif c and (re.search(r'\bante\b',otext(c),re.I) or 'Conspiracy' in tline(c)): bans.append((i,l,'category ban'))
    res['bans']=(not bans,bans)
    gcs=[(i,l,'banlist GC list' if nm.lower() in GC else 'Scryfall game_changer flag') for i,l,n,nm in ents
         if nm.lower() in GC or (cards.get(nm.lower()) or {}).get('game_changer')]
    res['game_changers']=(not gcs,gcs)
    names={(cards.get(nm.lower()) or {'name':nm})['name']:(i,l) for i,l,n,nm in ents}
    combos=[];decoys=[]
    for a,b in COMBOS:
        if a in names and b in names:
            (decoys if (a,b) in COMBO_NOTE else combos).append((names[a],names[b],a+' + '+b))
    res['combos']=(not combos,(combos,decoys))
    et=[(i,l) for i,l,n,nm in ents if cards.get(nm.lower()) and EXTRA.search(otext(cards[nm.lower()]))]
    ml=[(i,l) for i,l,n,nm in ents if cards.get(nm.lower()) and MLD.search(otext(cards[nm.lower()]))]
    res['extra_turns']=(not et,et); res['mld']=(not ml,ml)
    return res, hashlib.sha256(open(p,'rb').read()).hexdigest(), cname
if __name__=='__main__':
    allr={}
    for d in DECKS:
        r,h,c=audit(d); allr[d]={'sha256':h,'commander':c,'res':r}
    json.dump(allr,open('/workspace/mtg/audits/arbiter_scripts/results.json','w'),indent=1,default=str)
    for d,v in allr.items():
        print(d,v['commander'],{k:x[0] for k,x in v['res'].items()})
        for k,x in v['res'].items():
            if not x[0] or k in('combos','commander','color_identity'): print('   ',k,x[1])
