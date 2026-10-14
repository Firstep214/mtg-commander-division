# MTG Division Curriculum — v0.1 (DRAFT, 2026-10-14)
Status: syllabus + formats only. **No agent has taken a lesson or quiz yet** (15 MTG agents created 2026-10-14 per Manager; none has run a lesson yet). Entries are added only when a real run happens.

## Sources of truth (cite with date)
- Wizards of the Coast Magic: The Gathering Comprehensive Rules (current edition; record effective date on download).
- Official Commander rules, ban list, Bracket + Game Changers guidance (record page date).
- Scryfall bulk data snapshot: oracle_cards 2026-10-14T09:01:55Z, default_cards 2026-10-14T09:05:48Z (/workspace/mtg/data).
- Mark anything else (playgroup rules, Rule 0 agreements) as HOUSE RULE.

## Syllabus (units)
1. Turn structure, priority, the stack (CR 117, 405, 5xx)
2. Layers & timestamps (CR 613), dependency
3. Replacement vs triggered effects (CR 614, 603)
4. Commander rules: command zone, tax, 21 commander damage, colour identity (CR 903)
5. Tokens & copies (CR 111, 707)
6. Combat in multiplayer (CR 506-511, 802 attack multiple players)
7. Ban list, Brackets 1-5, Game Changers, tutors/MLD/extra turns/2-card combos
8. Oracle text vs printed text; legality fields
9. Budget pricing method (cheapest non-foil paper USD, dated)
10. Deck construction: curve, ramp, draw, removal, finishers
11. Multiplayer politics & threat assessment
12. Forge (Card-Forge) headless sim: `java -jar forge-gui-desktop-*.jar sim -d A.dck B.dck C.dck D.dck -f Commander -n N`; log reading

Every learned rule entry needs: rule number/source, date, one worked example, one adversarial counter-example.

## Quiz format
- 20 questions per unit; >=30% adversarial (trick wording, outdated rules, ban-list changes, house-rule vs official).
- Answer key must cite source + date. Pass: **>=95% (19/20)**. Below: remediation lesson + new quiz (different questions).
- Any incorrect claim in real work → error log + targeted re-test.

## Lesson log
| Date | Agent | Unit | Source+date | Score | Result |
|---|---|---|---|---|---|
| — | — | — | — | — | (none yet) |

## Error log
| Date | Agent/role | Wrong claim | Correct (source) | Remediation | Re-test |
|---|---|---|---|---|---|
| 2026-10-14 | Grok Bot (as Forge) | Draft B included Felidar Guardian with Restoration Angel (2-card infinite) | Known combo; Bracket 2 bars 2-card infinites | Removed pre-audit; added pair to audit_fresh.py | Fresh audit PASS |
| 2026-10-14 | Grok Bot (as Forge) | Drafts included off-colour cards (Lingering Souls B flashback, Moorland Haunt U, Phyrexian Arena, Monastery Mentor, etc.) | Colour identity includes activated/flashback costs (CR 903.4) | check.py caught; swapped | PASS |
| 2026-10-14 | Grok Bot (as Forge) | Draft B had Archaeomancer + Ghostly Flicker (+ Mystic Sanctuary) repeatable loop | Mana-gated loop; cut for Bracket 2 spirit | Removed | PASS |
