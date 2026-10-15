import sys,json,gzip,shutil
sys.path.insert(0,'/workspace/mtg/audits/arbiter_scripts'); import audit as A
W='/workspace/mtg/learning/arbiter_learn03'; D='/workspace/mtg/sources/2026-10-14/'
SW={'B_control':[('Comeuppance','Inspiring Overseer'),('Supreme Verdict','Elite Spellbinder')],'C_aristocrats':[("Toxic Deluge","Kaya's Wrath")],
'D_spellslinger':[('Coruscation Mage','Fiery Inscription'),('Fiery Cannonade','Propaganda'),('Essence Scatter','Harmonic Prodigy'),('Consider','Fiery Confluence')]}
gc={n.lower() for n in json.load(open(D+'game_changers.json'))['all_cards']}
k=lambda n:n.split(' // ')[0].lower(); led={};st={};flag={}
for l in gzip.open(D+'default-cards-20261014090548.jsonl.gz','rt'):
  c=json.loads(l); n=k(c['name'].split(' // ')[0]); flag[n]=flag.get(n,False) or bool(c.get('game_changer'))
  if c.get('layout') in('art_series','token','double_faced_token','emblem') or c.get('digital') or 'paper' not in c.get('games',[]) or c['prices'].get('usd') is None:continue
  p=float(c['prices']['usd']); led[n]=min(led.get(n,9e9),p)
  if not(c['set']=='plst' or c['set_type'] in('memorabilia','promo') or c.get('border_color')=='gold' or c.get('promo')): st[n]=min(st.get(n,9e9),p)
A.R=W; out={}
for d,sw in SW.items():
  L=open(f'/workspace/mtg/decks/{d}_V1.3.txt').read().splitlines(); names=[x.split(' ',1)[1] for x in L if x.strip()]
  pre=(round(sum(int(x.split(' ',1)[0])*led[k(x.split(' ',1)[1])] for x in L if x.strip()),2),round(sum(int(x.split(' ',1)[0])*st[k(x.split(' ',1)[1])] for x in L if x.strip()),2))
  rows=[]
  for o,i in sw:
    rows.append(dict(out=o,out_line=names.index(o)+1 if o in names else None,in_present=i in names,gc=(k(i) in gc,flag.get(k(i))),led=(led[k(o)],led[k(i)]),st=(st[k(o)],st[k(i)])))
    L=[f'1 {i}' if x==f'1 {o}' else x for x in L]
  open(f'{W}/decks/{d}_LEARN03.txt','w').write('\n'.join(L)+'\n')
  r,h,c=A.audit(f'{d}_LEARN03')
  post=(round(sum(int(x.split(' ',1)[0])*led[k(x.split(' ',1)[1])] for x in L if x.strip()),2),round(sum(int(x.split(' ',1)[0])*st[k(x.split(' ',1)[1])] for x in L if x.strip()),2))
  out[d]=dict(pre=pre,post=post,swaps=rows,checks={a:b for a,b in r.items()})
  print(d,pre,post,{a:b[0] for a,b in r.items()},r['combos'][1][0],r['mld'][1]);[print('  ',x) for x in rows]
json.dump(out,open(W+'/results.json','w'),indent=1,default=str)
