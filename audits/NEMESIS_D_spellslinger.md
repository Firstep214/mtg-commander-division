# NEMESIS audit — D_spellslinger (Veyran, Voice of Duality) V1
**VERDICT: PASS** (doc correction + disclosure required)
Sources: decks/*.txt; decks/PRICE_LEDGER_*.md; sources/2026-10-14/default-cards-20261014090548.jsonl.gz (sha256 c1ca5d84…eaf8e, matches scryfall_snapshot_state.json; byte-identical to data/default.jsonl.gz); banlist.json; game_changers.json. Scripts: audits/nemesis_recompute.py, audits/nemesis_strict_retail.py. "Strict retail" = cheapest printing excluding The List (PLST), promo, World Championship gold-bordered/memorabilia printings. Prior Grok pre-agent audit (decks/AUDIT_*.md) NOT used.

## 1. Budget
- Recompute: **$80.45** (margin $19.55). All 77 rows match. Strict retail **$83.38** (WC00 Counterspell +$0.92, Electrostatic Field PLST +$0.95, Pongify PLST +$0.67, etc.).
- 100 ✔ (Fire // Ice resolved as split card), singleton ✔, UR identity ✔, legal ✔, 0 GC ✔.

## 2. Combos
- 2-card infinites: **none.** Checked Veyran + Niv-Mizzet, Parun (2 draws per instant/sorcery → 2 pings each; finite), Thermo-Alchemist untaps (no mana), Storm-Kiln Artist + copy spells (Reverberate/Galvanic/Increasing Vengeance/Storm of Saruman: finite), Mystic Sanctuary + recursion (no loop), Mizzix's Mastery/Past in Flames (one-shot). No Curiosity/Ophidian Eye/Dualcaster/Twinflame pieces.
- **Informational, near-deterministic engine (3 cards):** Veyran + Storm-Kiln Artist (2 Treasures per spell) + Archmage Emeritus (2 draws per spell). Every 1-mana cantrip nets +1 mana and ~3 cards; with Guttersnipe or Niv-Mizzet the turn becomes lethal. Not technically infinite (it runs out of library and spells), but it is a Bracket-2 expectation risk. Disclose it.

## 3. Roles / risks
- Lands 38 (high for an MV-2.6 deck), ramp 7 rocks + treasure makers, draw ~20, interaction 15, wipes 2 (Blasphemous Act, Anger of the Gods). Both wipes kill your own payoff creatures.
- **Unsupported claim:** archetype line says "alt-win pressure", but the list has **no alternate-win card**. Fix the doc.
- **Commander over-reliance:** high. The payoffs are 1-3 toughness creatures, and Veyran doubling is the stated multiplier.
- Weakest: Opt, Consider, Essence Scatter, Pongify, Increasing Vengeance, Galvanic Iteration, Thrill of Possibility.

## 4. Proposed swaps
None required for budget/legality. Optional: cut 1 land (38→37) for an extra cantrip. Not priced here, so I'm not proposing a specific IN.
