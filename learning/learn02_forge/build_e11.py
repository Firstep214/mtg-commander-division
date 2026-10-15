import json,gzip,re,os
D='/workspace/mtg/sources/2026-10-14/';DK='/workspace/mtg/decks/'
k=lambda n:n.split(' // ')[0].lower()
led={};strict={}
for l in gzip.open(D+'default-cards-20261014090548.jsonl.gz','rt'):
  c=json.loads(l)
  if c.get('layout') in('art_series','token','double_faced_token','emblem'):continue
  if c.get('digital') or 'paper' not in c.get('games',[]) or c['prices'].get('usd') is None:continue
  n=k(c['name']);p=float(c['prices']['usd']);t=(p,c['set'].upper(),c['collector_number'])
  if n not in led or p<led[n][0]: led[n]=t
  if not(c['set']=='plst' or c['set_type'] in('memorabilia','promo') or c.get('border_color')=='gold' or c.get('promo')):
    if n not in strict or p<strict[n][0]: strict[n]=t
def ap(L,o,i):
  ix=[j for j,l in enumerate(L) if l.strip()=='1 '+o]; assert len(ix)==1,o; assert not any(l.strip()=='1 '+i for l in L),i; L[ix[0]]='1 '+i
tot=lambda L,t:round(sum(int(l.split(' ',1)[0])*t[k(l.split(' ',1)[1].strip())][0] for l in L if l.strip()),2)
cnt=lambda L:sum(int(l.split(' ',1)[0]) for l in L if l.strip())
L=open(DK+'E_winota_V1.0_SUBMITTED.txt').read().split('\n')
assert L[0].strip()=='1 Winota, Joiner of Forces (Commander)'; L[0]='1 Winota, Joiner of Forces'
pre=(tot(L,led),tot(L,strict))
for o,i in [('Boros Signet','Worn Powerstone'),('Odric, Master Tactician','Beetleback Chief')]: ap(L,o,i)
assert cnt(L)==100
rows=[(l.split(' ',1)[1].strip(),int(l.split(' ',1)[0])) for l in L if l.strip()]
print(json.dumps(dict(pre=pre,post=(tot(L,led),tot(L,strict)))))
if os.environ.get('WRITE'):
  assert not os.path.exists(DK+'E_winota_V1.1.txt'); open(DK+'E_winota_V1.1.txt','w').write('\n'.join(L))
  out=["# PRICE_LEDGER_E_winota (E_winota_V1.1, 2026-10-15, CH001-LEARN-03)","Source: Scryfall default_cards 2026-10-14 17:05 PHT. Ledger = cheapest non-foil paper USD; strict = excluding PLST/promo/memorabilia/gold-border. Script: learning/learn02_forge/build_e11.py","","| Qty | Card | Ledger $ | Ledger printing | Strict $ | Strict printing | Line strict $ |","|---|---|---|---|---|---|---|"]
  for n,q in rows:
    a=led[k(n)];b=strict[k(n)]; out.append(f"| {q} | {n} | {a[0]:.2f} | {a[1]} #{a[2]} | {b[0]:.2f} | {b[1]} #{b[2]} | {q*b[0]:.2f} |")
  out+=["",f"**Total: ledger ${tot(L,led):.2f} / strict ${tot(L,strict):.2f}** (V1.0 submitted: ${pre[0]:.2f} / ${pre[1]:.2f}). Under the $100 target; no over-budget reason needed."]
  open(DK+'PRICE_LEDGER_E_winota.md','w').write('\n'.join(out)+'\n')
