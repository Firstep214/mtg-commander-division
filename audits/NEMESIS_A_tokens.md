# NEMESIS audit — A_tokens (Adeline, Resplendent Cathar) V1
**VERDICT: REVISE**
Auditor: Nemesis · task CH001-AUD-NEM · 2026-10-14 (Asia/Manila)
Sources: decks/*.txt; decks/PRICE_LEDGER_*.md; sources/2026-10-14/default-cards-20261014090548.jsonl.gz (sha256 c1ca5d84…eaf8e, matches scryfall_snapshot_state.json; byte-identical to data/default.jsonl.gz); banlist.json; game_changers.json. Scripts: audits/nemesis_recompute.py, audits/nemesis_strict_retail.py. "Strict retail" = cheapest printing excluding The List (PLST), promo, World Championship gold-bordered/memorabilia printings. Prior Grok pre-agent audit (decks/AUDIT_*.md) NOT used.

## 1. Budget (cap $100.00, house rule per SOURCES.md / ledger)
- Independent recompute under the ledger's stated rule (min prices.usd, paper, non-digital): **$95.61**, margin **$4.39**. All 68 ledger rows match my per-card min price and qty exactly; no missing/extra rows; arithmetic correct; 33 Plains × $0.06 = $1.98 (C15 326).
- **Fragility (main finding):** the total depends on printings that are hard or impossible to buy at the listed price: Wrath of God **WC04 jn58** (World Championship gold-bordered memorabilia, not tournament-legal; normal printing DMR 279 = $3.51, +$2.48), Mother of Runes PLST ULG-14 (CMD 21 = $11.21, +$3.36), Welcoming Vampire PVOW 46p promo (+$0.28), Archivist of Oghma PLST (+$0.65), plus 6 smaller PLST rows.
- **Strict-retail total: $102.78 → OVER CAP by $2.78.** The deck passes only on the letter of the ledger rule, with a $4.39 cushion that any single price move erodes.
- Counts/legality: 100 cards incl. commander ✔; singleton ✔ (only Plains >1); colour identity W ✔; all commander-legal ✔; 0 banned, 0 Game Changers (Scryfall flag + game_changers.json) ✔.

## 2. Combos (fresh pairwise review of oracle text, + commander)
- 2-card infinites: **none found.** Checked untap/recursion/token-loop/ETB-blink candidates (Skullclamp, Mirror Entity, Felidar Retreat, Sigil of the Empty Throne, Divine Visitation, Cathars' Crusade, Dawn of Hope, Staff of the Storyteller, Hallowed Spiritkeeper, Selfless Spirit, Benevolent Bodyguard). Skullclamp + X/1 tokens is card-draw, finite.
- 3-card infinites: none found.

## 3. Roles (my count from oracle)
- Lands 36 (33 Plains + 3 utility) · Ramp 9 (5 rocks + Bauble, Knight of the White Orchid, Weathered Wayfarer, Gift of Estates; Weathered/Knight/Gift are conditional) · Draw ~10 engines · Spot removal 9 · Sweepers 3 (Wrath, Austere Command, Sunfall) + Elspeth −3.
- **Anti-synergy:** 3 symmetrical wipes in a go-wide deck; Wrath/Sunfall kill own board.
- **Unsupported win claim:** deck doc says "anthems + overruns", but it has **no true overrun**; Moment of Heroism is a single-target +2/+2. Only mass pumps are static anthems + Cathars' Crusade/Felidar Retreat counters.
- Commander over-reliance: moderate; Adeline is the main token source and has no hexproof. Mother of Runes/Selfless Spirit/Unbreakable Formation/Flawless Maneuver cover it.
- Fragile: Rally the Ranks needs a typed board (choose Human = Adeline tokens only). Mentor of the Meek and Dawn of Hope are mana sinks in a 36-land deck with low ramp.
- Weakest slots: Gift of Estates, Moment of Heroism, Wrath of God (anti-synergy + gold-border price), Bennie Bracks ($11.15 for a conditional draw engine), Rabble Rousing, Militia Bugler, Increasing Devotion (7 MV), Cathar Commando.

## 4. Proposed swaps (do not apply; Forge owns V1.1)
| OUT | IN | Reason | Budget delta (ledger rule / strict retail) |
|---|---|---|---|
| Wrath of God ($1.03 WC04; $3.51 DMR) | Inspired Charge ($0.03 M15 272) | Wipe is anti-synergy; adds the overrun the doc claims | −$1.00 / −$3.48 |
| Bennie Bracks, Zoologist ($11.15 MKC 57) | Rumor Gatherer ($0.35 PLST SNC-29 / $0.47 CLB 705) | Restores budget margin; draw on creatures entering | −$10.80 / −$10.68 |
| Moment of Heroism ($0.04 CNS 74) | Make a Stand ($0.16 PLST OGW-26 / $0.18 M19 26) | Team pump + wipe protection | +$0.12 / +$0.14 |
| Gift of Estates ($1.17 C14 73) | Thraben Inspector ($0.16 J22 255) | Gift is often dead; Inspector is a 1-drop body + clue | −$1.01 / −$1.01 |
All IN cards: mono-W, commander-legal, not GC (Scryfall snapshot). **After the swaps: $82.92 by ledger rule (margin $17.08); $87.75 strict retail.**
If no swaps are taken, at minimum require that the Wrath of God and Mother of Runes purchases use the listed printings, or re-price.
