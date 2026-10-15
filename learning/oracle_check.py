import re,json,glob,os,statistics as st
D='/workspace/mtg/forge/playtest_batch2'
rep={}
for l in open('/workspace/mtg/forge/PLAYTEST_BATCH2.md'):
    m=re.match(r'\| (g\d\d)\.log \|.*?\| (\w+) \| (\w+) \| Y \| (\w+) \| (\d+) \|.*\| (\d+) \|$',l)
    if m: rep[m[1]]=dict(roll=m[2],first=m[3],winner=m[4],turns=int(m[5]),tex=int(m[6]))
out={}
for f in sorted(glob.glob(D+'/g*.log')):
    g=os.path.basename(f)[:3]; L=open(f,errors='replace').read().split('\n')
    r=dict(turnlines=[],mull={},lost={})
    for i,l in enumerate(L,1):
        m=re.match(r'Turn: Turn (\d+) \(Ai\(\d\)-(\w+)\)',l)
        if m: r['turnlines'].append((int(m[1]),m[2],i))
        m=re.search(r'Game Result: .*Ai\(\d\)-(\w+) has won',l)
        if m: r['winner']=(m[1],i)
        m=re.match(r'Game Outcome: Turn (\d+)',l)
        if m: r['outturn']=(int(m[1]),i)
        m=re.match(r'Mulligan: Ai\(\d\)-(\w+) has mulliganed down to (\d)',l)
        if m: r['mull'].setdefault(m[1],[]).append(int(m[2]))
        m=re.match(r'Game Outcome: Ai\(\d\)-(\w+) has lost because (.*)',l)
        if m: r['lost'][m[1]]=m[2]
        if 'TimeoutException' in l: r['tex']=r.get('tex',0)+1
    tl=r['turnlines']
    r['first']=tl[0][1]; r['first_line']=tl[0][2]; r['lastturn']=tl[-1][0]; r['nturnlines']=len(tl)
    r['seq_ok']=all(tl[k][0]==k+1 for k in range(len(tl)))
    r['dupes']=sum(1 for k in range(1,len(tl)) if tl[k][1]==tl[k-1][1])
    r['per_deck_turns']={d:sum(1 for t in tl if t[1]==d) for d in ['A11','B','C','D']}
    del r['turnlines']; out[g]=r
json.dump(dict(rep=rep,log=out),open('/workspace/mtg/learning/oracle_check.json','w'),indent=1)
from collections import Counter
print('rep rows',len(rep))
print('winners',Counter(o['winner'][0] for o in out.values()))
print('first',Counter(o['first'] for o in out.values()))
print('first wins',Counter(o['winner'][0] for o in out.values() if o['winner'][0]==o['first']))
mis=[g for g in out if out[g]['winner'][0]!=rep[g]['winner'] or out[g]['first']!=rep[g]['first'] or out[g]['outturn'][0]!=rep[g]['turns']]
print('mismatch',mis)
rat=[out[g]['lastturn']/out[g]['outturn'][0] for g in out]
print('ratio',min(rat),max(rat),st.mean(rat)); print([ (g,out[g]['lastturn'],out[g]['outturn'][0]) for g in out if out[g]['lastturn']!=2*out[g]['outturn'][0]])
print('seq_ok all',all(o['seq_ok'] for o in out.values()),'dupes',sum(o['dupes'] for o in out.values()))
t=[o['outturn'][0] for o in out.values()];print('turns mean',st.mean(t),min(t),max(t))
print('tex',{g:out[g].get('tex',0) for g in out if out[g].get('tex')}, sum(o.get('tex',0) for o in out.values()))
print('mull',{g:o['mull'] for g in out if o['mull']})
print('lost reasons',Counter(v for o in out.values() for v in o['lost'].values()))
