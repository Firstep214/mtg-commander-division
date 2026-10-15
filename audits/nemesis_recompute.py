import gzip,json,collections,re
best={};ora={}
for l in gzip.open('/workspace/mtg/sources/2026-10-14/default-cards-20261014090548.jsonl.gz','rt'):
    l=l.strip().rstrip(',')
    if not l.startswith('{'): continue
    c=json.loads(l)
    n=c['name']
    if c.get('layout')in('art_series','token','double_faced_token','emblem'): continue
    ora.setdefault(n,c)
    p=c.get('prices',{}).get('usd')
    if p and 'paper' in c.get('games',[]) and not c.get('digital'):
        p=float(p)
        if n not in best or p<best[n][0]: best[n]=(p,c['set'].upper()+' '+c['collector_number'])
alias={}
for n in list(ora):
    if ' // ' in n: alias[n.split(' // ')[0]]=n
gc=set(json.load(open('/dev/stdin')) if False else [])
out={}
for d,cmdr_ci in [('A_tokens',None),('B_control',None),('C_aristocrats',None),('D_spellslinger',None)]:
    lines=[l.split(' ',1) for l in open(f'/workspace/mtg/decks/{d}.txt').read().split('\n') if l.strip()]
    deck=[(int(q),n.strip()) for q,n in lines]
    led={}
    for l in open(f'/workspace/mtg/decks/PRICE_LEDGER_{d}.md'):
        m=re.match(r'\| (\d+) \| (.+?) \| ([\d.]+) \| (.+?) \| ([\d.]+) \|',l)
        if m: led[m[2]]=(int(m[1]),float(m[3]),m[4])
    cmd=ora[deck[0][1]]; ci=set(cmd['color_identity'])
    tot=0;cnt=0;probs=[]
    for q,n in deck:
        nn=n if n in ora else alias.get(n,n)
        c=ora.get(nn); cnt+=q
        if not c: probs.append('MISSING '+n);continue
        if not set(c['color_identity'])<=ci: probs.append('CI '+n)
        if c['legalities']['commander']!='legal': probs.append('ILLEGAL '+n)
        if c.get('game_changer'): probs.append('GC '+n)
        if q>1 and 'Basic Land' not in c['type_line']: probs.append('SINGLETON '+n)
        b=best.get(nn)
        if not b: probs.append('UNPRICED '+n);continue
        tot+=q*b[0]
        L=led.get(n)
        if not L: probs.append('NOT IN LEDGER '+n)
        elif abs(L[1]-b[0])>0.001 or L[0]!=q: probs.append(f'MISMATCH {n} ledger {L} mine {b}')
    extra=set(led)-{n for q,n in deck}
    print(d,'count',cnt,'ledger rows',len(led),'total %.2f'%tot,'margin %.2f'%(100-tot),probs,'extra in ledger',extra)
