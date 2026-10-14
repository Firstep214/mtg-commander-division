import json,sys,collections
db=json.load(open('data/carddb.json'));al=db.pop('_alias')
BASIC={'Plains','Island','Swamp','Mountain','Forest','Wastes'}
def look(n): return db.get(n) or db.get(al.get(n,''))
def load(f):
    out=[]
    for l in open(f):
        l=l.strip()
        if not l: continue
        q,n=l.split(' ',1); out.append((int(q),n))
    return out
f=sys.argv[1]; deck=load(f); cmdr=deck[0][1]; C=look(cmdr)
tot=sum(q for q,_ in deck); prob=[]; price=0
if tot!=100: prob.append(f'count {tot}')
cnt=collections.Counter()
for q,n in deck:
    d=look(n)
    if not d: prob.append('MISSING '+n); continue
    cnt[d['name']]+=q
    if q>1 and n not in BASIC: prob.append('dup '+n)
    if not set(d['ci'])<=set(C['ci']): prob.append(f'CI {n} {d["ci"]}')
    if d['cmd']!='legal': prob.append(f'illegal {n} {d["cmd"]}')
    if d['gc']: prob.append('GC '+n)
    if d['usd'] is None: prob.append('noprice '+n)
    else: price+=q*d['usd']
    if d['usd'] and d['usd']>5: print('  pricey',n,d['usd'])
if 'Legendary' not in C['type'] or not ('Creature' in C['type'] or 'can be your commander' in C['text']): prob.append('commander not legendary creature')
print(f, 'total', round(price,2), 'cards',tot, 'PROBLEMS:',prob)
