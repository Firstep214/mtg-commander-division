import sys,json,re
sys.path.insert(0,'/workspace/mtg/audits/arbiter_scripts')
import audit as A
A.R='/workspace/mtg'
import gzip
D='/workspace/mtg/sources/2026-10-14/'
k=lambda n:n.split(' // ')[0].lower(); led={};st={}
for l in gzip.open(D+'default-cards-20261014090548.jsonl.gz','rt'):
  c=json.loads(l)
  if c.get('layout') in('art_series','token','double_faced_token','emblem') or c.get('digital') or 'paper' not in c.get('games',[]) or c['prices'].get('usd') is None:continue
  n=k(c['name']);p=float(c['prices']['usd'])
  led[n]=min(led.get(n,9e9),p)
  if not(c['set']=='plst' or c['set_type'] in('memorabilia','promo') or c.get('border_color')=='gold' or c.get('promo')): st[n]=min(st.get(n,9e9),p)
out={}
for d in ['B_control','C_aristocrats','D_spellslinger']:
  f=f'{d}_V1.3_PENDING'; r,h,c=A.audit(f)
  dk=[(int(l.split(' ',1)[0]),l.split(' ',1)[1].strip()) for l in open(f'decks/{f}.txt') if l.strip()]
  out[d]=dict(sha=h,checks={x:y for x,y in r.items()},ledger=round(sum(q*led[k(n)] for q,n in dk),2),strict=round(sum(q*st[k(n)] for q,n in dk),2))
  print(d,{x:y[0] for x,y in r.items()},out[d]['ledger'],out[d]['strict'],r['combos'][1],r['mld'][1],r['extra_turns'][1])
json.dump(out,open('learning/arbiter_learn02/v13_results.json','w'),indent=1,default=str)
