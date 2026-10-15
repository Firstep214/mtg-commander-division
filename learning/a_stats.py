import re,glob,collections as C,json,sys
deck=[l.split(' ',1)[1].strip() for l in open('/workspace/mtg/decks/A_tokens_V1.1.txt') if l.strip()]
def parse(f):
    g={'f':f.split('/')[-2]+'/'+f.split('/')[-1],'mull':[],'cast':C.OrderedDict(),'dmg':C.Counter(),'dmgby':C.Counter(),'turn':None,'lost':None,'lostturn':None,'winner':None,'first':None,'outturn':None}
    t=0;me=None
    for l in open(f,errors='ignore'):
        m=re.match(r'Turn: Turn (\d+) \(Ai\(\d\)-(\w+)\)',l)
        if m:
            t=int(m.group(1)); me=m.group(2)
            if g['first'] is None:g['first']=me
            if me=='A11': g.setdefault('myturns',0); g['myturns']+=1
        if l.startswith('Mulligan: Ai') and 'A11' in l: g['mull'].append(l.strip())
        m=re.match(r'Add To Stack: Ai\(\d\)-A11 cast (.+?)(?: targeting.*)?$',l.strip())
        if m: g['cast'].setdefault(m.group(1),(t,g.get('myturns',0)))
        m=re.match(r'Damage: (.+?) \(\d+\) deals (\d+) (combat )?damage to Ai\(\d\)-A11\.',l.strip())
        if m: g['dmg'][m.group(1)]+=int(m.group(2)); g['dmgby'][me]+=int(m.group(2))
        m=re.match(r'Game Outcome: Ai\(\d\)-A11 has lost because (.+)',l.strip())
        if m: g['lost']=m.group(1); g['lostturn']=t; g['lostactive']=me
        m=re.match(r'Game Result: .* Ai\(\d\)-(\w+) has won',l)
        if m: g['winner']=m.group(1)
        m=re.match(r'Game Outcome: Turn (\d+)',l)
        if m: g['outturn']=int(m.group(1))
    g['lastturn']=t
    return g
games=[parse(f) for f in sorted(glob.glob('/workspace/mtg/forge/playtest_batch1/rot*_g*.log'))+sorted(glob.glob('/workspace/mtg/forge/playtest_batch2/g*.log'))]
json.dump(games,open('a_stats.json','w'),indent=1,default=str)
def rep(gs,name):
    W=[g for g in gs if g['winner']=='A11'];L=[g for g in gs if g['winner']!='A11']
    print(f'== {name}: games {len(gs)} A11 wins {len(W)}')
    print('winner of games A lost:',C.Counter(g['winner'] for g in L))
    print('A11 elimination cause:',C.Counter(g['lost'] for g in L))
    print('A11 eliminated while active player was:',C.Counter(g.get('lostactive') for g in L))
    print('mulligan lines distinct:',C.Counter(m.split(' has ')[1] for g in gs for m in g['mull']))
    mg=[g for g in gs if any('mulligan' in m.lower() and 'kept' not in m for m in g['mull'])]
    print('games w/ A mulligan:',len(mg),'wins among them',sum(g['winner']=='A11' for g in mg))
    cw=C.Counter(c for g in W for c in g['cast']);cl=C.Counter(c for g in L for c in g['cast'])
    print('card: castW/%d castL/%d'%(len(W),len(L)))
    for c in sorted(set(deck)|set(cw)|set(cl),key=lambda c:-(cw[c]+cl[c])):
        if c.endswith('Plains') or c in('Plains',): continue
        print(f'  {c}: {cw[c]} / {cl[c]}')
    ad=[g for g in gs if 'Adeline, Resplendent Cathar' in g['cast']]
    print('Adeline cast in',len(ad),'games; wins',sum(g['winner']=='A11' for g in ad),'; own-turn# when cast:',sorted(g['cast']['Adeline, Resplendent Cathar'][1] for g in ad))
    nad=[g for g in gs if g not in ad]; print('no-Adeline games',len(nad),'wins',sum(g['winner']=='A11' for g in nad),[g['f'] for g in nad])
    tot=C.Counter();by=C.Counter()
    for g in gs: tot.update(g['dmg']);by.update(g['dmgby'])
    print('damage to A11 by source top15:',tot.most_common(15)); print('damage to A11 during turn of:',by)
for b in ('playtest_batch1','playtest_batch2'):
    rep([g for g in games if g['f'].startswith(b)],b)
rep(games,'ALL')
for g in games:
    if g['f'].startswith('playtest_batch2'): print(g['f'],g['winner'],'first',g['first'],'outturn',g['outturn'],'lastturn',g['lastturn'],'Alost',g['lost'],g['lostturn'],g.get('lostactive'),'Adeline',g['cast'].get('Adeline, Resplendent Cathar'),'mull',[m.split(' has ')[1] for m in g['mull']])
