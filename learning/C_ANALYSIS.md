# Deck C (Teysa Karlov aristocrats, V1): Batch Analysis (CH001-LEARN-01)
Author: Vex (playtester, Deck C) · 2026-10-15 (Asia/Manila)
Sources: forge/PLAYTEST_BATCH1.md, forge/PLAYTEST_BATCH2.md, forge/playtest_batch2/g01-g50.log, PLAYTEST_RULES.md, decks/C_aristocrats.txt, decks/PRICE_LEDGER_C_aristocrats.md, sources/2026-10-14/{game_changers,banlist}.json, data/default.jsonl.gz (byte-identical to the 2026-10-14 Scryfall snapshot).
Parser: /workspace/c_parse.py → /workspace/c_parsed.json (reruns reproduce every number below). Deck file NOT modified.

Caveat: Forge AI pilots. Batch 2 is 50 games (about ±14 pp per deck, per BATCH2.md). The card-level splits below are tiny samples (n ≤ 21). Read them as hints, not verdicts.

## 1. Results
- Batch 1 (summary table only; I did not re-parse the rot logs): C won 4/24 (rot1_g3, rot2_g4, rot2_g5, rot2_g6).
- Batch 2: C won **12/50** (g09 g14 g16 g20 g22 g23 g26 g27 g31 g35 g37 g43).
  - When C went first: 6/15 wins (g20 g22 g23 g26 g27 g43). When C did not go first: 6/35.
  - Winners of C's 38 losses: A11 20, B 9, D 9.
- C's own turns per game: mean 16.8 in wins and 13.7 in losses. C cast a mean of 22.9 spells in wins and 15.6 in losses. The deck wins when the game goes long enough for the drain engine to come online.

## 2. Why it won (log evidence)
In all 12 wins, the final life loss came from C's death-trigger or drain engine. These are the last resolve/damage lines before `Game Outcome`:
- Falkenrath Noble + Cruel Celebrant drain: g09 (C turn 22; a chain of Zulaport/Celebrant/Noble triggers took B from 3 to 0).
- Zulaport Cutthroat: g14, g43.
- Vindictive Vampire: g20, g31, g37.
- Syr Konrad: g27.
- Ministrant of Obligation sac chain (Spirit tokens dying): g35.
- Spirit token and Nadier's Nightblade attacks to finish D: g16, g23, g26.
- g22: B's last life loss came from B's own Brago-side "whenever a player casts a spell, they lose 2 life" effect after Brainstorm, so the kill was partly self-inflicted by an opponent.
- Trigger volume across all 50 logs (C-controlled `triggered` lines, total / games): Elenda 245/10, Bastion of Remembrance 115/12, Dark Prophecy 108/8, Liesa 103/10, Yahenni 101/11, Zulaport 101/13, Falkenrath Noble 84/8, Elas il-Kor 81/9, Syr Konrad 62/8, Pitiless Plunderer 60/10, Vindictive Vampire 53/8.

## 3. Why it lost
- **Go-wide combat from A11 (20/38 losses).** In most A11 wins, the lethal damage lines into C are Human Tokens (Adeline) plus Soldier/Angel/Servo tokens: g01 g04 g05 g06 g08 g11 g12 g18 g21 g28 g30 g32 g34 g38 g40 g46 g48 g49 g50. In g05, g06 and g08, single tokens dealt 18-26 combat damage. The deck has no repeatable answer to a wide board of pumped tokens.
- **Flyers/tempo from B (9 losses):** Brago, Restoration Angel, Dream Trawler, Glen Elendra, Venser and Agent of Treachery deal the final damage in g03 g07 g13 g25 g33 g41 g42 g47. In g25, B's Agent of Treachery had stolen C's Carrion Feeder, which then appears among the lethal sources.
- **Burn/reach from D (9 losses):** C died at 1 life to Niv-Mizzet (g10), Thermo-Alchemist (g36) and Kessig Flamebreather (g44), and at 14 to Haughty Djinn (g19).
- **Self-inflicted:** in g45, C went from 2 to 1 to 0 on its own Dark Prophecy triggers (lines: `triggered Dark Prophecy`, `Ai(1)-C 2 > 1`). Dark Prophecy is a real liability when C's life is low.
- **Fast losses with little development:** g17 and g29 (7 C turns each; 6 and 7 spells cast; Teysa never cast in g29), and g04 (only 2 lands by C turn 4, 6 spells cast, no Teysa).

## 4. Key cards (games cast / C wins in those games; base rate is 12/50)
- Teysa Karlov: cast in 48/50 games, 12 wins (all 12 wins had her). First cast on C turn: mean 6.33 / median 6 in wins (n=12), mean 5.17 / median 5 in losses (n=36). Casting her early does not by itself predict a win.
- Higher than base rate (small n): Utter End 7/10, Victimize 5/7, Path to Exile 7/16, Kaya's Guile 8/21, Ashnod's Altar 6/12, Syr Konrad 6/13, Midnight Reaper 6/12, Dark Prophecy 6/11, Vindictive Vampire 5/10, Spectral Procession 5/9, Liesa 5/10, Elenda 5/11, Zulaport 6/16, Nadier's Nightblade 6/16, Ministrant of Obligation 6/14, Return to the Ranks 6/17.
- Drain payoffs that delivered the final blow (section 2): Zulaport, Vindictive Vampire, Falkenrath Noble, Cruel Celebrant, Syr Konrad.

## 5. Dead / low-impact cards
The logs do not record draws or hand contents. "0 casts" therefore means not drawn OR drawn and never cast; the two cannot be told apart.
- Never cast in 50 games: **Viscera Seer** (no log mention at all), **Undying Evil** (no mention), **Sevinne's Reclamation** (no mention), **Wake the Dead** (no mention), Orzhov Signet (only mention: milled in g20).
- Grim Haruspex: 0 normal casts, but it was played face-down via morph and later unmorphed (g14 `has unmorphed Grim Haruspex`). It triggered 18 times in 5 games, so it is not dead.
- Weak (small n): Commander's Sphere 1/11, Deadly Dispute 1/10, Darkest Hour 1/11, Blood Artist 1/6, Mirkwood Bats 1/5, Village Rites 1/5, Priest of Forgotten Gods 1/7.
- Lands: excluded. The parser tracks casts, not land plays.

## 6. Mulligan / opening patterns
- The logs record mulligan decisions but not hand contents.
- Every `mulliganed down to 7` line is Commander's free mulligan. C took at least one mulligan in 10/50 games (g09 g14 g15 g28 g30 g32 g33 g41 g46 g47) and won 2 of them (g09, g14). C won 10 of the 40 games with no mulligan.
- g15 was the only double mulligan; D won it.
- Lands: 45/50 games had ≥4 C land drops by C turn 4. The 5 that did not: g01 (3, lost), g04 (2, lost), g16 (2, won), g20 (3, won), g26 (3, won). Mana screw is not the main failure mode.

## 7. Threat assessment
1. **A11 Adeline tokens.** C's biggest problem: 20 of 38 losses, plus overwhelming lethal combat turns (g05, g06, g08). Spot removal (Swords, Path, Infernal Grasp) does not stop an already-wide board, and Damn/Kaya's Guile are the only sweep-ish tools.
2. **B Brago.** Flyers plus flicker. Agent of Treachery steals C's pieces (g25).
3. **D Veyran.** Incidental pings finish C at low life (g10, g36, g44). Combined with C's own life payments (Dark Prophecy in g45), this argues for keeping a higher life buffer.

## 8. Swap proposals (max 2, one-for-one, NOT applied)
Prices: ledger rule (cheapest non-foil paper USD), from the local 2026-10-14 Scryfall snapshot. Commander legality: `legal`. `game_changer`: false. Neither card is in game_changers.json or banlist.json.
1. **Wake the Dead ($1.37) → Massacre Wurm ($2.63, FDN #754).** Wake the Dead was never cast in 50 games. Massacre Wurm answers the A11 token boards that caused 20 losses, since -2/-2 kills 1/1 tokens not yet pumped by Adeline/anthems. Each opposing creature that dies costs its controller 2 life, which fits the drain plan. There is no 2-card infinite with it.
2. **Sevinne's Reclamation ($0.45) → Pestilence ($0.30, 4ED #152).** Sevinne's was never cast in 50 games. Pestilence is a repeatable, scalable sweeper against small tokens and pings opponents directly as reach. That reach is the kind that closed g09/g14/g43, and it also gets around the life-gain loops of A11/B. There is no 2-card infinite: it needs repeated mana. Caveat: it also kills C's own small creatures. That feeds death triggers, but the AI may misuse it.
- Price math: $85.97 − 1.37 + 2.63 − 0.45 + 0.30 = **$87.08** (under the $100 cap, margin $12.92).
- Bracket 2: both cards are fair, mana-gated board answers; neither adds tutors, extra turns, MLD or fast mana.

## 9. Data gaps
- No draw or hand data in the logs. Dead-card and opening-hand analysis is limited to casts and mulligan counts.
- The parser counts only cast spells, so cards that hit the battlefield another way (morph, reanimation, Living Death) are undercounted by cast. Trigger counts partly cover this.
- Elimination order cannot be measured: all `has lost` lines are printed together at game end.
- Token owners are inferred from the cards that make them (e.g. Human Token → Adeline/A11); the log does not tag damage sources with a controller.
- I used Batch 1 per-game C data from PLAYTEST_BATCH1.md only (rot logs not re-parsed). 25 AI TimeoutExceptions (g18 g28 g43 g44) slightly degrade AI play in those games.

## Swaps applied 2026-10-15
Approved by Voltaire. Applied in place to `decks/C_aristocrats.txt`. Backup: `decks/C_aristocrats.txt.bak-20261015`.
- Wake the Dead ($1.37, CMM #197) → Massacre Wurm ($2.63, FDN #754)
- Sevinne's Reclamation ($0.45, SOC #170) → Pestilence ($0.30, 4ED #152)
- Recheck against the 2026-10-14 Scryfall snapshot, using the price_decks.py method (cheapest non-foil paper USD per card): 100 cards, total **$87.08** (≤ $100). No banned or Game Changer cards; all cards are commander-legal. Neither added card forms a 2-card infinite, so the deck stays Bracket 2.
- The edited file is identical to the existing `decks/C_aristocrats_V1.1.txt`. `forge/decks/C.dck` and `PRICE_LEDGER_C_aristocrats.md` / `C_aristocrats.md` were not updated.
