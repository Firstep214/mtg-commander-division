# Deck B (Brago control): Analysis, CH001-LEARN-01
Author: Nyx (Deck B playtester). Written 2026-10-15 (PHT). Deck file: `/workspace/mtg/decks/B_control.txt` (V1, 100 cards). **The deck was not modified.**
Sources: `forge/PLAYTEST_BATCH1.md`, `forge/PLAYTEST_BATCH2.md`, `forge/playtest_batch2/g01–g50.log` (all 50 exist), `/workspace/mtg/PLAYTEST_RULES.md` (at the repo root, not under forge/), `decks/PRICE_LEDGER_B_control.md`, `sources/2026-10-14/game_changers.json`, `data/default.jsonl.gz` (Scryfall bulk 2026-10-14).
Parser (reproducible): `learning/b_parse.py`. Raw output: `learning/b_parse_out.json`. Every number below comes from those logs or reports unless it is marked otherwise.

## Method notes and caveats
- "Turn" means the log's `Turn: Turn N` line counter. **Gap:** that counter is exactly 2× the `Game Outcome: Turn` value used in the batch reports (g16: 94 `Turn:` lines vs "Game Outcome: Turn 47"). Log turn numbers here are therefore not comparable to the report's "Turns" column. The B-turn counts (B's own turns) are unaffected.
- B's death turn is the first `Life:` line where B is at ≤0. The "lethal source" is the last `Damage:` line to B before that. Life loss that isn't damage (for example drain) is not attributed, so the source of a drain kill can be wrong.
- Cards in hand aren't logged. "Never cast" means no `Add To Stack: …-B cast X` line. It does not mean the card was never drawn.
- Forge AI pilots, n=50. Batch 2 itself states about ±14pp per deck. Cast-in-win/loss splits are correlations, not causes.
- I did not re-parse the Batch 1 logs. Its figure (B 6/24, 25%) is quoted from PLAYTEST_BATCH1.md.

## Record
- Batch 2: **9/50 wins (18%)**: g02, g03, g07, g13, g25, g33, g41, g42, g47. B went first 9 times and won 4 of them (g02, g07, g25, g47). Both sets match PLAYTEST_BATCH2.md.
- Batch 1 (report): 6/24 (25%).
- B's wins ended at report turn 24–36 (g42/g47 24, g07 27, g25 29, g02 30, g03 32, g41 33, g33 34, g13 36).
- In all 41 losses, B's life reached ≤0 before the game ended (no win was decided with B alive). B's finishing position among the losers: 1st eliminated 13×, 2nd 15×, 3rd 13×. B was first out in g04, g05, g08, g11, g18, g20, g27, g28, g30, g32, g34, g48, g50.

## Why B lost
- **Eventual winner of B's 41 losses:** A11 20, C 12, D 9.
- **Whose turn B died on:** A11 20, C 8, D 8, B's own turn 5 (g09, g10, g22, g35, g45, where C/D drain or triggers killed B, e.g. g10 Electrostatic Field, g22 Butcher of Malakir, g45 Niv-Mizzet, Parun).
- **Lethal source was a token in 26/41 losses.** Human Token 9 (g04, g06, g12, g14, g21, g28, g32, g38, g49), Angel Token 5 (g08, g18, g24, g40, g46), Spirit Token 3 (g16, g20, g30), Soldier Token 3 (g34, g48, g50), plus single Vampire/Human Wizard/Bird Illusion kills. Adeline's go-wide board is B's #1 killer.
- **Cumulative damage dealt to B across all 50 games** (from `Damage:` lines): tokens 1,469 in total (Human 517, Angel 384, Soldier 272, Human Wizard 63, Spirit 53, Vampire 43, other), D nontoken cards 631, A11 nontoken 383, C nontoken 180. D's burn (Guttersnipe lethal in g11, g29; Electrostatic Field g10, g44) is the second axis.
- Losing games aren't mana-screw games. B had ≥4 lands by its 4th turn in 36/41 losses (8/9 wins). Mulligans: B went to 6 only twice (g13, g47), and **won both**.
- Low card throughput is the losing pattern. B cast **28.0 spells per game in wins vs 17.3 in losses** (mean of logged casts). That fits B dying before its engine (Brago blinks, card draw) takes over.

## Why B won
- Its big ETB/flicker threats resolved. **Angel of Serenity** was cast in 8/9 wins (12/41 losses), Fact or Fiction in 7/9 (14/41), Venser 7/9 (12/41), **Path to Exile** 7/9 (6/41), Frost Titan 6/9, Agent of Treachery 6/9 (11/41), Restoration Angel 6/9 (8/41), Banishing Light 6/9, Mind Stone 6/9.
- Brago was cast in 48/50 games (all 9 wins). He usually stuck in wins: 1 cast in 4 wins and 3 in 3. In losses recasts climb: 3+ casts in 20 losses, up to 6. He keeps dying to removal/combat in losses.

## Key cards (cast in ≥6 of 9 wins)
Brago (9/9), Angel of Serenity (8/9), Fact or Fiction (7/9), Venser, Shaper Savant (7/9), Path to Exile (7/9), Frost Titan, Agent of Treachery, Restoration Angel, Banishing Light, Mind Stone, Frantic Search (6/9 each). Dream Trawler: 4 wins out of 7 games cast (n is tiny).

## Dead / underperforming cards
- **Never cast in 50 games (nonland):** Azorius Signet, Conjurer's Closet, Deputy of Detention, Ghostly Flicker, Mystic Confluence. Azorius Signet and Conjurer's Closet appear in `Discard: …-B discards` lines (5 logs mention the five cards in total). They were drawn and pitched, so the AI doesn't value them.
- **Cast but never in a win:** Man-o'-War (0W/16L), Mirrormade (0W/11L), Austere Command (0W/10L). Note: Austere Command was cast 10 times and still never in a win. Charming Prince 1W/13L, Flickerwisp 1W/15L, Cloudshift 2W/17L.
- Sweepers are cast a lot but don't convert to wins: Wrath of God 3W/15L, Supreme Verdict 1W/9L. Tokens keep coming back after the sweep (A11's token makers), and 26 lethal hits came from tokens.

## Mulligan / opening patterns
- B kept 7 in 48/50 games and mulled to 6 in g13 and g47 (won both). Mulligans weren't a cause of losses.
- Lands by B's 4th turn: 4 lands in 8/9 wins and 36/41 losses. 3 lands in 1 win and 4 losses. 2 lands in 1 loss. Land drops are not the separator.
- Going first: 4/9 wins (44%), compared with 5/41 when not first.

## Threat assessment (B's perspective)
1. **A11 Adeline tokens.** Won 20 of B's 41 losses, B died on A11's turn 20 times, and A11 tokens make up most of the 1,469 token damage. Wide boards outlast single sweepers.
2. **D Veyran spellslinger.** The largest nontoken damage to B (631). Guttersnipe and Electrostatic Field burn B out even through blockers (g10, g11, g29, g44).
3. **C Teysa aristocrats.** Drain kills on B's own turn (g09 Sorin, g22 Butcher, g35 Syr Konrad). Combat-based defence doesn't stop them.

## Swap proposals (max 2, one-for-one, NOT applied)
Rule v2.3 check: Bracket 2, no Game Changers, no 2-card infinites, total ≤ $100. Price is the lowest non-foil paper `prices.usd` in local Scryfall bulk `data/default.jsonl.gz` (2026-10-14), matching the ledger method. GC status comes from `sources/2026-10-14/game_changers.json` and Scryfall's `game_changer` flag.

1. **OUT Conjurer's Closet ($3.19) → IN Fumigate ($0.25, EOC #65; commander-legal; not a Game Changer).** Closet was never cast in 50 games and was discarded. Fumigate is a sweeper that gains 1 life per creature destroyed. Against A11's token boards (26/41 losses ended on token damage) it both clears the board and restores the life buffer that D's burn needs to break through. It creates no infinite combos with the list (no recursion loop).
2. **OUT Mystic Confluence ($0.49) → IN Settle the Wreckage ($0.41, HOB #26; commander-legal; not a Game Changer).** Confluence was never cast in 50 games (5 mana). Settle is an instant that exiles all attacking creatures, which answers the alpha strikes B died to on A11's turn (20/41) and doesn't feed C's death triggers (exile, not die). The opponent gets basic lands, a known drawback. It creates no infinite combos.
- **Price impact:** $83.50 − 3.19 + 0.25 − 0.49 + 0.41 = **$80.48**, under the $100 cap.
- **Bracket 2:** neither card is a Game Changer, an extra-turn card, MLD, or a tutor. Settle gives lands to opponents but isn't land destruction. In my judgment this stays Bracket 2, but Magnus/auditor should confirm.
- **Alternatives considered:** Man-o'-War or Mirrormade (0 wins when cast) instead of the never-cast cards. I held those back because they were at least castable and n is small.

## Gaps
- Batch 1 logs were not re-parsed (report figures only).
- The log Turn counter is 2× the report turn counter, and why is unexplained.
- Hand contents and draws aren't logged, so "dead" is based on casts/discards only. Non-damage life loss isn't attributed to a source.
