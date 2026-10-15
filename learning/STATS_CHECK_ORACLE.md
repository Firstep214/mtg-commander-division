# STATS_CHECK_ORACLE — CH001-LEARN-01 independent stats cross-check
Author: Oracle · 2026-10-15 (PHT). Independent; no other agent's check file was consulted.

## Method
- Script: `learning/oracle_check.py` → `learning/oracle_check.json` (new parser, analyst parsers not reused). Regexes over `forge/playtest_batch2/g01..g50.log`:
  `Game Result: ... Ai(n)-X has won` (winner), first `Turn: Turn 1 (Ai(n)-X)` (first player), `Game Outcome: Turn N` (report Turns), every `Turn: Turn N (...)` line (log counter), `Mulligan: ... mulliganed down to N`, `Game Outcome: ... has lost because`, `TimeoutException`.
- Parsed the PLAYTEST_BATCH2.md per-game table (50 rows) and compared per game. Batch 1: rg over `forge/playtest_batch1/rot*_g*.log` for winner, Outcome Turn, first player, Turn-line count.
- Spot-checked cited log lines with `sed -n`, and card cast/never-cast claims with `rg "Add To Stack: Ai(n)-<deck> cast <card>"`.
- Not re-derived (out of scope / time): per-card W/L splits, damage-by-source totals, spell-per-game means, lethal-source attributions, land-drop counts, prices.

## Confirmed
| Claim | Source | Claimed | Recounted | Citation |
|---|---|---|---|---|
| B2 wins A11/B/C/D | BATCH2, A/B/C/D | 20/9/12/9 | 20/9/12/9 (sum 50) | `Game Result` line of each log, e.g. g05.log:1757 (A11) |
| Per-game winner, first player, Turns column | BATCH2 table | 50 rows | 0 mismatches in 50 | first `Turn: Turn 1` line, e.g. g05.log:54; `Game Outcome: Turn` g05.log:1750 |
| Went first A11/B/C/D | BATCH2 | 12/9/15/14 | 12/9/15/14 | Turn 1 lines |
| Wins when first | BATCH2, A, B, C, D | 8/4/6/4 | 8/4/6/4; first player won 22/50 | — |
| Not-first records | A, B, C, D | A 12/38, B 5/41, C 6/35, D 5/36 | same | — |
| A's first-seat W/L game list | A §1 | g05,g18,g21,g24,g28,g38,g49,g50 W; g31,g33,g39,g44 L | same | — |
| Winners of a deck's losses | A, B, C | A: C12 B9 D9; B: A20 C12 D9; C: A20 B9 D9 | same | — |
| Report Turns mean/min/max | BATCH2 | 28.2 / 17 / 47 | 28.24 / 17 (g40) / 47 (g16) | g40.log:1204, g16.log:3190 |
| B win turns list (24–36) | B | g42/g47 24 … g13 36 | same | Outcome lines |
| D win turns (table) | D §2 | g10 40, g15 28, … g45 34 | same | g10.log:3163 |
| AI TimeoutExceptions | BATCH2 | 25 in 4 games (g18 2, g28 12, g43 1, g44 10) | same | — |
| All eliminations "life total reached 0" | A §1 | all | 149/149 B2 loss lines | Game Outcome lines |
| B1 wins A11/B/C/D | BATCH1, A, B, C, D | 10/6/4/4 | 10/6/4/4 | rot logs `Game Result` |
| B1 first player won | BATCH1 | 4/24 | 4/24 (rot2_g6, rot3_g3, rot3_g6, rot4_g2) | Turn 1 lines |
| A11 mulligan (any) | A §6 | B2 13 games/4 W; B1 3 games/0 W; 16/74 | 13/4; 3 games in B1 | `Mulligan:` lines |
| A11 to 6 cards | A §6 | 4 games (B1 2, B2 g03,g10), all L | B1 rot2_g6, rot4_g3; B2 g03, g10; all losses | — |
| B mulligans | B | mulled to 6 only g13, g47, won both | same (B also took the free 7-card mulligan in 9 games total, 2 W) | g13/g47 Mulligan lines |
| C mulligans | C §6 | 10 games, won 2 (g09,g14); g15 only double | same | — |
| Commander cast | A, B, C, D | Adeline 74/74, Brago 48/50, Teysa 48/50, Veyran 50/50 | same | cast lines |
| Never-cast lists | A, B, C, D | A: Sunfall, Mirror Entity, Unbreakable Formation; B: 5 cards; C: 5 cards; D: 4 cards | 0 cast lines for all 17 | rg over both batches |
| A cited lines | A §2/§3 | g05:1666/1701, g40:1148/1152, g02:1345 | content matches | g05.log:1666 "A11 cast Increasing Devotion" etc. |
| Turn counter 2× | A §9, B | ~2× / exactly 2× (g16: 94 lines vs 47) | see finding; g16 94 vs 47 confirmed | g16.log |

## Disputed
| Claim | Source | Claimed | Recounted | Citation |
|---|---|---|---|---|
| D mulligans | D §6 | "1 in 50 (g43)" | D took a mulligan in 8 games (g05,g15,g26,g29,g32,g38,g43,g46; 2 wins: g15,g29); only g43 went to 6. Claim true only if free 7→7 mulligan is excluded; wording should say "only 1 mulligan to 6" | `Mulligan: ... D has mulliganed down to 7` lines in those logs |
| "Turns" = all players' turns summed, ≈7 rounds | BATCH1 & BATCH2 | mean 28.2 ≈ 7 rounds | Outcome Turn is ~half the player-turn count; mean player turns ≈ 56 ≈ 14 rounds of 4 (fewer as players die) | g05.log:54,72,87 (Turn 1 A11, 2 B, 3 C) vs g05.log:1694 Turn 56 / 1750 Outcome 28 |
| Blasphemous Act citation | D §4 | g10 "T37", log lines 452–456 | Cast is at g10.log:924 (damage 929+), during log Turn 37 (g10.log:917). Lines 452–456 are C casting Teysa. Also D mixes units: table uses report turns (g10 T40), text uses log turns (T37) | g10.log:917,924,929 |
| "Exactly 2×" | B | exactly 2× | 27/50 exactly 2×; 23/50 are 2N−1 (ratio 1.95–2.0, mean 1.982) | e.g. g01 last Turn 51 vs Outcome 26 |

## Turn-counter finding
- In every B2 log, `Turn: Turn N` lines are strictly sequential 1..N with no gaps or duplicates, and each line names a different active player (never the same player twice in a row). So the log counter increments once per player turn (= the true number of turns taken).
- `Game Outcome: Turn` = ceil(last log turn / 2) in 50/50 games (e.g. g05: 56→28, g01: 51→26). Ratio min 1.952, max 2.000, mean 1.982. Batch 1 shows the same (rot1_g1 51→26, rot4_g3 86→43).
- So the batch reports' "Turns" are NOT "all players' turns summed"; they are half of that. Most likely Forge's Outcome counter is a separate value that counts 2 player turns per step (an internal Forge quirk, not confirmed from source). Practical rule: real player turns ≈ 2 × report Turns; rounds ≈ 2 × Turns / players alive. Any "turn N" in the analyses must say which counter: A/B/C use own-turn counts or report Turns; D's text uses log turns (T37, T23, T33) and its table uses report turns.

## Open issues
- Per-card W/L splits, damage totals, lethal-source and elimination-order claims were not re-derived (B and A use Life/Damage lines; C notes elimination order can't be read from `has lost` lines, which are all printed at game end).
- Why Forge halves the Outcome turn is unexplained; checking Forge source (`GameOutcome` / `PhaseHandler.getTurn`) would settle it.
- Batch 2 "Turns" column and summary text should be relabeled (or doubled) before turn-based stats are used.
