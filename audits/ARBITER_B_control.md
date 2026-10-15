# ARBITER audit — B_control
Task CH001-AUD-ARB · Arbiter · 2026-10-14 (PHT) · deck sha256 `b1e0dbe140c23c3a2be29d99bf7ef4533d4860af6f731b25b21de309a108444b` (deck not modified)

## OVERALL: PASS

Commander: Brago, King Eternal  (Bracket 2 target)

| Check | Result | Detail |
|---|---|---|
| Card names resolve (Scryfall oracle bulk) | PASS | all names resolved |
| Count = 100 incl. commander (CR 903.5a) | PASS | total 100 |
| Singleton (CR 903.5b) | PASS | no duplicates; only basics have qty >1 |
| Commander eligibility (CR 903.3) | PASS | line 1 `1 Brago, King Eternal`; Legendary Creature — Spirit Noble; partner ability: False; Scryfall commander legality: legal |
| Color identity (CR 903.4, 903.5c/d) | PASS | commander identity UW; off-identity: none |
| Bans (banlist.json 42 named + category bans + Scryfall legality) | PASS | none |
| Game Changers (Bracket 2 = 0) | PASS | count 0  |
| 2-card infinite combos | PASS | none found |
| Extra-turn cards | PASS | none (oracle text search for "extra turn") |
| Mass land destruction | PASS | none (oracle text regex) |

## Combo review notes
Ghostly Flicker is here, but no Mystic Sanctuary, Archaeomancer, Mnemonic Wall or Peregrine Drake. Brago + flicker cards make value, not a loop. Restoration Angel and Agent of Treachery have no Kiki-Jiki or Deadeye partner.

## CR citations (quoted from MagicCompRules_20260925.txt, effective September 25, 2026)
- 903.3: "Each deck has a legendary card designated as its commander. That card must be either (a) a creature card, (b) a Vehicle card, or (c) a Spacecraft card with one or more power/toughness boxes."
- 903.3a: "Some cards have an ability that states the card can be your commander."
- 903.4: "The color identity of a card is the color or colors of any mana symbols in that card's mana cost or rules text, plus any colors defined by its characteristic-defining abilities (see rule 604.3) or color indicator (see rule 204)."
- 903.4c: "Reminder text is ignored when determining a card's color identity." / 903.4d: back face of DFC included.
- 903.5a: "Each deck must contain exactly 100 cards, including its commander."
- 903.5b: "Other than basic lands, each card in a Commander deck must have a different English name."
- 903.5c: "A card can be included in a Commander deck only if every color in its color identity is also found in the color identity of the deck's commander."
- 903.5d: basic land types may only be included if each color of mana it could produce is in the commander's identity.
- 702.124a/h: partner abilities allow two commanders (not applicable here: commander has no partner ability).

## Method and source gaps
- Script: /workspace/mtg/audits/arbiter_scripts/audit.py (results.json). Card data: /workspace/mtg/data/oracle.jsonl.gz (Scryfall oracle_cards, updated 2026-10-14T09:01Z = 17:01 PHT). Color identity comes from Scryfall `color_identity`, which follows CR 903.4 and includes rules-text symbols.
- Source hashes: SHA256SUMS verified OK for all text/HTML sources.
- Game Changers: game_changers.json all_cards plus per-colour lists plus the Scryfall `game_changer` flag (Tergrid DFC name variance handled).
- Commander = line 1 of the deck file (file convention; the deck has no explicit commander marker).
- GAP: the local sources do not contain the per-bracket expectation text for two-card infinites, extra turns or mass land denial. formats_commander.txt only names these as "barometers". Zero-tolerance here applies Voltaire's house rule (SOURCES.md), not quoted Wizards text.
- LIMIT: combo detection uses a curated list of known pairs plus a manual review of the decklist. It is not an exhaustive combo database (no Commander Spellbook snapshot is in sources). Extra-turn and MLD checks are oracle-text regexes plus a manual read of the list.
