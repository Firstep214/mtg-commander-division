import json,gzip,re
D='/workspace/mtg/sources/2026-10-14/'
BASE={'A':'A_tokens_V1.1','B':'B_control','C':'C_aristocrats','D':'D_spellslinger'}
SW={'A':[('Sunfall','Ghostly Prison'),('Mirror Entity','Get Lost')],'B':[("Conjurer's Closet",'Fumigate'),('Mystic Confluence','Settle the Wreckage')],
'C':[('Wake the Dead','Massacre Wurm'),("Sevinne's Reclamation",'Pestilence')],'D':[("Mizzix's Mastery",'Fiery Cannonade'),('Past in Flames','Coruscation Mage')]}
gc={n.lower() for n in json.load(open(D+'game_changers.json'))['all_cards']}
ban={b['name'].lower() for b in json.load(open(D+'banlist.json'))['banned']}
k=lambda n:n.split(' // ')[0].lower()
led={};strict={};info={}
for l in gzip.open(D+'default-cards-20261014090548.jsonl.gz','rt'):
  c=json.loads(l)
  if c.get('layout') in('art_series','token','double_faced_token','emblem'):continue
  n=k(c['name'])
  if n not in info or c['legalities']['commander']=='legal':
    info[n]=dict(ci=c['color_identity'],leg=c['legalities']['commander'],gc=bool(c.get('game_changer')),text=c.get('oracle_text') or ' / '.join(f.get('oracle_text','') for f in c.get('card_faces',[])))
  if c.get('digital') or 'paper' not in c.get('games',[]) or c['prices'].get('usd') is None:continue
  p=float(c['prices']['usd']); tag=(p,c['set'].upper(),c['collector_number'])
  if n not in led or p<led[n][0]: led[n]=tag
  if not(c['set_type'] in('memorabilia','promo') or c['set']=='plst' or c.get('promo')):
    if n not in strict or p<strict[n][0]: strict[n]=tag
out={}
for d,f in BASE.items():
  deck=[(int(l.split(' ',1)[0]),l.split(' ',1)[1].strip()) for l in open(f'/workspace/mtg/decks/{f}.txt') if l.strip()]
  names=[n for q,n in deck]; cid=set(info[k(names[0])]['ci'])
  def tot(tbl,dk):return round(sum(q*tbl.get(k(n),(0,))[0] for q,n in dk),2),[n for q,n in dk if k(n) not in tbl]
  pre=tot(led,deck); pres=tot(strict,deck)
  new=list(deck); rows=[]
  for o,i in SW[d]:
    ii=info.get(k(i),{})
    rows.append(dict(out=o,inn=i,out_present=o in names,in_absent=i not in names,legal=ii.get('leg'),ci=ii.get('ci'),ci_ok=set(ii.get('ci',['?']))<=cid,
      ban=k(i) in ban,gc=k(i) in gc or ii.get('gc'),price_out=led.get(k(o)),price_in=led.get(k(i)),strict_in=strict.get(k(i)),strict_out=strict.get(k(o)),
      extra=bool(re.search('extra turn',ii.get('text',''),re.I)),text=ii.get('text','')))
    new=[(q,i if n==o else n) for q,n in new]
  out[d]=dict(base=f,cid=''.join(sorted(cid)),count=sum(q for q,n in new),pre=pre,pre_strict=pres,post=tot(led,new),post_strict=tot(strict,new),swaps=rows)
json.dump(out,open('/workspace/mtg/learning/arbiter_swap/results.json','w'),indent=1)
for d,v in out.items():
  print(d,v['base'],v['cid'],v['count'],'pre',v['pre'],v['pre_strict'],'post',v['post'],v['post_strict'])
  for r in v['swaps']:print('  ',{x:y for x,y in r.items() if x!='text'});print('    ',r['text'][:300].replace('\n',' | '))
