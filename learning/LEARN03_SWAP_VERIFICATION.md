# LEARN03_SWAP_VERIFICATION (CH001-LEARN-03, Arbiter, 2026-10-15 PHT)
Script: learning/arbiter_learn03/verify.py (results.json). The post-swap lists checked are scratch copies in learning/arbiter_learn03/decks/*_LEARN03.txt. No real deck files were edited.

## Current versions
- **B, C, D:** `*_V1.3.txt`, each byte-identical to its V1.3_PENDING file (= V1.2 with the Signet replaced by Worn Powerstone).
- **A:** V1.2, not checked as instructed.

## Prices
Scryfall default_cards, updated 2026-10-14 17:05 PHT.
- **Ledger:** cheapest non-foil paper USD.
- **Strict retail:** same, excluding PLST, promo, memorabilia and gold-border printings.

## Per swap
Every removed card was present at the line shown, and no added card was already in its deck. Every added card is commander-legal, inside the commander's colours, not banned, not a Game Changer (absent from game_changers.json and Scryfall flag false), has no extra-turn text and does no MLD. No incoming card's Forge script contains `AI:RemoveDeck` of any variant; all seven scripts were read from forge/app/res/cardsfolder/cardsfolder.zip.

| Deck | OUT (line) → IN | Strict $ OUT → IN | Notes | Verdict |
|---|---|---|---|---|
| B | Comeuppance (L45) → Inspiring Overseer | 5.00 → 0.15 | ETB lifegain + draw. Brago and flicker cards repeat it, but each flicker is a finite trigger | PASS |
| B | Supreme Verdict (L42) → Elite Spellbinder | 2.37 → 0.29 | ETB hand disruption, flicker-repeatable but finite | PASS |
| C | Toxic Deluge (L41) → Kaya's Wrath | 4.81 → 0.46 | WWBB, inside Teysa's WB identity. One-shot wipe; death triggers are bounded by the number of creatures | PASS |
| D | Coruscation Mage (L54) → Fiery Inscription | 2.40 → 0.46 | ETB "the Ring tempts you" is fine in Commander. See Bracket 2 review | PASS (strong) |
| D | Fiery Cannonade (L53) → Propaganda | 0.22 → 1.93 | U enchantment, attack tax | PASS |
| D | Essence Scatter (L42) → Harmonic Prodigy | 0.07 → 5.07 | See Bracket 2 review | PASS (strong) |
| D | Consider (L29) → Fiery Confluence | 0.35 → 0.32 | "Destroy target artifact" is a single target, so not MLD | PASS |

## Bracket 2 review: Harmonic Prodigy, Fiery Inscription and Veyran
**CR 603.2d:** "An ability may state that a triggered ability triggers additional times. In this case, rather than simply determining that such an ability has triggered, determine how many times it should trigger, then that ability triggers that many times. An effect that states that an ability triggers additional times doesn't invoke itself repeatedly…"

Veyran's effect (instant/sorcery cast or copy, any permanent) and Prodigy's effect (Shaman or another Wizard) each add one trigger. Spell-cast triggers of D's Wizards and Shamans therefore trigger **3 times** per instant or sorcery.

**Wizards and Shamans in D:** Young Pyromancer, Thermo-Alchemist, Storm-Kiln Artist, Guttersnipe, Kessig Flamebreather, Talrand, Murmuring Mystic, Archmage Emeritus, Niv-Mizzet Parun, Stormcatch Mentor (static ability only) and Baral (static ability only).

**Examples:**
- Guttersnipe deals 6 damage to each opponent per instant or sorcery.
- Storm-Kiln Artist makes 3 Treasures per spell, so any spell costing 1–2 is mana-positive.
- Archmage Emeritus draws 3 cards per spell.
- Niv-Mizzet draws 3 cards (cast trigger), and each draw triggers its ping twice (Prodigy), for 6 pings.
- Fiery Inscription is not a Wizard, so Prodigy doesn't apply. Veyran makes it 4 damage to each opponent per instant or sorcery.

**Infinite? No.** Neither card untaps, recurs or copies spells, and every loop still needs a new spell cast from a finite hand or library. Prodigy + Veyran is a multiplier, not a loop. No 2-card or 3-card combo was found, so this is not a hard FAIL under the rules.

**Still a concern.** Storm-Kiln + Archmage Emeritus + Veyran was already flagged as near-deterministic by Nemesis. Adding Prodigy raises that engine to ×3, so one cheap-spell chain with Prodigy, Storm-Kiln and Emeritus can easily drain the library and burn the table. Arbiter rating: **legal and finite, but a strong Bracket 2 outlier.** Recommendation: disclose it in the deck notes, and ask Nemesis or Voltaire whether it fits the spirit of Bracket 2 before applying. Optional softer version: skip Prodigy (keep Essence Scatter).

## Totals (ledger / strict retail, USD)
| Deck | V1.3 now | After LEARN-03 | Flags |
|---|---|---|---|
| B | 84.06 / 87.73 | **77.13 / 80.80** | ≤ $100 |
| C | 90.91 / 98.15 | **86.56 / 93.80** | ≤ $100 |
| D | 76.18 / 79.11 | **80.92 / 83.85** | ≤ $100 |

All three post-swap lists pass the full audit: 100 cards, singleton, legal, in colour, no bans, 0 Game Changers, no 2-card infinites, no extra turns, no MLD.

## Carry-over
`decks/C_aristocrats.txt` (the frozen V1) is still overwritten with the V1.1 contents.
