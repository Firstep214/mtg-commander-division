# NEMESIS audit — B_control (Brago, King Eternal) V1
**VERDICT: PASS** (minor revisions recommended)
Sources: decks/*.txt; decks/PRICE_LEDGER_*.md; sources/2026-10-14/default-cards-20261014090548.jsonl.gz (sha256 c1ca5d84…eaf8e, matches scryfall_snapshot_state.json; byte-identical to data/default.jsonl.gz); banlist.json; game_changers.json. Scripts: audits/nemesis_recompute.py, audits/nemesis_strict_retail.py. "Strict retail" = cheapest printing excluding The List (PLST), promo, World Championship gold-bordered/memorabilia printings. Prior Grok pre-agent audit (decks/AUDIT_*.md) NOT used.

## 1. Budget
- Recompute: **$83.50** (margin $16.50). All 79 ledger rows match my numbers. Strict retail: **$87.17** (WC00 Counterspell +$0.92, WC04 Wrath +$2.48, PLST/promo small deltas), still under cap.
- 100 cards ✔, singleton ✔, identity WU ✔, legal ✔, 0 banned, 0 GC ✔.

## 2. Combos
- 2-card infinites: **none.** Checked Brago + every ETB/flicker card, Restoration Angel/Soulherder/Conjurer's Closet/Teleportation Circle/Ghostly Flicker/Ephemerate with Venser, Man-o'-War, Kor Skyfisher, Glen Elendra (persist reset by flicker is finite), Mirrormade, Teferi. Ghostly Flicker loops need Mystic Sanctuary/Archaeomancer (absent).
- 3-card: none found.

## 3. Roles / risks
- Lands 37, ramp 11, draw ~15, targeted removal/bounce ~12, counters 5, wipes 4 (Supreme Verdict, Wrath, Austere, Hallowed Burial).
- **Commander over-reliance:** Brago is the engine but needs to connect; flicker density (8 non-Brago blink effects) mitigates.
- **Anti-synergy:** Spell Queller: when it leaves (any Brago/Closet/Resto blink), the opponent casts the exiled spell for free.
- Win cons thin and slow (Sun/Frost Titan, Dream Trawler, Teferi, Elspeth, Agent steals); doc claims are supported but there is no quick close.
- Weakest: Spell Queller, Eerie Interlude ($6.88 for redundant flicker), Negate, Burnished Hart, Thirst for Discovery, Fblthp.

## 4. Proposed swaps
| OUT | IN | Reason | Budget delta |
|---|---|---|---|
| Spell Queller ($0.29 INR 435) | Cast Out ($0.09 C20 79) | Removes blink anti-synergy; flash removal that Brago re-targets | −$0.20 → $83.30 |
