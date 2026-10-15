# CH001-LEARN-03 — Deck B (B_control_V1.3, Brago) swap proposals
Prepared 2026-10-15 (PHT) by Nyx. **Proposals only. No deck file was changed.**

## Sources
- Batch 5: `forge/PLAYTEST_BATCH5.md` (B13 51/200 = 25.5%, CI 20.0–32.0; A12 68, C13 62, D13 19) and logs `forge/playtest_batch5/g001–g200.log`.
- Card stats: B5 had no per-card file, so I re-ran the Batch 4 parser unchanged except for deck names and folder: `learning/batch5/b5_cards_nyx.py` -> `learning/batch5/B5_CARD_STATS.txt`. Its winner counts match PLAYTEST_BATCH5.md (A12 68, B13 51, C13 62, D13 19).
- Prices and legality: Scryfall `default_cards` snapshot updated 2026-10-14T09:05:48Z (17:05 PHT). Strict retail is the cheapest non-foil paper `prices.usd`. Game Changers: `sources/2026-10-14/game_changers.json` plus the Scryfall flag.
- Baseline: B_control_V1.3 recomputed = **$84.06**, 100 cards, 0 unpriced. This matches the V1.3 changelog.

## Signet (Vector's finding)
**Already done.** V1.3 replaced Azorius Signet with Worn Powerstone ($0.26), per B_control_V1.3_CHANGELOG.md. The Signet is no longer in the deck, so no swap is proposed. Batch 5 shows the AI plays the replacement: B13 cast Worn Powerstone in 54 games (PLAYTEST_BATCH5.md; win when cast 16/54 = 29.6%, above the 25.5% base). Arcane Signet, Mind Stone, Fellwar Stone and Talisman of Progress were already in the deck and are all cast by the AI. Adding another would break singleton.

## Swaps (out -> in)
| # | Out | $ | In | $ | Price change |
|---|---|---|---|---|---|
| 1 | Comeuppance | 5.00 | Inspiring Overseer | 0.15 | **−4.85 (cheaper)** |
| 2 | Supreme Verdict | 2.37 | Elite Spellbinder | 0.29 | **−2.08 (cheaper)** |

**New total: $77.13** (84.06 − 4.85 − 2.08), **down $6.93**. That is under the $100 target, so no reason needs logging. The deck stays at 100 cards and singleton (79 distinct names; only Plains ×11 and Island ×12 repeat). Colors stay W/U.

### Reasons
1. **Comeuppance -> Inspiring Overseer.** Comeuppance was never cast in 200 B5 games (B5_CARD_STATS "never cast" list). Across all 200 logs it appears in only one line, a mill (`Zone Change: Ai-B13 milled Comeuppance`). Its Forge script is a bare `SP$ Effect` prevention spell. My inference is that the AI has no logic to cast it on the opponent's attack; I haven't confirmed that. It's the same dead-card pattern as the guild Signets, and it was the most expensive LEARN-02 addition. Overseer is a 3-mana flier that gains 1 life and draws a card on entry, and Brago and B's flicker cards re-trigger it. B's flicker and value creatures win above base when cast: Soulherder 23/51 (45.1%), Kor Skyfisher 21/48 (43.8%), Charming Prince 27/66 (40.9%). The other LEARN-02 additions did get cast: Skyclave Apparition 20/51 (39.2%), Aetherize 10/31 (32.3%).
2. **Supreme Verdict -> Elite Spellbinder.** This is the revisit I flagged in LEARN-02. Verdict won below base for the second batch running: B4 7/47 (14.9% vs 22%) and B5 9/44 (20.5% vs 25.5%). Spellbinder is a 3-mana flier whose entry trigger exiles a card from an opponent's hand and makes it cost {2} more. It's a flicker target that adds pressure, unlike a wrath that also kills B's own creatures. B keeps Wrath of God, Austere Command, Fumigate and Settle the Wreckage as mass answers, plus Aetherize against attacks.

### Caveats
- **Correlation only.** Wraths get cast when B is already behind, which by itself lowers their win rate. That could explain all of Verdict's low number.
- **Wrath of God** did worse than Verdict in B5: 9/47 (19.1%). I left it in so B keeps a sorcery-speed reset against A12 and C13. A12 won 68 games and C13 62 in B5, and B's losses split A12 68 / C13 62 / D13 19. If B6 shows the same, cutting Wrath is the next step. With two sweepers gone, B is weaker against wide boards, so B6 should be watched for token losses.
- **Settle the Wreckage** was cast in only 2 games (won both), so its sample is too small to judge.
- The batch is about ±6 points of noise either way: B4 -> B5 for B was 44 -> 51 wins with overlapping CIs. Several cards changed between V1.1 and V1.3, so no win-rate change can be credited to one card.
- The parser counts only `cast` lines, so lands show as "never cast" and are ignored.

## Rule checks (v2.3)
| In card | Commander legal | Banned | Game Changer | Color identity | Forge AI flag |
|---|---|---|---|---|---|
| Inspiring Overseer | legal | no | no | W | no RemoveDeck in its script |
| Elite Spellbinder | legal | no | no | W | no RemoveDeck in its script |

- **2-card infinites (checked against the whole deck):** none. Both cards have one-shot entry triggers. None of the deck's flicker cards (Brago, Soulherder, Ephemerate, Cloudshift, Eerie Interlude, Restoration Angel, Flickerwisp, Teleportation Circle, Charming Prince) give an untapped repeatable loop with them.
- **Bracket 2:** no Game Changers, tutors, extra turns or mass land destruction were added. That this stays Bracket 2 is my judgment; the auditor should confirm.
