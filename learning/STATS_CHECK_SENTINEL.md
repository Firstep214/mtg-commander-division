# STATS_CHECK_SENTINEL: independent cross-check of Batch 2 stats (CH001-LEARN-01)
Author: Sentinel · 2026-10-15 (PHT) · No other files modified.

## Confirmed
- **Batch 2 wins: A11 20, B 9, C 12, D 9 (total 50).** Each winner was taken from the `Game Result: ... Ai(n)-X has won!` line. The per-game table is below; every winner also matches the `Game Outcome: ... has won` line.
  - A11: g01 g04 g05 g06 g08 g11 g12 g18 g21 g24 g28 g30 g32 g34 g38 g40 g46 g48 g49 g50
  - B: g02 g03 g07 g13 g25 g33 g41 g42 g47
  - C: g09 g14 g16 g20 g22 g23 g26 g27 g31 g35 g37 g43
  - D: g10 g15 g17 g19 g29 g36 g39 g44 g45
- Win % in BATCH2.md (40/18/24/18) follows from these counts.
- The winner column in BATCH2.md's per-game table matches the logs in 50/50 games.
- "Forge Turn 1" column (first `Turn: Turn 1` line) matches in 50/50 games. Went first: A11 12, B 9, C 15, D 14. Wins when first: A11 8, B 4, C 6, D 4. First player won 22/50.
- The "Turns" column equals `Game Outcome: Turn N` in 50/50 games. Mean 28.24, min 17 (g40), max 47 (g16). These match the report's 28.2 / 17 / 47 as numbers, but see the label problem below.
- Wall times (`ended in N ms`) match to ±1 s rounding in 50/50 games.
- AI `TimeoutException` lines: 25 in total, in 4 games (g18 2, g28 12, g43 1, g44 10). This matches the report.
- 0 draws, 0 timeouts: all 50 logs have a Game Result line with a winner.
- A_ANALYSIS: A11 went first 12 times and won 8 (g05 g18 g21 g24 g28 g38 g49 g50). A11 mulliganed in 13 B2 games and won 4 of them (g18 g21 g38 g46). A11 went to 6 cards in g03 and g10. Adeline was cast in 50/50 B2 games.
- B_ANALYSIS: 9 wins and the game list are correct. Went first 9 times and won 4. Mulled to 6 only in g13 and g47 (kept 7 in 48/50). Brago was cast in 48/50 games.
- C_ANALYSIS: 12 wins and the game list are correct. 6/15 wins when first. C took a mulligan in 10 games (g09 g14 g15 g28 g30 g32 g33 g41 g46 g47) and won 2 (g09 g14). Teysa was cast in 48/50 games.
- D_ANALYSIS: 9 wins and the game list are correct. 14 times first, 4 wins. Veyran was cast in 50/50 games. D's only mulligan to 6 was g43 (g43.log:91-94).
- Winners of each deck's losses (A: C12 B9 D9 in B2; B: A20 C12 D9; C: A20 B9 D9; D: A20 B9 C12) follow directly from the winner list.

## Disputed
| Claim | Source | Actual (logs) | Citation |
|---|---|---|---|
| "Turns (Forge global counter, all players' turns summed): mean 28.2 (about 7 rounds)" | PLAYTEST_BATCH2.md | The figure is `Game Outcome: Turn N`, not the global counter. The global counter (`Turn: Turn N`, one per player-turn) has mean 56.0, min 34, max 94. That is about 14 rounds of 4 players, not about 7. | e.g. g16.log: last `Turn: Turn 94`, l.3190 `Game Outcome: Turn 47` |
| Same label in Batch 1: "global turn counter ... Mean 26.0 (≈6.5 rounds)" | PLAYTEST_BATCH1.md | Probably the same mislabel. I did not re-parse the rot logs, so this is unverified. | n/a |
| "Turn = Forge global counter" while quoting (T40), (T28) etc. per win | D_ANALYSIS §2 | Those T values are the Outcome values (half the global counter). Other D figures, e.g. "g40 ... T23", exceed g40's Outcome Turn 17 (global last = 34), so they use the real log counter. D mixes the two scales. | g40.log l.1204 `Game Outcome: Turn 17` |
| "g15 was the only double mulligan" | C_ANALYSIS §6 | This is true only for C (g15.log:43,47,48). Deck-wide, players went to 6 in g03 (A11), g10 (A11), g13 (B), g15 (C), g43 (D) and g47 (B). | g03.log:15-19, g43.log:91-94 |
| "B report turn ... (g42/g47 24, ...)" | B_ANALYSIS | Confirmed as Outcome values. B says the log counter is "exactly 2x". It is exactly 2x in 27 games and 2x−1 in 23 (see below). | per-game table |

Not verified (out of scope or needs each analyst's own parser): card-level cast/damage/trigger tallies (for example A's "Veyran 260", B's "1,469 token damage", C's trigger counts, D's damage-source table), land-drop counts and price math.

## Turn-counter finding
- `Turn: Turn N (Ai(n)-X)` lines are a **global counter of individual player-turns**. In all 50 logs it runs 1,2,3,... with no gaps, and it rotates through the seats (g01: Turn 1 B, 2 C, 3 D, 4 A11, ...). It is not a per-player counter.
- `Game Outcome: Turn N` (the value in the reports' Turns column) equals **ceil(last global turn / 2) in 50/50 games**. The ratio is exactly 2.000 in 27 games and 1.952-1.971 in the other 23 (odd global counts, e.g. g01 51 → 26). So "~2x" is correct, and the precise rule is global = 2·Outcome or 2·Outcome−1.
- It is neither rounds (that would be about global/4) nor the winner's own turn count (it never matched the max per-player turn count in any game; e.g. g16's busiest player had 25 turns, Outcome said 47). Forge's Outcome turn appears to count half of the global per-player turn counter. The cause is internal to Forge and not visible in the logs. Practical consequence: the "Turns" figures are about 2x rounds, and both batch reports' "(global counter, ≈N rounds)" labels are wrong.

| Game | Winner | Winner line | First (line) | Outcome Turn (line) | Last global Turn | Ratio |
|---|---|---|---|---|---|---|
| g01 | A11 | g01.log:1625 | B (l.21) | 26 (l.1618) | 51 | 1.962 |
| g02 | B | g02.log:2037 | B (l.53) | 30 (l.2030) | 60 | 2.000 |
| g03 | B | g03.log:2083 | C (l.21) | 32 (l.2076) | 64 | 2.000 |
| g04 | A11 | g04.log:1554 | D (l.49) | 24 (l.1547) | 47 | 1.958 |
| g05 | A11 | g05.log:1757 | A11 (l.54) | 28 (l.1750) | 56 | 2.000 |
| g06 | A11 | g06.log:1918 | C (l.49) | 28 (l.1911) | 56 | 2.000 |
| g07 | B | g07.log:1848 | B (l.58) | 27 (l.1841) | 54 | 2.000 |
| g08 | A11 | g08.log:1813 | C (l.52) | 26 (l.1806) | 52 | 2.000 |
| g09 | C | g09.log:2365 | D (l.58) | 37 (l.2358) | 74 | 2.000 |
| g10 | D | g10.log:3170 | D (l.56) | 40 (l.3163) | 80 | 2.000 |
| g11 | A11 | g11.log:1292 | D (l.42) | 19 (l.1285) | 38 | 2.000 |
| g12 | A11 | g12.log:1742 | B (l.48) | 27 (l.1735) | 53 | 1.963 |
| g13 | B | g13.log:2608 | D (l.93) | 36 (l.2601) | 72 | 2.000 |
| g14 | C | g14.log:1868 | D (l.49) | 26 (l.1861) | 51 | 1.962 |
| g15 | D | g15.log:1770 | C (l.52) | 28 (l.1763) | 55 | 1.964 |
| g16 | C | g16.log:3197 | D (l.101) | 47 (l.3190) | 94 | 2.000 |
| g17 | D | g17.log:1263 | B (l.44) | 21 (l.1256) | 42 | 2.000 |
| g18 | A11 | g18.log:2057 | A11 (l.153) | 31 (l.2050) | 62 | 2.000 |
| g19 | D | g19.log:1566 | D (l.47) | 22 (l.1559) | 43 | 1.955 |
| g20 | C | g20.log:2720 | C (l.58) | 40 (l.2713) | 80 | 2.000 |
| g21 | A11 | g21.log:1759 | A11 (l.45) | 26 (l.1752) | 51 | 1.962 |
| g22 | C | g22.log:1258 | C (l.48) | 21 (l.1251) | 41 | 1.952 |
| g23 | C | g23.log:1829 | C (l.44) | 31 (l.1822) | 62 | 2.000 |
| g24 | A11 | g24.log:1902 | A11 (l.54) | 30 (l.1895) | 60 | 2.000 |
| g25 | B | g25.log:1926 | B (l.59) | 29 (l.1919) | 57 | 1.966 |
| g26 | C | g26.log:2579 | C (l.61) | 32 (l.2572) | 63 | 1.969 |
| g27 | C | g27.log:1662 | C (l.48) | 22 (l.1655) | 44 | 2.000 |
| g28 | A11 | g28.log:3527 | A11 (l.744) | 40 (l.3520) | 80 | 2.000 |
| g29 | D | g29.log:1345 | C (l.43) | 21 (l.1338) | 41 | 1.952 |
| g30 | A11 | g30.log:2258 | D (l.53) | 34 (l.2251) | 68 | 2.000 |
| g31 | C | g31.log:1781 | A11 (l.53) | 24 (l.1774) | 47 | 1.958 |
| g32 | A11 | g32.log:2028 | C (l.52) | 28 (l.2021) | 56 | 2.000 |
| g33 | B | g33.log:2313 | A11 (l.263) | 34 (l.2306) | 67 | 1.971 |
| g34 | A11 | g34.log:2137 | D (l.48) | 29 (l.2130) | 58 | 2.000 |
| g35 | C | g35.log:1808 | D (l.57) | 23 (l.1801) | 45 | 1.957 |
| g36 | D | g36.log:1851 | D (l.52) | 27 (l.1844) | 54 | 2.000 |
| g37 | C | g37.log:1867 | B (l.50) | 31 (l.1860) | 61 | 1.968 |
| g38 | A11 | g38.log:2302 | A11 (l.58) | 32 (l.2295) | 64 | 2.000 |
| g39 | D | g39.log:1233 | A11 (l.44) | 21 (l.1226) | 41 | 1.952 |
| g40 | A11 | g40.log:1211 | C (l.46) | 17 (l.1204) | 34 | 2.000 |
| g41 | B | g41.log:2134 | D (l.61) | 33 (l.2127) | 65 | 1.970 |
| g42 | B | g42.log:1550 | C (l.47) | 24 (l.1543) | 48 | 2.000 |
| g43 | C | g43.log:1847 | C (l.97) | 24 (l.1840) | 48 | 2.000 |
| g44 | D | g44.log:2676 | A11 (l.543) | 23 (l.2669) | 45 | 1.957 |
| g45 | D | g45.log:2480 | D (l.68) | 34 (l.2473) | 67 | 1.971 |
| g46 | A11 | g46.log:2333 | C (l.54) | 33 (l.2326) | 65 | 1.970 |
| g47 | B | g47.log:1533 | B (l.56) | 24 (l.1526) | 47 | 1.958 |
| g48 | A11 | g48.log:1364 | B (l.46) | 23 (l.1357) | 45 | 1.957 |
| g49 | A11 | g49.log:1229 | A11 (l.46) | 21 (l.1222) | 41 | 1.952 |
| g50 | A11 | g50.log:1614 | A11 (l.49) | 26 (l.1607) | 52 | 2.000 |

## Method
- Script /tmp/chk.py (box scratch). It applies regexes per log: `^Turn: Turn (\d+) \(Ai\(\d\)-(\w+)\)`, `Game Outcome: Turn (\d+)`, `Game Result: .* ended in (\d+) ms\. Ai\(\d\)-(\w+) has won`, `TimeoutException`, `Mulligan: ... has mulliganed down to N`. The script parsed the BATCH2.md per-game table and compared it field by field.
- "mulliganed down to 7" is Commander's free mulligan; a "mulligan to 6" means a `kept a hand of 6` line.
- Cast checks used `rg -l "Add To Stack: Ai\(\d\)-<deck> cast <commander>"`.
- Batch 1 logs were not re-parsed.
