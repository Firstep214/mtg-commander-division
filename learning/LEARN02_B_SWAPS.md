# CH001-LEARN-02 — Deck B (B_control_V1.1, Brago) swap proposals
Prepared 2026-10-15 (PHT) by Nyx. **Proposals only. No deck file was changed.**

## Sources
- Win stats: `forge/PLAYTEST_BATCH4.md` (200 games: B11 44/200 = 22.0%, CI 16.8–28.2; A12 94/200 = 47.0%), `learning/batch4/B4_CARD_STATS.txt`, `learning/batch4/B4_NOTES.md`.
- Prices and legality: Scryfall bulk `default_cards`, updated_at 2026-10-14T09:05:48Z (`sources/2026-10-14/scryfall_snapshot_state.json`). Strict retail is the minimum non-foil `prices.usd` across paper printings, the same rule as the price ledgers. Every card below has a usd price, so nothing is missing.
- Game Changers: `sources/2026-10-14/game_changers.json` (WotC, retrieved 2026-10-14T10:56:58Z), cross-checked with the Scryfall `game_changer` flag. Banlist: `sources/2026-10-14/banlist.json`.
- Baseline total: B_control_V1.1 recomputed from the snapshot = **$80.48** (100 cards, 0 unpriced). This matches SWAP_VERIFICATION.md.

## Caveat on the stats
"Win% when cast" means B's wins among the games where it cast the card. That is correlation, not cause. Sweepers get cast when B is already behind, and late cards show up mostly in long games. Forge AI decides what gets cast, so "never cast" can be an AI quirk and doesn't mean the card is bad. Lands are played, not cast, so they always show as "never cast" and are ignored here.

## Swaps (out -> in)
| # | Out | $ | In | $ | Δ$ |
|---|---|---|---|---|---|
| 1 | Ghostly Flicker | 1.16 | Skyclave Apparition | 0.26 | −0.90 |
| 2 | Deputy of Detention | 0.34 | Aetherize | 0.30 | −0.04 |
| 3 | Hallowed Burial | 0.48 | Comeuppance | 5.00 | +4.52 |

**New total: $84.06** (80.48 − 0.90 − 0.04 + 4.52). That is under the $100 target, so no over-$100 reason is needed. The deck stays at 100 cards and in W/U colors (Aetherize is U; Apparition and Comeuppance are W).

### Reasons
1. **Ghostly Flicker -> Skyclave Apparition.** Ghostly Flicker was never cast in 200 B4 games (B4_CARD_STATS "never cast" list). Apparition is a 3-mana creature with an exile-removal ETB, which fits the flicker shell: Brago, Soulherder, Restoration Angel and Ephemerate re-trigger it. The cast cards closest to it, Banishing Light (19/50, 38.0%) and Oblivion Ring (22/64, 34.4%), sit above B's 22% base. Caveat: Flicker's 0 casts may be Forge AI not handling its two targets.
2. **Deputy of Detention -> Aetherize.** Deputy was never cast in 200 games. A12 is the main threat: it won 94/200 and B's B4 losses split A12 94 / C11 35 / D11 27. Aetherize is an instant that returns all attackers to hand, and returned tokens cease to exist. It leaves B's board alone, which a symmetrical wrath doesn't. This is the same plan as Settle the Wreckage, but Settle was cast only once (0/1), so its effect is still untested.
3. **Hallowed Burial -> Comeuppance.** Burial won 6/39 when cast (15.4%, below the 22% base). The B4 notes say B's three symmetrical sweepers also hit B's own creature-based board. Comeuppance is a one-sided answer to the big combat turn: it prevents the damage and reflects it, killing attacking creatures. B keeps Supreme Verdict, Wrath of God, Austere Command, Fumigate and Settle, so it still has 5 mass answers. It is the most expensive pick ($5.00, MAR #1).

### Considered, not swapped
- **Supreme Verdict** (7/47, 14.9%, the lowest rate) and **Reflector Mage** (9/53, 17.0%) are both weak by correlation. I kept Verdict this round so the deck doesn't lose two of its symmetrical wraths at once against A's token boards; Burial goes first. Verdict is the next cut if B5 repeats the pattern. I kept Reflector Mage because its sample is a flicker-target creature that is often cast early, so the low rate is hard to read.
- **Azorius Signet** was never cast, but Signets were never cast in any deck. Per Magnus, it stays until Vector's quirk check.
- **Reliquary Tower** is a land, so "never cast" doesn't apply.

## Rule checks (v2.3)
| In card | Commander legal | Banned | Game Changer (WotC list / Scryfall flag) | Color identity |
|---|---|---|---|---|
| Skyclave Apparition | legal | no | no / no | W |
| Aetherize | legal | no | no / no | U |
| Comeuppance | legal | no | no / no | W |

- **2-card infinites (checked against the whole deck):** none found. Apparition's leave-the-battlefield trigger gives the opponent a token, and none of the flicker effects (Brago, Soulherder, Ephemerate, Cloudshift, Eerie Interlude, Restoration Angel, Flickerwisp, Teleportation Circle) loop without limit with it. Aetherize and Comeuppance are one-shot instants. Removing Ghostly Flicker also takes out the deck's only Archaeomancer-style recursion piece.
- **Bracket 2:** no Game Changers, no tutors, no extra turns, and no mass land destruction were added. Whether it stays Bracket 2 is my judgment; the auditor should confirm.
