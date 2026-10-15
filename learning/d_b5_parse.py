import re,glob,json,collections,os
DK={'A12':'decks/A_tokens_V1.2.txt','B13':'decks/B_control_V1.3.txt','C13':'decks/C_aristocrats_V1.3.txt','D13':'decks/D_spellslinger_V1.3.txt'}
owner={}
for d,p in DK.items():
    for l in open(p):
        if l.strip(): owner.setdefault(l.split(' ',1)[1].strip(),d)
out=[]
for f in sorted(glob.glob('forge/playtest_batch5/g*.log')):
    L=open(f,errors='ignore').read().splitlines()
    g=dict(log=os.path.basename(f),winner=None,cast=collections.Counter(),death=None,dmg_out=collections.Counter())
    turn=0;active=None;prev=None;ids={}
    for i,l in enumerate(L,1):
        m=re.match(r'Turn: Turn (\d+) \(Ai\(\d\)-(\w+)\)',l)
        if m: turn=int(m[1]);active=m[2];continue
        m=re.match(r'Add To Stack: Ai\(\d\)-(\w+) cast (.+?)(?: targeting.*)?$',l)
        if m:
            if m[1]=='D13': g['cast'][m[2]]+=1
            continue
        m=re.match(r'Damage: (.+?) \((\d+)\) deals (\d+) .*damage to Ai\(\d\)-(\w+)',l)
        if m:
            src=m[1];dk=owner.get(src) or (f'token/active={active}' if 'Token' in src else '?')
            if m[4]=='D13': prev=(i,src,dk,int(m[3]))
            elif dk=='D13': g['dmg_out'][src]+=int(m[3])
            continue
        m=re.match(r'Life: Life: Ai\(\d\)-D13 (-?\d+) > (-?\d+)',l)
        if m and int(m[2])<=0 and g['death'] is None:
            # find nearest preceding damage/lose line
            ctx=None
            for j in range(i-1,max(0,i-12),-1):
                if re.search(r'D13',L[j-1]) and re.match(r'(Damage|Resolve Stack|Add To Stack|Combat)',L[j-1]): ctx=(j,L[j-1][:200]);break
            g['death']=dict(line=i,turn=turn,active=active,lastdmg=prev,ctx=ctx,life=(int(m[1]),int(m[2])))
        m=re.match(r'Game Result: .*Ai\(\d\)-(\w+) has won',l)
        if m:g['winner']=m[1]
    g['cast']=dict(g['cast']);g['dmg_out']=dict(g['dmg_out']);out.append(g)
json.dump(out,open('learning/d_b5_parsed.json','w'),indent=1)
