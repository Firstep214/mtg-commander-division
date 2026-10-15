# SWAP_VERIFICATION (CH001-LEARN-01, Arbiter, 2026-10-15 PHT)
Script: learning/arbiter_swap/verify.py (results.json). No deck files were edited.

## Sources and method
- **Rule "v2.3" is not in PLAYTEST_RULES.md.** That file only holds R1 (dice-roll seating). The house constraints applied here come from STATUS_CH001.md line 2 ("each ≤ US$100 incl. commander + all lands; Bracket 2; zero Game Changers; no 2-card infinites") and prompts/v2.3_installed/07_Arbiter.md ("exactly 100 cards and <=$100 after each accepted swap"). PLAYTEST_RULES.md names no price method, so this uses the method from the ledger and scryfall_snapshot_state.json.
- **Prices:** Scryfall default_cards bulk `sources/2026-10-14/default-cards-20261014090548.jsonl.gz`, updated 2026-10-14 17:05 PHT. Ledger price = lowest `prices.usd` (non-foil, paper, non-digital) per card name.
- **Strict retail:** same rule, but excluding The List (PLST), promo and memorabilia printings (the Nemesis "strict" basis).
- **Card checks:** legality, colour identity and Game Changer flag come from the same bulk file, plus banlist.json and game_changers.json.
- **Base decks:** A = decks/A_tokens_V1.1.txt (current version: −Wrath of God +Inspired Charge). B, C and D = the frozen V1 .txt files.

## Per-swap results
Every OUT card was found in its base deck, and no IN card was already there. Every IN card is commander-legal, inside the commander's colours, not banned, not a Game Changer, and has no extra-turn text.

| Deck | OUT → IN | Ledger price (OUT → IN) | Colour identity | New 2-card infinite? | Extra turns / MLD | Verdict |
|---|---|---|---|---|---|---|
| A (W) | Sunfall → Ghostly Prison | 0.31 FRC → 5.68 PLST (strict 5.78 C19) | W | No: static attack tax, no loop with Intangible Virtue, Felidar Retreat or Divine Visitation | No | PASS (rules), see budget |
| A (W) | Mirror Entity → Get Lost | 1.01 PLST → 3.22 LCI | W | No: one-shot removal; Map tokens go to the opponent | No | PASS (rules), see budget |
| B (WU) | Conjurer's Closet → Fumigate | 3.19 → 0.25 | W | No: one-shot sweeper | Not MLD (creatures only) | PASS |
| B (WU) | Mystic Confluence → Settle the Wreckage | 0.49 → 0.41 | W | No | Not MLD: exiles attacking creatures and gives that player *basic lands* (ramps them) | PASS |
| C (WB) | Wake the Dead → Massacre Wurm | 1.37 → 2.63 | B | No: ETB −2/−2 is one-shot; drains are bounded by opponents' creatures. Bigger burst with Teysa (doubled death triggers) plus Blood Artist/Zulaport, but finite | No | PASS |
| C (WB) | Sevinne's Reclamation → Pestilence | 0.45 → 0.30 | B | No: each activation costs {B}, and C has no infinite black mana. With Teysa, Blood Artist and Bastion it is a strong finite drain, so disclose it as a mana-bound engine | No (creatures/players only) | PASS |
| D (UR) | Mizzix's Mastery → Fiery Cannonade | 3.78 → 0.22 | R | No | No | PASS (note: it also kills D's own Young Pyromancer / Talrand tokens) |
| D (UR) | Past in Flames → Coruscation Mage | 2.53 → 2.40 | R | No: 1 damage per noncreature spell cast, with no untap or recursion. Veyran doubles the trigger, which is finite. Removing Past in Flames lowers loop risk | No | PASS |

## Recomputed deck totals (ledger / strict retail, USD)
| Deck | Pre-swap | Post-swap | vs $100 cap |
|---|---|---|---|
| A (V1.1 base) | 94.61 / 99.30 | **102.19 / 106.87** | OVER by 2.19 (ledger) / 6.87 (strict) |
| B | 83.50 / 87.17 | **80.48 / 84.15** | under |
| C | 85.97 / 93.22 | **87.08 / 94.33** | under |
| D | 80.45 / 83.38 | **76.76 / 79.69** | under |

**A's $102.19 claim:** the number is reproduced exactly on the ledger basis. It depends on a The List (PLST) printing of Ghostly Prison, though. On strict retail the post-swap total is $106.87.

**A's approval is not supported by the files.** The only owner approval on file (A_tokens_V1.1_CHANGELOG.md) is for "slightly over" based on V1 strict retail $102.78. Nothing in the files records approval of $102.19 or $106.87. The changelog and the arbiter prompt both say the cap is ≤$100 after each accepted swap. So A's swaps are **FAIL on budget unless Voltaire explicitly re-approves the new total**.

A cheaper option: swap out Unbreakable Formation ($0.75) instead of Mirror Entity ($1.01). That only saves about $0.26 and still leaves A over the cap.

## Verdict
- **B, C, D:** both swaps PASS.
- **A:** both swaps PASS the rules checks, but the pair is a **budget FAIL** pending explicit owner approval of $102.19 (ledger) / $106.87 (strict).


## Budget approval addendum (2026-10-15, recorded by Magnus)
Voltaire approved Deck A CH001-LEARN-01 swaps up to $106.87 strict retail (covers $102.19 cheapest-printing basis), via in-chat decision 2026-10-15 03:50 PHT. Deck A budget status: PASS (approved overage).
