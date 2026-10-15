import json
r=json.load(open('results.json'))
CR="""## CR citations (quoted from MagicCompRules_20260925.txt, effective September 25, 2026)
- 903.3: "Each deck has a legendary card designated as its commander. That card must be either (a) a creature card, (b) a Vehicle card, or (c) a Spacecraft card with one or more power/toughness boxes."
- 903.3a: "Some cards have an ability that states the card can be your commander."
- 903.4: "The color identity of a card is the color or colors of any mana symbols in that card's mana cost or rules text, plus any colors defined by its characteristic-defining abilities (see rule 604.3) or color indicator (see rule 204)."
- 903.4c: "Reminder text is ignored when determining a card's color identity." / 903.4d: back face of DFC included.
- 903.5a: "Each deck must contain exactly 100 cards, including its commander."
- 903.5b: "Other than basic lands, each card in a Commander deck must have a different English name."
- 903.5c: "A card can be included in a Commander deck only if every color in its color identity is also found in the color identity of the deck's commander."
- 903.5d: basic land types may only be included if each color of mana it could produce is in the commander's identity.
- 702.124a/h: partner abilities allow two commanders (not applicable here: commander has no partner ability).
"""
NOTES={'C_aristocrats':"Reviewed manually, not infinite as a pair: Ashnod's Altar with Teysa Karlov, Pitiless Plunderer, Yahenni, Sifter of Skulls, or Kaya's Ghostform. Each one needs a third piece (a recursion engine or a persistent/undying creature) before it loops. Known 3-card risk: Ashnod's Altar + Pitiless Plunderer + a recursive creature. Teysa doubling death triggers increases drain output but does not create a loop.",
'D_spellslinger':"Reviewed manually, not infinite as a pair: Mizzix's Mastery + Past in Flames (finite: the graveyard empties) and Storm-Kiln Artist + Haughty Djinn (no untap or recursion). No Mystic Sanctuary + Ghostly Flicker pair: Ghostly Flicker is not in this deck.",
'B_control':"Ghostly Flicker is here, but no Mystic Sanctuary, Archaeomancer, Mnemonic Wall or Peregrine Drake. Brago + flicker cards make value, not a loop. Restoration Angel and Agent of Treachery have no Kiki-Jiki or Deadeye partner.",
'A_tokens':"No known pair found. Mirror Entity, Felidar Retreat and Cathars' Crusade each lack an Intruder Alarm-style partner."}
for d,v in r.items():
    R=v['res']; ok=all(x[0] for x in R.values())
    L=[f"# ARBITER audit — {d}",f"Task CH001-AUD-ARB · Arbiter · 2026-10-14 (PHT) · deck sha256 `{v['sha256']}` (deck not modified)","",
       f"## OVERALL: {'PASS' if ok else 'FAIL'}","",f"Commander: {v['commander']}  (Bracket 2 target)","","| Check | Result | Detail |","|---|---|---|"]
    def f(k): return 'PASS' if R[k][0] else 'FAIL'
    c=R['commander'][1]
    L+= [f"| Card names resolve (Scryfall oracle bulk) | {f('names')} | {R['names'][1] or 'all names resolved'} |",
    f"| Count = 100 incl. commander (CR 903.5a) | {f('count')} | total {R['count'][1]} |",
    f"| Singleton (CR 903.5b) | {f('singleton')} | {R['singleton'][1] or 'no duplicates; only basics have qty >1'} |",
    f"| Commander eligibility (CR 903.3) | {f('commander')} | line {c['line']} `{c['text']}`; {c['type']}; partner ability: {c['partner']}; Scryfall commander legality: {c['legality']} |",
    f"| Color identity (CR 903.4, 903.5c/d) | {f('color_identity')} | commander identity {R['color_identity'][1][0]}; off-identity: {R['color_identity'][1][1] or 'none'} |",
    f"| Bans (banlist.json 42 named + category bans + Scryfall legality) | {f('bans')} | {R['bans'][1] or 'none'} |",
    f"| Game Changers (Bracket 2 = 0) | {f('game_changers')} | count {len(R['game_changers'][1])} {R['game_changers'][1] or ''} |",
    f"| 2-card infinite combos | {f('combos')} | {R['combos'][1][0] or 'none found'} |",
    f"| Extra-turn cards | {f('extra_turns')} | {R['extra_turns'][1] or 'none (oracle text search for \"extra turn\")'} |",
    f"| Mass land destruction | {f('mld')} | {R['mld'][1] or 'none (oracle text regex)'} |","",
    "## Combo review notes",NOTES[d],"",CR,
    "## Method and source gaps",
    "- Script: /workspace/mtg/audits/arbiter_scripts/audit.py (results.json). Card data: /workspace/mtg/data/oracle.jsonl.gz (Scryfall oracle_cards, updated 2026-10-14T09:01Z = 17:01 PHT). Color identity comes from Scryfall `color_identity`, which follows CR 903.4 and includes rules-text symbols.",
    "- Source hashes: SHA256SUMS verified OK for all text/HTML sources.",
    "- Game Changers: game_changers.json all_cards plus per-colour lists plus the Scryfall `game_changer` flag (Tergrid DFC name variance handled).",
    "- Commander = line 1 of the deck file (file convention; the deck has no explicit commander marker).",
    "- GAP: the local sources do not contain the per-bracket expectation text for two-card infinites, extra turns or mass land denial. formats_commander.txt only names these as \"barometers\". Zero-tolerance here applies Voltaire's house rule (SOURCES.md), not quoted Wizards text.",
    "- LIMIT: combo detection uses a curated list of known pairs plus a manual review of the decklist. It is not an exhaustive combo database (no Commander Spellbook snapshot is in sources). Extra-turn and MLD checks are oracle-text regexes plus a manual read of the list."]
    open(f'/workspace/mtg/audits/ARBITER_{d}.md','w').write('\n'.join(L)+'\n')
    print(d,'PASS' if ok else 'FAIL')
