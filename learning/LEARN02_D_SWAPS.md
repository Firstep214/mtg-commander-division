# LEARN02 — Deck D swap proposals (CH001-LEARN-02)
Author: Thorne (MTG-13) · 2026-10-15 ~8:40 AM PHT · Base: decks/D_spellslinger_V1.1.txt (NOT modified; no ledger touched). Proposal only; Arbiter/Nemesis must verify before a V1.2 file is saved (PLAYTEST_RULES.md swap rule).
Inputs: forge/PLAYTEST_BATCH4.md, learning/batch4/B4_NOTES.md, learning/batch4/B4_CARD_STATS.txt, learning/D_ANALYSIS.md (Batch 2), learning/SWAP_VERIFICATION.md, PLAYTEST_RULES.md, CURRICULUM.md, decks/PRICE_LEDGER_D_spellslinger.md.

## Context (B4)
D11 won 27/200 (13.5%, CI 9.4–18.9). A12 won 94 (47%) and is the main problem for everyone (BATCH4.md). D's B2 losses: A11 dealt the last hit in 20/41 (D_ANALYSIS §3).

## Swaps (2, one-for-one)
| # | OUT → IN | Price OUT → IN (ledger / strict retail) | Reason |
|---|---|---|---|
| 1 | Faithless Looting → Mulldrifter | 0.37 LCC#225 / 0.37 → 0.28 MMA#54 / 0.28 | Faithless Looting was never cast in B4 (0/200, B4_CARD_STATS "never cast") or B2 (0/50, D_ANALYSIS §5; only discards seen: g17, g19, g35). Card draw is what D wins with when cast: Fact or Fiction 16/57 (28.1%), Sublime Epiphany 16/67 (23.9%) vs base 13.5%. Mulldrifter is plain draw-2 (or a 2/2 flyer for 5) that the Forge AI is expected to play; correlation only. |
| 2 | Blasphemous Act → Aetherize | 0.76 FDC#140 / 0.76 → 0.30 FDC#59 / 0.30 | Blasphemous Act is D's lowest-win card when cast: 4/42 (9.5%) vs base 13.5% (B4_CARD_STATS); B2 2/12 (D_ANALYSIS §2/4 table). It also kills D's own engine (pingers like Kessig/Electrostatic Field/Guttersnipe that won B2 games). Aetherize (instant, returns all attackers to owners' hands, so tokens disappear) is one-sided against A's go-wide attacks and does not touch D's board. Correlation only; long games inflate late cards. |

Not cut, on purpose:
- Izzet Signet (0/200 cast in B4, 0 in B2): Magnus' order is to wait for Vector's Signet quirk check.
- Sol Ring 6/58 (10.3%), Talrand 6/54 (11.1%), Third Path Iconoclast 6/51 (11.8%): below base, but these are cheap mana or spell payoffs. I see no causal story, so the correlation alone isn't enough to cut them.

## Earlier swaps (LEARN-01), both already in V1.1
- Mizzix's Mastery → Fiery Cannonade: **kept.** B4 9/51 (17.6%), above base 13.5%. Caveat: kills own small creatures.
- Past in Flames → Coruscation Mage: **kept.** B4 13/57 (22.8%).

## Rule checks
- Commander-legal, game_changer=false (Scryfall snapshot 2026-10-14); not in sources/2026-10-14/game_changers.json or banlist.json.
- 2-card infinites, checked against the full V1.1 list: Mulldrifter's ETB draw would need a repeatable flicker or recursion, and D has no blink effect or Past in Flames (cut in V1.1). Aetherize is a one-shot bounce with no untap or recursion engine in D; Reverberate/Galvanic Iteration/Increasing Vengeance copies are finite. No new loop.
- Bracket 2: no tutors, extra turns or MLD added.
- Price method = arbiter_swap/verify.py: ledger = min non-foil paper USD; strict = same, excluding PLST/promo/memorabilia. Both cards come from regular sets, so ledger = strict.

## Totals (computed over all 100 cards of V1.1 with the method above)
| | Ledger | Strict retail |
|---|---|---|
| V1.1 (current) | $76.76 | $79.69 |
| Proposed V1.2 | **$76.21** | **$79.14** |
Under the $100 target, so no over-$100 ledger line is needed. Check: 79.69 − 0.37 − 0.76 + 0.28 + 0.30 = 79.14.

## Data gaps
- B4_CARD_STATS lists "Fire // Ice" as never cast, but "Fire" is cast in 71 games; this is a split-card naming artifact, not a dead card.
- D's "rarely cast" list includes A's cards (e.g. Austere Command 1/1, Path to Exile 0/1). These are probably cast via copy/steal effects or are a parser attribution quirk; I didn't check them.
- There's no B4 data for Mulldrifter or Aetherize in D, and Forge AI handling of Aetherize (an instant cast during combat) is untested. These swaps need a Batch 5 run.
- Win% when cast is correlation only (B4_NOTES caveat). I did not count B4 damage sources or killers per game.
