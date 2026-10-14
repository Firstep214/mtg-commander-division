import json,gzip,collections,datetime
D='/workspace/mtg/sources/2026-10-14/'
meta=json.load(open(D+'bulk_meta.json'))
gc=set(json.load(open(D+'game_changers.json'))['all_cards'])
bl=json.load(open(D+'banlist.json')); ban={b['name'] for b in bl['banned']}
BASICS={'Plains','Island','Swamp','Mountain','Forest','Wastes'}
best={}; leg={}; gcf={}
def key(n): return n.split(' // ')[0].lower()
for l in gzip.open(D+'default-cards-20261014090548.jsonl.gz','rt'):
  c=json.loads(l)
  if c.get('layout') in ('art_series','token','double_faced_token','emblem'): continue
  k=key(c['name']); lv=c['legalities']['commander']
  if leg.get(k)!='legal': leg[k]=lv; gcf[k]=gcf.get(k,False) or bool(c.get('game_changer'))
  if c.get('digital') or 'paper' not in c.get('games',[]): continue
  p=c['prices'].get('usd')
  if p is None: continue
  p=float(p)
  if k not in best or p<best[k][0]: best[k]=(p,c['set'].upper(),c['collector_number'])
state={'snapshot':'Scryfall bulk default_cards','bulk_updated_at':meta['updated_at'],'download_uri':meta['jsonl_download_uri'],'local_file':D+'default-cards-20261014090548.jsonl.gz',
 'sha256':'c1ca5d84148da3ac3e13db85aa27eaac1173e545942864cbf15923d0c17eaf8e','retrieved_utc':'2026-10-14T10:56:58Z',
 'rule':'per card name: minimum prices.usd (non-foil USD) across printings with "paper" in games and digital==false; prices.usd_foil/usd_etched ignored',
 'basic_land_policy':'basic lands priced at the cheapest non-foil paper printing like any other card; totals also shown excluding basics'}
json.dump(state,open(D+'scryfall_snapshot_state.json','w'),indent=1)
summary={}
for deck in ['A_tokens','B_control','C_aristocrats','D_spellslinger']:
  rows=[];unp=[];tot=0;totnb=0;n=0;issues=[]
  for line in open(f'/workspace/mtg/decks/{deck}.txt'):
    line=line.strip()
    if not line: continue
    q,name=line.split(' ',1); q=int(q); n+=q; k=key(name)
    b=best.get(k); lg=leg.get(k,'NOT FOUND'); g=name in gc or gcf.get(k,False)
    if lg!='legal': issues.append(f'{name}: scryfall commander legality = {lg}')
    if name in ban: issues.append(f'{name}: on WotC Commander banlist')
    if name=='Lutri, the Spellchaser': issues.append('Lutri present: legal in 99/commander, not as companion')
    if g: issues.append(f'{name}: GAME CHANGER (not allowed in Bracket 2)')
    if b is None: unp.append(name); rows.append((q,name,None,'','')); continue
    sub=round(b[0]*q,2); tot+=sub
    if name not in BASICS: totnb+=sub
    rows.append((q,name,b[0],f'{b[1]} #{b[2]}',sub))
  tot=round(tot,2); totnb=round(totnb,2); m=round(100-tot,2)
  summary[deck]=dict(cards=n,total=tot,total_ex_basics=totnb,margin=m,unpriced=unp,issues=issues)
  with open(f'/workspace/mtg/decks/PRICE_LEDGER_{deck}.md','w') as f:
    f.write(f'# Price ledger — {deck} V1\n\nSnapshot: Scryfall bulk `default_cards` updated_at {meta["updated_at"]} ({meta["jsonl_download_uri"]}); state file `{D}scryfall_snapshot_state.json`. Generated 2026-10-14 (Asia/Manila).\n\nRule: {state["rule"]}.\nBasic-land policy: {state["basic_land_policy"]}.\n\n')
    f.write(f'**Cards: {n} · Total: ${tot:.2f} · Total excl. basics: ${totnb:.2f} · Margin vs $100 cap: ${m:.2f}**' + (' ⚠️ OVER CAP' if m<0 else (' ⚠️ THIN MARGIN (<$10) — re-price before purchase' if m<10 else '')) + '\n\n')
    f.write('Unpriced cards: ' + (', '.join(unp) if unp else 'none') + '\n\nLegality / Game Changer check (banlist.json, game_changers.json, Scryfall legalities.commander): ' + ('; '.join(issues) if issues else 'no banned, not-legal, or Game Changer cards found') + '\n\n')
    f.write('| Qty | Card | Unit USD | Cheapest printing | Line USD |\n|---|---|---|---|---|\n')
    for q,nm,u,pr,s in rows: f.write(f'| {q} | {nm} | {"" if u is None else f"{u:.2f}"} | {pr} | {"UNPRICED" if u is None else f"{s:.2f}"} |\n')
json.dump(summary,open(D+'price_summary.json','w'),indent=1); print(json.dumps(summary,indent=1))
