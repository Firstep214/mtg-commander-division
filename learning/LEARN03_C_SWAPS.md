# CH001-LEARN-03: Deck C (C_aristocrats_V1.3) swap proposals
Author: Vex (Deck C) · 2026-10-15 (Asia/Manila) · PROPOSAL ONLY. No deck file was edited.
Sources: forge/PLAYTEST_BATCH5.md; forge/playtest_batch5/g001–g200.log; learning/batch4/SIGNET_CHECK.md; PLAYTEST_RULES.md; decks/C_aristocrats_V1.3.txt (+ CHANGELOG); Forge card scripts (forge/app/res/cardsfolder/cardsfolder.zip); Scryfall 2026-10-14 snapshot, game_changers.json, banlist.json.
Scripts: /workspace/learn02/b5c.py (per-card cast / win-when-cast for C13) and /workspace/learn02/strict.py (strict retail, Nemesis method).

## B5 baseline (computed from logs)
- C13 won 62/200. C's 138 losses by winner: A12 68, B13 51, D13 19.
- V1.3 strict retail recomputed: **$98.15** (100 cards). This matches the CHANGELOG.

## Orzhov Signet: already handled
V1.3 already replaced Orzhov Signet with **Worn Powerstone** (V1.3 CHANGELOG, Arbiter PASS). No Signet swap is needed.
- Worn Powerstone works in the sims: C13 cast it in 37 games and won 8 of them (PLAYTEST_BATCH5.md counts 38 casts in 37 games).
- Arcane Signet was cast in 45 games, 14 of them wins.
- One caveat: the 8/37 (21.6%) win rate when Powerstone was cast is below C's 31% base. That is correlation only, and slow ramp tends to show up in long games.

## Swap 1 (proposed): Toxic Deluge → Kaya's Wrath
| Out | In |
|---|---|
| Toxic Deluge, $4.81 strict (MSC #161) | Kaya's Wrath, $0.46 strict (DMC #155) |

Reason: this is the same Forge-AI dead-card problem as the guild Signets.
- `toxic_deluge.txt` in Forge's cardsfolder carries `AI:RemoveDeck:All`.
- In B5, "Toxic Deluge" appears in **0 of 200 logs**: no cast, no discard, no zone change. That is true even though C13.dck (~/.forge/decks/commander/C13.dck) does list it.
- So C has effectively played 99 cards in every B5 game.
- Kaya's Wrath (`kayas_wrath.txt`) has no `AI:` flag. It is an unconditional wrath against A12's go-wide boards, and A12 is still C's top loss source (68 of 138 losses). It costs WWBB, which C's W/B mana base supports.
- I also checked the other "RemoveDeck:All" card in C, Fetid Heath. It does work: it was played in 55 logs, with `Mana: Fetid Heath` lines in 46 logs. Keep it.

## Considered, not proposed
- **Massacre Girl:** 4/21 (19.0%). **Village Rites:** 6/31 (19.4%). These are the lowest win-when-cast cards with n ≥ 20, but the samples are small, it is correlation only, and neither card has an AI flag. Revisit after B6.
- **Grim Haruspex:** shows 1 cast because it is mostly played face-down. It has 94 triggers in 46 logs. Not dead.
- I found no other cards with `AI:RemoveDeck:All` that are non-lands. Darkest Hour and Living Death carry `RemoveDeck:Random`, and both were cast (49 and 40 games).
- The script lookup missed 3 cards with special names (Elas il-Kor, Bartolomé del Presidio, Brightclimb Pathway). All three show casts or land plays in the logs.

## New total (strict retail)
- $98.15 − 4.81 + 0.46 = **$93.80** (100 cards, singleton preserved). Under the $100 target, so no ledger reason is needed.
- Kaya's Wrath: commander-legal, not a Game Changer, not banned, color identity W/B.

## 2-card infinite check
- Kaya's Wrath is a one-shot sorcery with no recursion, untap or mana text, so it cannot pair into a loop with any existing card.
- Its life gain (one life per creature you lose) is finite.
- Removing Toxic Deluge removes no loop.
- The existing pairs were re-checked on the V1.3 list. Ashnod's Altar + Pitiless Plunderer, Altar + Sifter of Skulls, Kaya's Ghostform, Victimize, Priest of Forgotten Gods and Sorin are all finite: no persist/undying creatures, and no untap or self-recursion. Massacre Girl's chain stops when creatures run out, and Pestilence costs {B} per activation.
- **No 2-card infinite.** The deck stays Bracket 2.

## Data gaps
- The logs have no draw or hand data. "0 mentions" for Toxic Deluge combines "never drawn" and "drawn but invisible". Either way the AI cannot cast a RemoveDeck:All card, and the Signets show the same pattern.
- I have not confirmed whether Forge strips RemoveDeck:All cards from AI decks at load. Fetid Heath shows it is at least not always removed.
- Win-when-cast numbers are correlations biased toward long games.
- Kaya's Wrath has never been played in any batch (0 logs), so how well the Forge AI uses it is untested.
- Prices are from the 2026-10-14 snapshot.
- Batch 5 notes: g187 broke R1 (probe failed); 10 games had AI TimeoutExceptions.
