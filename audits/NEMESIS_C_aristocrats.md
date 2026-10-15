# NEMESIS audit — C_aristocrats (Teysa Karlov) V1
**VERDICT: PASS** (minor revisions recommended)
Sources: decks/*.txt; decks/PRICE_LEDGER_*.md; sources/2026-10-14/default-cards-20261014090548.jsonl.gz (sha256 c1ca5d84…eaf8e, matches scryfall_snapshot_state.json; byte-identical to data/default.jsonl.gz); banlist.json; game_changers.json. Scripts: audits/nemesis_recompute.py, audits/nemesis_strict_retail.py. "Strict retail" = cheapest printing excluding The List (PLST), promo, World Championship gold-bordered/memorabilia printings. Prior Grok pre-agent audit (decks/AUDIT_*.md) NOT used.

## 1. Budget
- Recompute: **$85.97** (margin $14.03). All 79 rows match. Strict retail **$93.22**: Ashnod's Altar is priced from **WC00 nl274 (gold-bordered memorabilia) $8.15**; the normal printing 6ED 274 is **$14.30** (+$6.15). Still under cap, but most of the cushion is gone.
- 100 ✔, singleton ✔, WB identity ✔ (Sifter of Skulls devoid/colourless ✔), legal ✔, 0 GC ✔.

## 2. Combos
- 2-card infinites: **none.** Checked Ashnod's Altar / Pitiless Plunderer / Viscera Seer / Carrion Feeder / Yahenni / Bartolomé / Priest with every recursion piece (Kaya's Ghostform one-shot, Undying Evil is a one-shot spell, Sevinne's/Unearth/Sorin/Victimize finite). No persist/undying creature and no Gravecrawler-type loop. Teysa doubles drains but loops nothing.
- 3-card: none in deck. Note: Ashnod's Altar + Pitiless Plunderer + any persist/undying creature would be infinite. Do not add one (doc already warns).

## 3. Roles / risks
- Lands 36, ramp 9 rocks + Plunderer/treasures, draw ~10, spot removal 10 (strong), wipes 1 (Damn) + Living Death.
- Liesa in the 99 taxes your own spells (2 life per spell) in a deck that also pays life with Night's Whisper, Painful Truths, Dark Prophecy, Infernal Grasp, Anguished Unmaking, Midnight Reaper: a self-damage pile-up.
- Graveyard-hate fragile (doc admits). Teysa is not required; the drain pieces work alone.
- Weakest: **Darkest Hour ($4.81, near-blank)**, Kaya's Ghostform, Undying Evil, Martyr of Dusk, Return to the Ranks, Liesa.

## 4. Proposed swaps
| OUT | IN | Reason | Budget delta |
|---|---|---|---|
| Darkest Hour ($4.81 7ED 128) | Cast Out ($0.09 C20 79) | Blank card → flexible removal; frees budget | −$4.72 → $81.25 |
