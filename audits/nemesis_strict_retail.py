import gzip,json
decks={d:[(int(l.split(' ',1)[0]),l.split(' ',1)[1].strip()) for l in open(f'/workspace/mtg/decks/{d}.txt') if l.strip()] for d in ['A_tokens','B_control','C_aristocrats','D_spellslinger']}
names={n.split(' // ')[0] for v in decks.values() for q,n in v}
pr={};st={};ora={}
for l in gzip.open('/workspace/mtg/sources/2026-10-14/default-cards-20261014090548.jsonl.gz','rt'):
    l=l.strip().rstrip(',')
    if not l.startswith('{'):continue
    c=json.loads(l);n=c['name'].split(' // ')[0]
    if n not in names or c.get('layout') in('art_series','token'):continue
    ora.setdefault(n,c)
    p=c['prices'].get('usd')
    if p and 'paper' in c['games'] and not c.get('digital'):
        pr.setdefault(n,[]).append((float(p),c['set'].upper(),c['collector_number'],c['set_type'],c.get('border_color'),c.get('promo')))
for d,v in decks.items():
    strict=0;notes=[]
    for q,n in v:
        n=n.split(" // ")[0];L=sorted(pr[n]);b=L[0]
        ok=[x for x in L if x[1]!='PLST' and x[3] not in('memorabilia','promo') and x[4]!='gold' and not x[5]]
        s=ok[0] if ok else b
        if s!=b: notes.append(f'{n}: {b[0]} {b[1]} {b[2]} ({b[3]}) -> {s[0]} {s[1]} {s[2]} (+{s[0]-b[0]:.2f})')
        strict+=q*s[0]
    print(d,'strict-retail total %.2f'%strict);print('\n'.join(notes))
json.dump({n:{'ci':c['color_identity'],'cmc':c.get('cmc'),'type':c['type_line'],'text':c.get('oracle_text') or ' // '.join(f.get('oracle_text','') for f in c.get('card_faces',[]))} for n,c in ora.items()},open('/tmp/ora.json','w'))
