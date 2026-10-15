import json,gzip,re
D='/workspace/mtg/sources/2026-10-14/'
BASE={'B':'B_control_V1.1','C':'C_aristocrats_V1.1','D':'D_spellslinger_V1.1'}
SW={'B':[('Ghostly Flicker','Skyclave Apparition'),('Deputy of Detention','Aetherize'),('Hallowed Burial','Comeuppance'),('Azorius Signet','Talisman of Progress')],
'C':[('Undying Evil','Toxic Deluge'),('Viscera Seer','Massacre Girl'),('Path to Exile','Go for the Throat'),('Orzhov Signet','Talisman of Hierarchy')],
'D':[('Faithless Looting','Mulldrifter'),('Blasphemous Act','Aetherize'),('Izzet Signet','Talisman of Creativity')]}
FALLBACK=['Mind Stone','Fellwar Stone']
gcj=json.load(open(D+'game_changers.json')); gc={n.lower() for n in gcj['all_cards']}
ban={b['name'].lower() for b in json.load(open(D+'banlist.json'))['banned']}
k=lambda n:n.split(' // ')[0].lower()
led={};strict={};info={}
for l in gzip.open(D+'default-cards-20261014090548.jsonl.gz','rt'):
  c=json.loads(l)
  if c.get('layout') in('art_series','token','double_faced_token','emblem'):continue
  n=k(c['name'])
  i=info.setdefault(n,dict(ci=c['color_identity'],leg=c['legalities']['commander'],gc=False,text=c.get('oracle_text') or ' / '.join(f.get('oracle_text','') for f in c.get('card_faces',[]))))
  i['gc']=i['gc'] or bool(c.get('game_changer'))
  if c['legalities']['commander']=='legal': i['leg']='legal'
  if c.get('digital') or 'paper' not in c.get('games',[]) or c['prices'].get('usd') is None:continue
  p=float(c['prices']['usd']); t=(p,c['set'].upper(),c['collector_number'])
  if n not in led or p<led[n][0]: led[n]=t
  if not(c['set']=='plst' or c['set_type'] in('memorabilia','promo') or c.get('border_color')=='gold' or c.get('promo')):
    if n not in strict or p<strict[n][0]: strict[n]=t
def tot(tbl,dk): return round(sum(q*tbl[k(n)][0] for q,n in dk),2)
out={'gc_json_retrieved':gcj['retrieved_utc'],'toxic':{'in_json':'toxic deluge' in gc,'scryfall_flag':info['toxic deluge']['gc']}}
for d,f in BASE.items():
  deck=[(int(l.split(' ',1)[0]),l.split(' ',1)[1].strip()) for l in open(f'/workspace/mtg/decks/{f}.txt') if l.strip()]
  names=[n for q,n in deck]; cid=set(info[k(names[0])]['ci']); new=list(deck); rows=[]
  for o,i in SW[d]:
    ii=info[k(i)]; cur=[n for q,n in new]
    r=dict(out=o,inn=i,out_present=o in cur,out_line=cur.index(o)+1 if o in cur else None,in_absent=i not in cur,in_line=cur.index(i)+1 if i in cur else None,
      legal=ii['leg'],ci=''.join(ii['ci']),ci_ok=set(ii['ci'])<=cid,ban=k(i) in ban,gc=(k(i) in gc,ii['gc']),
      led=(led[k(o)],led[k(i)]),strict=(strict[k(o)],strict[k(i)]),extra=bool(re.search('extra turn',ii['text'],re.I)),text=ii['text'][:220])
    if 'Signet' in o: r['fallbacks']={fb:(fb in cur, cur.index(fb)+1 if fb in cur else None) for fb in FALLBACK}
    ok=r['out_present'] and r['in_absent'] and r['legal']=='legal' and r['ci_ok'] and not r['ban'] and not any(r['gc'])
    r['apply']=ok
    if ok: new=[(q,i if n==o else n) for q,n in new]
    rows.append(r)
  out[d]=dict(base=f,cid=''.join(sorted(cid)),count=sum(q for q,n in new),pre=(tot(led,deck),tot(strict,deck)),post=(tot(led,new),tot(strict,new)),swaps=rows)
json.dump(out,open('/workspace/mtg/learning/arbiter_learn02/results.json','w'),indent=1)
print(json.dumps(out,indent=0)[:6000])
