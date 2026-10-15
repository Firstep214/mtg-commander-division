# CH001-LEARN-02: Deck C (C_aristocrats_V1.1) swap proposals
Author: Vex (Deck C) · 2026-10-15 (Asia/Manila) · PROPOSAL ONLY. No deck file was edited. Needs Arbiter/Nemesis verification before it is applied as a new version (V1.2).
Sources: forge/PLAYTEST_BATCH4.md; learning/batch4/B4_NOTES.md; learning/batch4/B4_CARD_STATS.txt; PLAYTEST_RULES.md (budget rule 04:44 PHT, swap rule 05:12 PHT); CURRICULUM.md; forge/playtest_batch4/g001-g200.log (grep checks only); sources/2026-10-14 Scryfall snapshot, game_changers.json, banlist.json.
Pricing script: /workspace/learn02/strict.py. It uses the strict-retail method of audits/nemesis_strict_retail.py: cheapest non-foil paper USD, excluding PLST, promo, memorabilia and gold-border printings.

## B4 context (from the files)
- C11 won 35/200 (17.5%, CI 12.9–23.4) and 31/195 R1-compliant games. It won 6 of the 47 games where it went first.
- C11's 165 losses by winner: A12 94, B11 44, D11 27 (B4_CARD_STATS.txt). A12 Adeline tokens remain the main problem.
- Strong when cast: Blood Artist 14/36, Midnight Reaper 14/40, Liesa 15/43. Weak when cast: Path to Exile 4/43 (9.3%), Despark 8/57, Night's Whisper 5/33. These are correlations only (B4_NOTES caveat).
- Massacre Wurm (V1.1 add): 9/31 (29.0%) when cast. Pestilence: 8/36 (22.2%).

## Lead verification (grep of the g001–g200 logs)
- **Viscera Seer:** never cast. Its only appearance in all 200 logs is one `Ai-C11 discards Viscera Seer` line. The Forge AI does not deploy it.
- **Undying Evil:** 0 mentions in 200 logs (never cast).
- **Grim Haruspex is NOT dead.** It shows as "never cast" because Forge plays it face-down. The stats line `Morph 13/50` is that card, and the logs show 54 `has unmorphed Grim Haruspex` lines and 142 `triggered Grim Haruspex` lines in 49 files. Keep it.
- **Orzhov Signet:** only one `discards Orzhov Signet` line. Kept per instruction, pending the Vector quirk check.

## Proposed swaps (3)
| # | Out (strict $) | In (strict $, printing) | Reason (B4 data) |
|---|---|---|---|
| 1 | Undying Evil ($0.40, DKA #77) | **Toxic Deluge** ($4.81, MSC #161) | Undying Evil was never cast in 200 games. A12 won 94 of C's 165 losses. Deluge answers token boards that anthems have pumped beyond Massacre Wurm's -2/-2 and Pestilence's damage, and C rebuilds afterwards with Living Death (15/48), Return to the Ranks (11/35), Unearth and Victimize. |
| 2 | Viscera Seer ($0.49, TDC #199) | **Massacre Girl** ($0.49, WAR #99) | The Forge AI never cast Viscera Seer (only 1 discard line). C still has 5 other sac outlets: Ashnod's Altar, Carrion Feeder, Yahenni, Elas il-Kor, Priest. Massacre Girl is a second sweeper against A12 tokens that chains through Teysa-doubled death triggers. The cards that pay off death triggers are C's best performers (Blood Artist 14/36, Midnight Reaper 14/40). |
| 3 | Path to Exile ($0.85, FRC #30) | **Go for the Throat** ($0.30, FDC #100) | Path is C's lowest win-rate-when-cast card at 4/43 (9.3%, against a 17.5% base). This is correlation only. Path also ramps the opponent, and A12/B11 are the decks beating C. Go for the Throat is instant 2-mana removal with no land gift; it misses only artifact creatures. |

Not proposed:
- Grim Haruspex: active via morph (see above).
- Signets: held per instruction.
- Despark (8/57) and Night's Whisper (5/33): also below base, but cutting more cards would thin the interaction and draw suite on correlation alone. Revisit after V1.2 is tested.

## New total (strict retail)
- V1.1 strict total recomputed: **$94.33**. This matches SWAP_VERIFICATION.md's 94.33.
- Swap deltas: +4.41 (Deluge), 0.00 (Girl), −0.55 (GftT), net **+$3.86**.
- **V1.2 proposed: $98.19 strict retail, 100 cards.** That is under the $100 target, so no ledger reason is needed, and under the $120 cap.
- All three adds are commander-legal, not on the Game Changer list, not banned, and inside the W/B color identity (all mono-B).

## 2-card infinite check
Method: I checked every card in V1.1 plus the three adds for persist, undying, return-to-battlefield, untap and mana-producing text.
- **Ashnod's Altar + Pitiless Plunderer:** each sacrifice nets {C}{C} plus a Treasure, but nothing returns the creature. Finite (bounded by creature count). The deck has no persist creatures.
- **Altar/Plunderer + Undying Evil:** undying returns a creature once, and it comes back with a +1/+1 counter, so it does not return again. Finite. Swap 1 removes Undying Evil anyway, which removes this loop risk.
- **Kaya's Ghostform:** one-time return, the Aura is gone afterwards. Finite.
- **Sifter of Skulls + Altar:** Scions come only from nontoken deaths. Finite.
- **Priest of Forgotten Gods, Sorin's −X, Victimize:** each needs fresh resources per use. Finite.
- **Massacre Girl:** her repeated −1/−1 wave ends when no creatures are left. With Teysa it is a large but finite drain. There is no 2-card loop with Blood Artist, Zulaport or Bastion.
- **Toxic Deluge, Go for the Throat:** one-shot spells.
- **Result: no 2-card infinite found**, and the deck stays Bracket 2.
- Disclosure: Massacre Girl + Teysa + drain payoffs can produce a large one-turn swing. It is finite and mana-bound, the same class as Pestilence in SWAP_VERIFICATION.md.

## Data gaps
- The logs have no draw or hand data, so "never cast" cannot separate "never drawn" from "drawn but not played". Viscera Seer was drawn at least once (it was discarded).
- Win-when-cast numbers are correlations biased toward long games (B4_NOTES caveat).
- 5 games broke R1 (g075 g100 g121 g146 g181) and 11 had AI TimeoutExceptions. Both are included in the card stats.
- Prices come from the 2026-10-14 snapshot and may have drifted since.
- Forge AI handling of Massacre Girl and Toxic Deluge (choosing X) is untested and may be poor. A test batch is needed.
