import re,glob,json,collections,os
deck=[l.split(' ',1)[1].strip() for l in open('/workspace/mtg/decks/D_spellslinger.txt') if l.strip()]
res=[]
for f in sorted(glob.glob('/workspace/mtg/forge/playtest_batch2/g*.log'))+sorted(glob.glob('/workspace/mtg/forge/playtest_batch1/rot*_g*.log')):
    L=open(f,errors='ignore').read().splitlines()
    g=dict(log=os.path.relpath(f,'/workspace/mtg/forge'),cast=collections.Counter(),mull=None,winner=None,lost=None,lostturn=None,first=None,
           dturns=0,lands=0,dcast_by_own_turn={},cmdcasts=0,killer=collections.Counter(),lastdmg=None,firstturn=None)
    turn=0;cur=None;own=0
    for l in L:
        m=re.match(r'Turn: Turn (\d+) \(Ai\(\d\)-(\w+)\)',l)
        if m:
            turn=int(m[1]);cur=m[2]
            if g['firstturn'] is None:g['firstturn']=cur
            if cur=='D':own+=1
            continue
        m=re.match(r'Mulligan: Ai\(\d\)-D has (kept a hand of (\d+)|mulliganed)',l)
        if m and m[2]:g['mull']=7-int(m[2])
        m=re.match(r'Add To Stack: Ai\(\d\)-D cast (.+?)( targeting.*)?$',l)
        if m:
            c=m[1].strip();g['cast'][c]+=1
            g['dcast_by_own_turn'].setdefault(own,[]).append(c)
        m=re.match(r'Land: Ai\(\d\)-D played',l)
        if m:g['lands']+=1
        m=re.match(r'Damage: (.+?) deals (\d+) .*damage to Ai\(\d\)-D',l)
        if m:g['lastdmg']=(turn,cur,m[1],m[2])
        m=re.match(r'Game Outcome: Ai\(\d\)-D has lost because (.+)',l)
        if m:g['lost']=m[1];g['lostturn']=turn;g['lostlastdmg']=g['lastdmg']
        m=re.match(r'Game Result: .*Ai\(\d\)-(\w+) has won',l)
        if m:g['winner']=m[1]
        m=re.match(r'Game Outcome: Ai\(\d\)-(\w+) has lost because (.+)',l)
        if m and m[1]!='D' and g['winner'] is None: pass
    g['dturns']=own;g['turns']=turn
    g['cast']=dict(g['cast'])
    res.append(g)
json.dump(res,open('/workspace/mtg/learning/d_parsed.json','w'),indent=1)
