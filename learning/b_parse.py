import re,glob,collections,json,os
D="/workspace/mtg/decks/"
def load(f): return [l.split(" ",1)[1].strip() for l in open(D+f) if l.strip() and l[0].isdigit()]
decks={"A11":load("A_tokens_V1.1.txt"),"B":load("B_control.txt"),"C":load("C_aristocrats.txt"),"D":load("D_spellslinger.txt")}
owner={}
for k,v in decks.items():
    for c in v: owner.setdefault(c,k)
Bset=set(decks["B"])
casts=collections.Counter(); castW=collections.Counter(); castL=collections.Counter(); gamesCast=collections.defaultdict(set)
rows=[];killer=collections.Counter();dmgsrc=collections.Counter();brago=collections.Counter()
for f in sorted(glob.glob("/workspace/mtg/forge/playtest_batch2/g*.log")):
    g=os.path.basename(f)[:-4]; L=open(f,errors="ignore").read().splitlines()
    turn=0;active=None;winner=None;Bturns=0;lands4=None;Blands=0;mull="7";Bdead=None;lastsrc=None;first=None;bl=40;finalturn=None
    gc=collections.Counter(); deadOrder=[]; life={}
    for l in L:
        m=re.match(r"Turn: Turn (\d+) \(Ai\(\d\)-(\w+)\)",l)
        if m:
            turn=int(m.group(1));active=m.group(2); first=first or active
            if active=="B": Bturns+=1
            if Bturns==5 and lands4 is None and active=="B": lands4=Blands
            continue
        if l.startswith("Mulligan: Ai") and "-B " in l and "kept a hand of" in l: mull=re.search(r"of (\d+)",l).group(1)
        if l.startswith("Land: Ai") and "-B played" in l: Blands+=1
        m=re.match(r"Add To Stack: Ai\(\d\)-B cast (.+?)( targeting.*)?$",l)
        if m:
            c=m.group(1).strip(); gc[c]+=1
            if c.startswith("Brago"): brago[g]+=1
        m=re.match(r"Damage: (.+?) \(\d+\) deals (\d+) .*damage to Ai\(\d\)-B\.",l)
        if m and Bdead is None:
            src=m.group(1); o=owner.get(src,"token/other:"+src); lastsrc=(o,src); dmgsrc[o]+=int(m.group(2))
        m=re.match(r"Life: Life: Ai\(\d\)-(\w+) (-?\d+) > (-?\d+)",l)
        if m:
            p=m.group(1);life[p]=int(m.group(3))
            if int(m.group(3))<=0 and p not in deadOrder: deadOrder.append(p)
            if p=="B" and int(m.group(3))<=0 and Bdead is None: Bdead=turn; deathactive=active
        m=re.search(r"Ai\(\d\)-(\w+) has won",l)
        if m: winner=m.group(1)
        m=re.match(r"Game Outcome: Turn (\d+)",l)
        if m: finalturn=int(m.group(1))
    if lands4 is None: lands4=Blands
    for c,n in gc.items():
        casts[c]+=n; gamesCast[c].add(g); (castW if winner=="B" else castL)[c]+=1
    if Bdead and winner!="B": killer[(deathactive,lastsrc)]+=1
    rows.append(dict(g=g,first=first,winner=winner,turns=finalturn,mull=mull,Bdead=Bdead,deathactive=deathactive if Bdead else None,lastsrc=lastsrc if Bdead else None,lands_by_B_turn4=lands4,Bturns=Bturns,brago=brago[g],order=deadOrder,ncast=sum(gc.values()),top=gc.most_common(6)))
json.dump(dict(rows=rows,casts=casts,castW=castW,castL=castL,gamesCast={k:sorted(v) for k,v in gamesCast.items()},never=sorted(c for c in Bset if c not in gamesCast),dmg=dmgsrc,killer=[[str(k),v] for k,v in killer.most_common()]),open("/workspace/mtg/learning/b_parse_out.json","w"),indent=1,default=list)
for r in rows: print(r)
