import gzip,json
db={}
for l in gzip.open('data/oracle.jsonl.gz','rt'):
    c=json.loads(l)
    if c.get('layout') in ('token','art_series','emblem','double_faced_token'): continue
    n=c['name']; db[n]={'name':n,'ci':c.get('color_identity',[]),'cmd':c['legalities'].get('commander'),'gc':c.get('game_changer',False),'type':c.get('type_line',''),'cmc':c.get('cmc',0),'text':c.get('oracle_text') or ' // '.join(f.get('oracle_text','') for f in c.get('card_faces',[])),'usd':None,'set':None}
    if '//' in n: db.setdefault('_alias',{})[n.split(' // ')[0]]=n
for l in gzip.open('data/default.jsonl.gz','rt'):
    c=json.loads(l)
    if c.get('digital') or 'paper' not in c.get('games',[]): continue
    p=c['prices'].get('usd')
    if not p: continue
    d=db.get(c['name'])
    if d and (d['usd'] is None or float(p)<d['usd']): d['usd']=float(p); d['set']=c['set'].upper()+' '+c['collector_number']
json.dump(db,open('data/carddb.json','w'))
print(len(db), sum(1 for k,v in db.items() if k!='_alias' and v['gc']))
