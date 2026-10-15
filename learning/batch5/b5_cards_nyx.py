import re,glob,collections as C,json
decks={'A12':'A_tokens_V1.2','B13':'B_control_V1.3','C13':'C_aristocrats_V1.3','D13':'D_spellslinger_V1.3'}
lists={k:[l.split(' ',1)[1].strip() for l in open(f'/workspace/mtg/decks/{v}.txt') if l.strip() and l[0].isdigit()] for k,v in decks.items()}
games=[]
for f in sorted(glob.glob('/workspace/mtg/forge/playtest_batch5/g*.log')):
    g={'f':f.split('/')[-1],'cast':{k:set() for k in decks},'winner':None,'dmg':{k:C.Counter() for k in decks}}
    for l in open(f,errors='ignore'):
        l=l.strip()
        m=re.match(r'Add To Stack: Ai\(\d\)-(\w+) cast (.+?)(?: targeting.*)?$',l)
        if m and m.group(1) in decks: g['cast'][m.group(1)].add(m.group(2))
        m=re.match(r'Damage: (.+?) \(\d+\) deals (\d+) (?:combat )?damage to Ai\(\d\)-(\w+)\.',l)
        if m and m.group(3) in decks: g['dmg'][m.group(3)][m.group(1)]+=int(m.group(2))
        m=re.match(r'Game Result: .* Ai\(\d\)-(\w+) has won',l)
        if m: g['winner']=m.group(1)
    games.append(g)
out=[]
out.append(f'games parsed: {len(games)}, winners: {dict(C.Counter(g["winner"] for g in games))}')
for d in decks:
    W=[g for g in games if g['winner']==d];L=[g for g in games if g['winner']!=d]
    base=len(W)/len(games)
    out.append(f'\n== {d} ({decks[d]}): {len(W)} wins / {len(games)}  base {base:.1%}')
    rows=[]
    for c in set(lists[d])|set().union(*[g['cast'][d] for g in games]):
        if c in('Plains','Island','Swamp','Mountain','Forest'):continue
        cg=[g for g in games if c in g['cast'][d]];cw=sum(g['winner']==d for g in cg)
        rows.append((c,len(cg),cw,cw/len(cg) if cg else None))
    never=[r[0] for r in rows if r[1]==0]
    rows=[r for r in rows if r[1]>0]
    rows.sort(key=lambda r:-(r[3]))
    out.append('  cast-in>=15 games, win% when cast (high to low):')
    for c,n,w,p in rows:
        if n>=15: out.append(f'    {p:5.1%}  {w:3}/{n:3}  {c}')
    out.append(f'  never cast in 200 games ({len(never)}): '+'; '.join(sorted(never)))
    out.append(f'  rarely cast (<15 games): '+'; '.join(f'{c} {w}/{n}' for c,n,w,p in sorted(rows) if n<15))
    tot=C.Counter()
    for g in L:
        if g['winner']: pass
    # who killed this deck
    out.append('  games lost, by winner: '+str(dict(C.Counter(g['winner'] for g in L))))
open('B5_CARD_STATS.txt','w').write('\n'.join(out))
print('\n'.join(out))
