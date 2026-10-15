# LEARN03 — Deck D bold swap round (CH001-LEARN-03)
Author: Thorne (MTG-13) · 2026-10-15 ~1:00 PM PHT · Base: decks/D_spellslinger_V1.3.txt (100 cards; NOT modified; no ledger touched). Proposal only: Arbiter/Nemesis must verify before a V1.4 file is saved.
Inputs: forge/PLAYTEST_BATCH5.md, forge/playtest_batch5/g001–g200.log, learning/batch4/SIGNET_CHECK.md, PLAYTEST_RULES.md, CURRICULUM.md, LEARN02_D_SWAPS.md, D_ANALYSIS.md.
Parser: learning/d_b5_parse.py → learning/d_b5_parsed.json (mine, new). **Turn scale: "log Turn" = the `Turn: Turn N` line (one per player turn); a 4-player round ≈ 4 log Turns.**

## What changed since V1.1
V1.1 → V1.3: Izzet Signet → Worn Powerstone; Faithless Looting → Mulldrifter; Blasphemous Act → Aetherize (V1.2/V1.3 changelogs).
**Signet task:** Izzet Signet is already gone; V1.3 replaced it with Worn Powerstone, which the AI casts (D13 cast it 60 times in 58 games, BATCH5.md). Arcane Signet is already in the deck (V1.3 line 3), so singleton blocks adding it. No ramp swap is needed.

## How D13 lost in Batch 5 (19 W / 181 L)
- D's life hit ≤0 in 180 of 181 losses (g089: no such Life line found, so excluded).
- **Whose turn it was when D died:** A12 73, B13 52, C13 49, D13's own turn 6.
- **Last damage source before death:** A's tokens 64 (Human Token 46 overall across decks, Angel Token 11, Soldier Token 6), C13 cards 46, B13 cards 30, A12 nontoken cards 14. Token owner is inferred from whose turn it was (parser heuristic).
  - Example: g192, log Turn 25 (g192.log:668–674): A's Human Tokens hit for 7 and 3, then D goes `7 > -116`. This was D's earliest death.
  - Other early deaths: g196 log Turn 27 (Human Token, line 745), g066 log Turn 29 (Human Token, line 903), g128 log Turn 30 (Human Token, line 1039).
  - C's drain: Syr Konrad last hit in 9 games (e.g. g015:1369, g032:1264, g197:1366); Pestilence in 7 (e.g. g023:2080, g181:1323).
  - B: Brago last hit in 10 (e.g. g012:1356, g164:1181).
- **Death timing:** mean log Turn 48.2, median 45.5, range 25–103. 9 deaths came by log Turn 30 and 48 by log Turn 40.

## Engine density (B5)
Pingers counted: Guttersnipe, Kessig Flamebreather, Electrostatic Field, Firebrand Archer, Thermo-Alchemist, Coruscation Mage, Niv-Mizzet.
| Distinct pingers cast in game | D wins / games |
|---|---|
| 0 | 0 / 24 |
| 1 | 2 / 52 |
| 2 | 8 / 62 |
| 3+ | 9 / 62 |
Top D damage to opponents, summed over the 19 wins: Guttersnipe 378, Veyran 209, Electrostatic Field 184, Kessig Flamebreather 179, Niv-Mizzet 152, Haughty Djinn 131. Correlation only (longer games see more cards), but the pattern matches Batch 2 (D_ANALYSIS §2): D wins by spell-triggered damage.

## Underperformers (win% when cast, B5, ≥15 games; base 19/200 = 9.5%)
Coruscation Mage 2/51 (3.9%), Fiery Cannonade 2/39 (5.1%), Essence Scatter 3/54 (5.6%), Consider 2/34 (5.9%), Negate 5/63 (7.9%), Rapid Hybridization 4/46 (8.7%).
The two LEARN-02 adds look fine: Aetherize 5/42 (11.9%), Mulldrifter 7/60 (11.7%). Both are kept.

## Swaps (4, one-for-one)
| # | OUT → IN | Price OUT → IN (strict = ledger for all 8) | Reason |
|---|---|---|---|
| 1 | Coruscation Mage → **Fiery Inscription** | 2.40 BLB#131 → 0.46 LTR#126 | Mage won 2/51 (3.9%), the worst cast-win rate in D. Fiery Inscription is a Guttersnipe (D's top win-damage source) on an enchantment: 2 damage to each opponent per instant/sorcery, doubled by Veyran. As an enchantment it survives creature combat, A's/B's creature removal and D's own Anger of the Gods/Fiery Confluence. Adds engine density. |
| 2 | Fiery Cannonade → **Propaganda** | 0.22 CMR#178 → 1.93 FDC#72 | Cannonade won 2/39 (5.1%) and also kills D's own x/2 pingers (my LEARN-01 caveat). A's go-wide attacks are D's main killer (73 deaths on A's turn; 64 last hits by tokens). Propaganda taxes every attacker by {2}, which blunts token alpha strikes like g192 and Brago (B) attacks, and does not hurt D's board. |
| 3 | Essence Scatter → **Harmonic Prodigy** | 0.07 M14#55 → 5.07 MH2#352 | Scatter won 3/54 (5.6%). Prodigy makes every Shaman/Wizard trigger fire one extra time. D's Shamans and Wizards are Guttersnipe, Kessig Flamebreather, Thermo-Alchemist and Young Pyromancer, plus Veyran, Talrand, Murmuring Mystic, Archmage Emeritus, Stormcatch Mentor and Niv-Mizzet. That stacks with Veyran: Guttersnipe goes to 4 triggers per spell. This is the "strengthen the engine" piece. |
| 4 | Consider → **Fiery Confluence** | 0.35 TDC#148 → 0.32 SCD#141 | Consider won 2/34 (5.9%); cantrip redundancy is high (Opt, Ponder, Preordain, Brainstorm stay). Confluence is a modal answer and finisher: 1–3 damage to each creature clears A's 1/1 Human/Soldier tokens (the top last-hit source); 6 damage to each opponent closes games for a pinger deck; or it destroys an artifact. |

Kept, on purpose: Negate 5/63 and Rapid Hybridization 4/46. They are near the 9.5% base, and D needs some answers to Brago/C's enchantments (Pestilence). Revisit in the next round.

## Rule checks
- **Legality / Game Changers:** all 4 incoming cards are Commander-legal and game_changer=false (Scryfall snapshot 2026-10-14). None appears in sources/2026-10-14/game_changers.json or banlist.json. Singleton: none of the 4 is already in V1.3 (scripted check: no duplicates).
- **2-card infinites**, each incoming card checked against the full V1.3 list:
  - Fiery Inscription: a damage trigger only, with no mana, untap or recursion.
  - Propaganda: static tax.
  - Fiery Confluence: one-shot.
  - Harmonic Prodigy multiplies triggers, so every pairing was checked:
    - Thermo-Alchemist untaps only on cast, which is finite.
    - Storm-Kiln Artist is a Dwarf Shaman, so it makes 2 (3 with Veyran) Treasures per spell. That is still bounded by the number of spells cast, and nothing in D converts Treasures into a free recast. It is mana acceleration, not a loop.
    - Archmage Emeritus draws extra cards per spell (finite). With Niv-Mizzet, each draw pings. Bounded by cards in library, with no self-loop.
    - Talrand, Murmuring Mystic and Young Pyromancer make extra tokens (finite).

    No combination produces unbounded mana, casts or damage. **No 2-card infinite.**
- **Bracket 2:** no tutors, extra turns or MLD added. Note: Harmonic Prodigy + Veyran is a high-ceiling damage multiplier. It is legal, but Arbiter may want to judge it against the Bracket 2 "casual" spirit.
- **Price method** (as in arbiter_swap/verify.py / the ledger): ledger = min non-foil paper USD; strict = same, excluding PLST/promo/memorabilia. Snapshot 2026-10-14. All 8 cards are priced from regular sets, so ledger and strict are the same.

## Totals (computed over all 100 cards)
| | Ledger | Strict retail |
|---|---|---|
| V1.3 (current) | $76.18 | $79.11 |
| Proposed V1.4 | **$80.92** | **$83.85** |
Check: 79.11 − (2.40+0.22+0.07+0.35) + (0.46+1.93+5.07+0.32) = 83.85. Under the $100 target, so no ledger reason line is needed.

## Data gaps
- Killer attribution uses the last `Damage:` line before D's life hits ≤0. Life-loss effects without a Damage line (e.g. drain) may be credited to the previous damage source. Token owners are inferred from the active player.
- g089: D lost but no ≤0 Life line was found; not analysed.
- "Fire // Ice" win-rate in my parser is unreliable: prefix matching "Fire" also catches Firebrand Archer, so it is omitted above.
- Win% when cast is correlation only. None of the 4 incoming cards has sim data. Forge AI handling is unverified: whether it casts Propaganda, pays its tax correctly as an opponent, and picks good Fiery Confluence modes. Needs a Batch 6.
- Fiery Inscription's "the Ring tempts you" is irrelevant upside; Forge support for it is assumed, not checked in the cardsfolder.
