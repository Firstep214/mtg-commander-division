# Independent re-check: reads raw Scryfall bulk files directly (does not use carddb.json/check.py)
import gzip,json,sys,re
ORA={};FACE={}
for l in gzip.open('data/oracle.jsonl.gz','rt'):
    c=json.loads(l)
    if c.get('layout') in ('token','art_series','emblem','double_faced_token'):continue
    ORA[c['name']]=c; FACE[c['name'].split(' // ')[0]]=c['name']
PR={}
for l in gzip.open('data/default.jsonl.gz','rt'):
    c=json.loads(l)
    if c.get('digital') or 'paper' not in c.get('games',[]):continue
    u=c['prices'].get('usd')
    if u and (c['name'] not in PR or float(u)<PR[c['name']]):PR[c['name']]=float(u)
BASICS={'Plains','Island','Swamp','Mountain','Forest','Wastes'}
# Known 2-card infinite pairs (non-exhaustive, Bracket 2 screen)
PAIRS=[('Felidar Guardian','Restoration Angel'),('Exquisite Blood','Sanguine Bond'),('Dualcaster Mage','Twinflame'),('Dualcaster Mage','Heat Shimmer'),('Gravecrawler','Phyrexian Altar'),('Niv-Mizzet, Parun','Curiosity'),('Deadeye Navigator','Peregrine Drake'),('Kiki-Jiki, Mirror Breaker','Zealous Conscripts'),('Thassa\'s Oracle','Demonic Consultation'),('Isochron Scepter','Dramatic Reversal'),('Basalt Monolith','Rings of Brighthearth'),('Mikaeus, the Unhallowed','Triskelion'),('Heliod, Sun-Crowned','Walking Ballista'),('Krenko, Mob Boss','Thornbite Staff'),('Reassembling Skeleton','Ashnod\'s Altar'),('Sword of the Meek','Thopter Foundry'),('Peregrine Drake','Ghostly Flicker'),('Archaeomancer','Ghostly Flicker'),('Mnemonic Wall','Ghostly Flicker'),('Brago, King Eternal','Strionic Resonator')]
f=sys.argv[1];L=[(int(a),b) for a,b in (x.strip().split(' ',1) for x in open(f) if x.strip())]
res={};flags=[]
cards=[(q,ORA.get(n) or ORA.get(FACE.get(n,''))) for q,n in L]
res['missing']=[n for (q,n),(_,c) in zip(L,cards) if not c]
cm=cards[0][1];ci=set(cm['color_identity'])
res['count']=sum(q for q,_ in L)
res['commander_ok']=('Legendary' in cm['type_line'] and 'Creature' in cm['type_line'])
names=[c['name'] for q,c in cards if c]
res['nonbasic_dups']=[n for n in set(names) if names.count(n)>1 or any(q>1 and c['name']==n and n not in BASICS for q,c in cards)]
res['ci_viol']=[c['name'] for q,c in cards if c and not set(c['color_identity'])<=ci]
res['not_legal']=[c['name'] for q,c in cards if c and c['legalities']['commander']!='legal']
res['game_changers']=[c['name'] for q,c in cards if c and c.get('game_changer')]
txt=lambda c:(c.get('oracle_text') or ' '.join(x.get('oracle_text','') for x in c.get('card_faces',[]))).lower()
res['extra_turns']=[c['name'] for q,c in cards if c and 'extra turn' in txt(c)]
res['mass_land_denial']=[c['name'] for q,c in cards if c and re.search(r'destroy all lands|each player sacrifices .*lands|lands don.t untap|destroy all nonbasic|return all lands',txt(c))]
res['tutors']=[c['name'] for q,c in cards if c and re.search(r'search your library for an? (?!basic|land|plains|island|swamp|mountain)',txt(c)) and 'Land' not in c['type_line']]
res['infinite_pairs']=[p for p in PAIRS if p[0] in names and p[1] in names]
missingprice=[c['name'] for q,c in cards if c and c['name'] not in PR]
res['no_price']=missingprice
res['total_usd']=round(sum(q*PR.get(c['name'],0) for q,c in cards if c),2)
res['under_100']=res['total_usd']<=100
ok=res['count']==100 and res['commander_ok'] and not any(res[k] for k in ['missing','nonbasic_dups','ci_viol','not_legal','game_changers','extra_turns','mass_land_denial','infinite_pairs','no_price']) and res['under_100']
res['PASS']=ok
print(json.dumps(res,indent=1))
