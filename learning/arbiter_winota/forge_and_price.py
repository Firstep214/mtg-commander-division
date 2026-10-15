import zipfile,re,json,gzip
Z=zipfile.ZipFile('/workspace/mtg/forge/app/res/cardsfolder/cardsfolder.zip')
idx={}
for n in Z.namelist():
  if n.endswith('.txt'):
    t=Z.read(n).decode('utf-8','ignore'); m=re.search(r'^Name:(.*)$',t,re.M)
    if m: idx.setdefault(m.group(1).strip().lower(),(n,t))
D='/workspace/mtg/sources/2026-10-14/'; k=lambda n:n.split(' // ')[0].lower(); led={};st={}
for l in gzip.open(D+'default-cards-20261014090548.jsonl.gz','rt'):
  c=json.loads(l)
  if c.get('layout') in('art_series','token','double_faced_token','emblem') or c.get('digital') or 'paper' not in c.get('games',[]) or c['prices'].get('usd') is None:continue
  n=k(c['name']);p=float(c['prices']['usd']);led[n]=min(led.get(n,9e9),p)
  if not(c['set']=='plst' or c['set_type'] in('memorabilia','promo') or c.get('border_color')=='gold' or c.get('promo')): st[n]=min(st.get(n,9e9),p)
L=[(i,int(x.split(' ',1)[0]),x.split(' ',1)[1].strip()) for i,x in enumerate(open('decks/E_clean.txt'),1) if x.strip()]
res={'flags':[],'missing':[],'unpriced':[],'prices':{}}
for i,q,n in L:
  f=idx.get(k(n))
  if not f: res['missing'].append((i,n))
  else:
    for line in f[1].splitlines():
      if 'RemoveDeck' in line: res['flags'].append((i,n,f[0],line.strip()))
  if k(n) not in st: res['unpriced'].append((i,n))
  res['prices'][n]=(led.get(k(n)),st.get(k(n)))
res['ledger']=round(sum(q*(led.get(k(n)) or 0) for i,q,n in L),2); res['strict']=round(sum(q*(st.get(k(n)) or 0) for i,q,n in L),2)
top=sorted(((st.get(k(n),0)*q,n) for i,q,n in L),reverse=True)[:12]
json.dump(res,open('forge_price.json','w'),indent=1)
print(res['flags'],res['missing'],res['unpriced'],res['ledger'],res['strict'],top,sep='\n')
