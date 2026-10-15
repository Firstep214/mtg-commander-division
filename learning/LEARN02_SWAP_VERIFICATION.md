# LEARN02_SWAP_VERIFICATION (CH001-LEARN-02, Arbiter, 2026-10-15 PHT)
Script: learning/arbiter_learn02/verify.py (results.json). No deck files were edited.

## Rules applied
From PLAYTEST_RULES.md and CURRICULUM.md (budget rule 2026-10-15 04:44 PHT, swap rule 05:12 PHT):
- Target $100; hard cap $120 at strict retail; anything over $100 needs a ledger line.
- Unlimited swaps; each change is saved as a new deck version.
- Bracket 2, no Game Changers, no 2-card infinites.

## Pricing
Source: Scryfall default_cards, updated 2026-10-14 17:05 PHT.
- **Ledger** = cheapest non-foil paper `prices.usd` per card.
- **Strict retail** = the same, but excluding The List (PLST), promo, memorabilia and gold-border printings (same rule as audits/nemesis_strict_retail.py).

## Current versions
- **B, C, D:** V1.1 (`*_V1.1.txt`). All 8 LEARN-01 swaps are present: B has Fumigate + Settle; C has Massacre Wurm + Pestilence; D has Fiery Cannonade + Coruscation Mage. A's two swaps are presumably in V1.2, which was not checked as instructed.
- ⚠ **Integrity issue:** `decks/C_aristocrats.txt` (the frozen V1) was modified at 2026-10-15 04:12 PHT and is now byte-identical to C_aristocrats_V1.1.txt. The original V1 contents are lost from that file. B and D's V1 files are unchanged.

## Game Changer check: Toxic Deluge
- **game_changers.json** (retrieved 2026-10-14 10:56Z = 18:56 PHT; Wizards list updated 2025-10-22 / 2026-02-09): not listed.
- **Scryfall `game_changer` flag** (bulk 2026-10-14 09:05Z = 17:05 PHT), on every printing: false.
- **Result: not a Game Changer.**

## Per swap
Every added card below is commander-legal, inside the commander's colours, not banned, not a Game Changer, has no extra-turn text and does no land destruction.

| Deck | OUT (line) → IN | Strict $ OUT → IN | Infinite / MLD review | Verdict |
|---|---|---|---|---|
| B | Ghostly Flicker (L29) → Skyclave Apparition | 1.16 → 0.26 | Flicker effects (Brago, Ephemerate, Restoration Angel) give repeat value, but each trigger is bounded and there is no loop. Also removes the Ghostly Flicker loop risk | PASS |
| B | Deputy of Detention (L22) → Aetherize | 0.34 → 0.30 | One-shot bounce | PASS |
| B | Hallowed Burial (L45) → Comeuppance | 0.48 → 5.00 (MAR #1) | One-shot | PASS |
| B | Azorius Signet (L6) → "Azorius Talisman" = **Talisman of Progress** | 0.26 → 0.28 | Already in the deck at **L5 `1 Talisman of Progress`**, so this breaks singleton (CR 903.5b). Fallbacks also fail: Mind Stone is at L4, Fellwar Stone at L9 | **FAIL** |
| C | Undying Evil (L41) → Toxic Deluge | 0.40 → 4.81 | One-shot −X/−X. Death triggers (Blood Artist, Zulaport, Teysa doubling) are bounded by the number of creatures | PASS |
| C | Viscera Seer (L18) → Massacre Girl | 0.49 → 0.49 | Each death makes every other creature −1/−1, and that can chain. It ends when no creatures remain, because the board is finite and tokens aren't regenerated: Pitiless Plunderer makes Treasures (non-creatures) and Ashnod's Altar needs creatures to sacrifice. Teysa doubles death-caused triggers, but the total is still bounded. Mass drain is possible but **finite, not infinite**. Also removes a free sac outlet. It kills C's own board, which is a strategy note, not a rules issue | PASS |
| C | Path to Exile (L49) → Go for the Throat | 0.85 → 0.30 | One-shot | PASS |
| C | Orzhov Signet (L4) → **Talisman of Hierarchy** | 0.30 → 0.40 | Already in the deck at **L5 `1 Talisman of Hierarchy`**, so singleton fails. Fallbacks also fail: Mind Stone L6, Fellwar Stone L7 | **FAIL** |
| D | Faithless Looting (L32) → Mulldrifter | 0.37 → 0.28 | One-shot | PASS |
| D | Blasphemous Act (L47) → Aetherize | 0.76 → 0.30 | One-shot | PASS |
| D | Izzet Signet (L4) → **Talisman of Creativity** | 0.29 → 0.49 | Already in the deck at **L5 `1 Talisman of Creativity`**, so singleton fails. Fallbacks also fail: Mind Stone L6, Fellwar Stone L7 | **FAIL** |

### Possible Signet replacements (not verified)
None of these is in any of the three decks; all are legal and not Game Changers:

| Card | Strict $ | Notes |
|---|---|---|
| Star Compass | 0.49 (IMA) | Enters tapped |
| Prismatic Lens | 0.27 (EMA) | Has a {T}: add {C} ability, so the AI may cast it |
| Coldsteel Heart | 1.10 (CSP) | Enters tapped |
| Worn Powerstone | 0.26 | Taps for two colourless; doesn't fix colours |
| Everflowing Chalice | 0.28 | Doesn't fix colours |

Whether the Forge AI will cast these is untested. Each needs its own verification before it goes in.

## Final totals (all PASS swaps applied; Signet slots unchanged)
| Deck | Before, ledger / strict | After, ledger / strict | Status |
|---|---|---|---|
| B (V1.1 → proposed V1.2) | 80.48 / 84.15 | **84.06 / 87.73** | ≤ $100, no ledger reason needed |
| C | 87.08 / 94.33 | **90.95 / 98.19** | ≤ $100 |
| D | 76.76 / 79.69 | **76.21 / 79.14** | ≤ $100 |

All decks stay at 100 cards with no new 2-card infinite. Using any of the replacement rocks above changes each total by less than $1.

## V1.3_PENDING (Forge follow-up, Arbiter, 2026-10-15 08:3x PHT)
Script: learning/arbiter_learn02/verify_v13.py (v13_results.json); full checks reuse audits/arbiter_scripts/audit.py. No deck files were edited.

### Diffs
- **V1.1 → V1.2:** exactly the 8 passing LEARN-02 swaps, and nothing else.
  - B: L22 Deputy of Detention → Aetherize; L29 Ghostly Flicker → Skyclave Apparition; L45 Hallowed Burial → Comeuppance.
  - C: L18 Viscera Seer → Massacre Girl; L41 Undying Evil → Toxic Deluge; L49 Path to Exile → Go for the Throat.
  - D: L32 Faithless Looting → Mulldrifter; L47 Blasphemous Act → Aetherize.
- **V1.2 → V1.3_PENDING:** exactly one line per deck, and nothing else.
  - B: L6 `1 Azorius Signet` → `1 Worn Powerstone`.
  - C: L4 `1 Orzhov Signet` → `1 Worn Powerstone`.
  - D: L4 `1 Izzet Signet` → `1 Worn Powerstone`.

### Checks (all three V1.3_PENDING files)
- **PASS on every check:** 100 cards, singleton, card names resolve, commander eligible, colour identity, no bans, 0 Game Changers, no extra turns, no MLD.
- **Worn Powerstone:** colourless, commander-legal, not banned, not a Game Changer. It enters tapped and taps for {C}{C}. No infinite: nothing in the decks untaps artifacts, and Brago flickering it brings it back tapped.
- **2-card infinites:** none.
  - C's Ashnod's Altar pairs and D's Storm-Kiln Artist + Haughty Djinn were reviewed earlier as finite.
  - The LEARN-02 adds are also finite: Massacre Girl's chain stops once the creatures run out, and Toxic Deluge is a one-shot.

### Forge script
`forge/app/res/cardsfolder/cardsfolder.zip` → worn_powerstone.txt has **no `AI:RemoveDeck` line**. Its mana ability is `A:AB$ Mana | Cost$ T | Produced$ C | Amount$ 2`, a net-mana {T} ability, unlike the guild Signets' `Cost$ 1 T` filter. It also has an ETBTapped replacement.

### Totals (Scryfall 2026-10-14 17:05 PHT; ledger / strict retail)
| Deck | Recomputed | Forge claim | Match |
|---|---|---|---|
| B V1.3_PENDING | $84.06 / $87.73 | $84.06 / $87.73 | ✅ |
| C V1.3_PENDING | $90.91 / $98.15 | $90.91 / $98.15 | ✅ |
| D V1.3_PENDING | $76.18 / $79.11 | $76.18 / $79.11 | ✅ |

All three are under $100, so no ledger reason is needed.

### Verdict
**B PASS · C PASS · D PASS.**
- Carry-over note: C's frozen V1 file (`C_aristocrats.txt`) is still overwritten with the V1.1 contents.
