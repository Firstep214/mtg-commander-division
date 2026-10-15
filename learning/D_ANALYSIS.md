# Deck D (Veyran spellslinger, V1) — Playtest Analysis (CH001-LEARN-01)
Author: Thorne (MTG-13). Written 2026-10-15 (PHT). Deck file NOT modified.
Sources: forge/PLAYTEST_BATCH1.md, forge/PLAYTEST_BATCH2.md, forge/playtest_batch2/g01–g50.log, PLAYTEST_RULES.md, decks/D_spellslinger.txt, decks/PRICE_LEDGER_D_spellslinger.md, data/default.jsonl.gz + data/oracle.jsonl.gz (Scryfall snapshot 2026-10-14).
Method: every number below comes from `learning/d_parse.py` (output `learning/d_parsed.json`) or `rg` over the Batch 2 logs.
**Turn scale (used everywhere in this file): "log Turn N"** = the `Turn: Turn N` line in the log, which goes up by one for each player turn (sequential 1..N in every log; Oracle check). For reference, BATCH2.md's "Turns" column = `Game Outcome: Turn` = ceil(log Turn / 2) (Oracle: true in 50/50 games). With 4 players, one full table round is about 4 log Turns, so "log Turn 16" is about the end of round 4. Caveat: Forge AI pilots; 50 games ≈ ±14pp (BATCH2.md).

## 1. Results
- Batch 2: 9/50 wins (18%) — g10, g15, g17, g19, g29, g36, g39, g44, g45. Went first 14 times, won 4 of those (BATCH2.md table; parser agrees).
- Batch 1: 4/24 (17%) — rot1_g6, rot2_g1, rot3_g5, rot4_g2 (BATCH1.md; seat order not R1-compliant, so used only as corroboration).

## 2. Why D won — damage-per-spell engines, not Veyran beats
Top damage sources to opponents in each win (rg "Damage: X deals N … to Ai(n)-opp", last 60 hits):
| Game (final log Turn) | Top D damage sources |
|---|---|
| g10 (log Turn 80) | Niv-Mizzet, Parun 18 lines; Electrostatic Field 12+12; Firebrand Archer 8 |
| g15 (log Turn 55) | Haughty Djinn 4; Docent of Perfection 3; Veyran 2 |
| g17 (log Turn 42) | Thermo-Alchemist 9; Electrostatic Field 7 |
| g19 (log Turn 43) | Guttersnipe 31 (+4 second copy line) |
| g29 (log Turn 41) | Guttersnipe 24; Kessig Flamebreather 15; Electrostatic Field 4 |
| g36 (log Turn 54) | Kessig Flamebreather 33; Thermo-Alchemist 11 |
| g39 (log Turn 41) | Veyran 6; Niv-Mizzet 3; Murmuring Mystic 3 |
| g44 (log Turn 45) | Kessig Flamebreather 30; Electrostatic Field 30 |
| g45 (log Turn 67) | Guttersnipe 28; Niv-Mizzet 7 |
In 7/9 wins (g10, g17, g19, g29, g36, g44, g45) the top source was a "whenever you cast" pinger (Guttersnipe / Kessig / Electrostatic Field / Thermo-Alchemist / Niv-Mizzet / Firebrand Archer), which Veyran's magecraft doubling amplifies. Only g15 and g39 were won mainly by creature combat.
- Spell volume: mean D casts per game 31.3 in wins vs 20.1 in losses; lands played 10.6 vs 10.8 (so losses were not land-starved on average — the gap is spell density/engine online).
- Game-presence vs win rate (games where D cast the card, B2): Guttersnipe 5 games / 3 wins; Kessig Flamebreather 15/5; Electrostatic Field 14/5; Anger of the Gods 11/5; Storm of Saruman 11/5; Rapid Hybridization 12/5. Baseline is 9/50. Small samples — directional only.

## 3. Why D lost (41 losses)
- Killer of D (source of last damage D took): A11 20, B 11, C 9 (parser; g08's 34-dmg Jazal Goldmane hit and g28's 68-dmg Soldier Token show A11 pump alpha strikes).
- Go-wide tokens are the main killer: last hits by A11 Human/Soldier/Angel tokens in g05, g11, g12, g14, g18, g24, g28, g30, g32, g34, g40, g41, g46, g48, g49, g50.
- Fastest deaths: g40 (last damage to D at log Turn 23, from an A11 Angel Token; D took 6 turns and cast 6 spells), g49 (last damage at log Turn 33; 5 lands, 9 casts), g43 (D's only mulligan to 6; 5 lands; last damage at log Turn 33, from Zulaport Cutthroat).
- B kills via fliers/evasive value: Glen Elendra Archmage last hit in g01, g33, g47; Brago in g06, g37; Bird Illusion tokens g25, g42.
- In losses D usually never assembled a pinger; Guttersnipe was cast in only 2 of 41 losses (vs 3 of 9 wins).

## 4. Key cards
- Veyran, Voice of Duality: cast in 50/50 games. First cast, log Turn — wins: g10 17, g15 14, g17 32, g19 13, g29 10, g36 9, g39 12, g44 40, g45 17; losses mean 14.83. Veyran timing does not separate wins from losses; what matters is having a pinger next to it.
- Pinger package (Guttersnipe, Kessig Flamebreather, Electrostatic Field, Thermo-Alchemist, Firebrand Archer, Niv-Mizzet): the win condition (section 2).
- Sweepers vs A11: Anger of the Gods (5 of 11 cast-games won), Blasphemous Act (g10, log Turn 37 (g10.log:917): cast at g10.log:924 with two Veyran magecraft triggers on the next lines; damage from g10.log:929).
- Most-cast nonland cards: Reality Shift 26 games, Fire // Ice 24, Fact or Fiction 22, Expressive Iteration 21, Arcane Denial 21.

## 5. Dead cards (Batch 2)
Never cast in 50 games (parser cast counts = 0; rg confirms only appearances):
- Mizzix's Mastery — 0 casts; appears once (milled, g35). 4-mana sorcery needing a stocked graveyard; AI never used it.
- Past in Flames — 0 casts; appears in 10 logs, observed as discards (g02, g17, g19…).
- Faithless Looting — 0 casts; 8 logs, discarded (g17, g19, g35…). Forge AI seems not to value it.
- Izzet Signet — 0 casts; 5 logs, discarded (g04, g11, g49…). Anomalous given other rocks are cast 12–16 games; may be AI preference.
Low use: Reverberate 5 games (g01 shows "Couldn't add to stack, failed to target"), Increasing Vengeance 6, Ral, Storm Conduit 9, Consider 10 (0 in wins).

## 6. Mulligan / opening patterns
- Mulligans (corrected): D took a mulligan in **8/50** Batch 2 games: g05, g15, g26, g29, g32, g38, g43, g46 (`Mulligan: ... D has mulliganed down to 7` lines, e.g. g05.log:49, g15.log:44, g29.log:38). 7 of these were the free mulligan back to 7 cards; only **g43 went to 6** (g43.log:91–94). D won **2 of 8** mulligan games (g15, g29) and 7 of the other 42. Batch 1 (my parser): 0 hands below 7; free 7→7 mulligans were not checked there.
- Conclusion: a free mulligan did not visibly hurt D (2/8 is the same range as the 9/50 baseline; the samples are too small for anything more). The one trip to 6 (g43) lost. The keep/mulligan rate tells us little about deck quality because the Forge AI decides it.
- First spell (log Turn): every game by log Turn 15 at the latest. Wins: g10 5, g15 6, g17 11, g19 1, g29 6, g36 2, g39 5, g44 9, g45 13; losses mean 6.95.
- D spells cast by log Turn 16 (about the first 4 rounds): wins mean 3.22, losses 3.61. The opening does not separate wins from losses; what matters is assembling the damage engine mid-game.
- Going first did not help D: 4 wins in 14 first-seat games (29%) vs 5 in 36 otherwise.

## 7. Threat assessment
1. A11 (Adeline tokens): killed D in 20/41 losses; tokens + anthems/pump outrace a deck with few blockers. Biggest threat. Cheap sweepers are the answer.
2. B (Brago control): 11 kills, slow evasive value (Glen Elendra, Brago, Bird Illusions); counters slow D's engine.
3. C (Teysa aristocrats): 9 kills, often drain (Zulaport g43, Vindictive Vampire g31, Nadier's Nightblade g23/g26).

## 8. Swap proposals (max 2, one-for-one, NOT applied)
| # | Out | In | Reason (log evidence) |
|---|---|---|---|
| 1 | Mizzix's Mastery ($3.78 ledger) | Fiery Cannonade ($0.22, CMR #178) | Mastery: 0 casts/50. A11 tokens killed D in 20/41 losses; Anger of the Gods games won 5/11. Instant-speed 2-damage sweep kills 1/1 tokens. Note: also kills D's own Guttersnipe/Pyromancer/Archer (x/2 or less) — AI sequencing risk. |
| 2 | Past in Flames ($2.53 ledger) | Coruscation Mage ($2.40, BLB #131) | Past in Flames: 0 casts/50, only discarded. 7/9 wins were driven by "whenever you cast" pingers; Guttersnipe-in-play games 3/5 won. Mage is a 2-mana pinger with offspring for a second copy; adds redundancy to the real win-con. |
Compliance (rule v2.3): both commander-legal and game_changer=false in Scryfall snapshot 2026-10-14; neither in local game_changers list. Neither forms a 2-card infinite (fixed 1-shot / per-spell 1 damage, no untap or recursion loops). Bracket 2 fits (no tutors, no extra turns, no MLD). Price: ledger total $80.45 − 3.78 − 2.53 + 0.22 + 2.40 = **$76.76** (≤ $100). Prices = cheapest paper USD printing in data/default.jsonl.gz.

## 9. Data gaps
- Logs do not record draws or opening hands, so "drawn but uncastable" vs "never drawn" cannot be separated; dead-card list = never cast, plus observed discards.
- Elimination turn approximated by D's last damage taken; the "has lost" line is only printed at game end.
- Forge AI piloting (Past in Flames, Faithless Looting, Mizzix's Mastery, Reverberate) likely understates their value with a human pilot.
- Swaps are untested; would need a Batch 3 run.

## Changelog
- 2026-10-15 ~3:55 AM PHT (Thorne): applied the Oracle/Sentinel corrections. Mulligans are 8 games (not 1); only g43 went to 6. The Blasphemous Act citation is now g10.log:924 (log Turn 37). Every turn reference is converted to one labeled scale (log Turn), and the Veyran timing, first-spell and early-cast stats are recomputed. The swap proposals are unchanged.
