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
R={'cands':{c:(led[k(c)],strict[k(c)]) for c in ["Coldsteel Heart","Prismatic Lens","Star Compass","Worn Powerstone","Everflowing Chalice"]}}
SW={'B':('B_control',[('Ghostly Flicker','Skyclave Apparition'),('Deputy of Detention','Aetherize'),('Hallowed Burial','Comeuppance')],'Azorius Signet'),
'C':('C_aristocrats',[('Undying Evil','Toxic Deluge'),('Viscera Seer','Massacre Girl'),('Path to Exile','Go for the Throat')],'Orzhov Signet'),
'D':('D_spellslinger',[('Faithless Looting','Mulldrifter'),('Blasphemous Act','Aetherize')],'Izzet Signet')}
PICK=os.environ.get('PICK','Worn Powerstone')
def ap(L,o,i):
  ix=[j for j,l in enumerate(L) if l.strip()=='1 '+o]; assert len(ix)==1,o; assert not any(l.strip()=='1 '+i for l in L),i; L[ix[0]]='1 '+i
tot=lambda L,t:round(sum(int(l.split(' ',1)[0])*t[k(l.split(' ',1)[1].strip())][0] for l in L if l.strip()),2)
cnt=lambda L:sum(int(l.split(' ',1)[0]) for l in L if l.strip())
for d,(b,sw,sig) in SW.items():
  L=open(DK+b+'_V1.1.txt').read().split('\n'); pre=(tot(L,led),tot(L,strict))
  for o,i in sw: ap(L,o,i)
  v12=list(L); v12tot=(tot(L,led),tot(L,strict)); assert cnt(L)==100
  R[d]={'in_deck':{c:any(l.strip()=='1 '+c for l in L) for c in R['cands']}}
  ap(L,sig,PICK); assert cnt(L)==100
  R[d].update(v11=pre,v12=v12tot,v13p=(tot(L,led),tot(L,strict)),sig=sig)
  if os.environ.get('WRITE'):
    for fn,body in [(b+'_V1.2.txt',v12),(b+'_V1.3_PENDING.txt',L)]:
      assert not os.path.exists(DK+fn); open(DK+fn,'w').write('\n'.join(body))
print(json.dumps(R,indent=0))
