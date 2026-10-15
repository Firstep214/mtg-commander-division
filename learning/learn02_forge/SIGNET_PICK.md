# Signet replacement pick (CH001-LEARN-02, phase 1) — PENDING judge PASS
Prices: same source and rule as ledgers/LEARN02_SWAP_VERIFICATION (Scryfall default_cards 2026-10-14; strict excludes PLST/promo/memorabilia/gold-border). Script: build.py → results.json.
Forge scripts: forge/app/res/cardsfolder/cardsfolder.zip.

| Card | Strict $ (printing) | Forge script AI flags | Mana ability | Eligible |
|---|---|---|---|---|
| Worn Powerstone | 0.26 (SCD 288) | none | `Cost$ T`, Produced C x2; ETB tapped | **PICK** |
| Prismatic Lens | 0.27 (EMA 230) | **`AI:RemoveDeck:All`** | T: C; 1,T: any | NO (flag) |
| Everflowing Chalice | 0.28 (MM2 212) | none (`NeedsToPlayKickedVar:Z GE4` = AI kicks only with ≥4 untapped lands) | T: C per counter | backup |
| Star Compass | 0.49 (IMA 229) | none | ManaReflected, ETB tapped | backup (fixes colours) |
| Coldsteel Heart | 1.10 (CSP 136) | none (`AILogic$ MostProminentInComputerDeck`) | T: chosen colour; ETB tapped | backup |

None of the five is in B/C/D V1.2. Worn Powerstone has a net-positive `Cost$ T` ability (unlike the Signets' `Cost$ 1 T` filter that SIGNET_CHECK.md blames), so the AI should cast it, but no existing log shows it cast; confirm in phase 2. Downside: colourless only (no fixing); Star Compass is the colour-fixing option at +$0.23.

| Deck | Out | In | V1.2 ledger/strict | Staged V1.3 ledger/strict |
|---|---|---|---|---|
| B | Azorius Signet | Worn Powerstone | 84.06 / 87.73 | 84.06 / 87.73 |
| C | Orzhov Signet | Worn Powerstone | 90.95 / 98.19 | 90.91 / 98.15 |
| D | Izzet Signet | Worn Powerstone | 76.21 / 79.14 | 76.18 / 79.11 |
Staged files: decks/*_V1.3_PENDING.txt (not applied; no Forge .dck created).
