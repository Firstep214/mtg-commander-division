# CH001-SRC sources cache — retrieved 2026-10-14 10:56 UTC (18:56 Asia/Manila)
All files fetched with curl into this folder; hashes in SHA256SUMS.

| Source | URL | Local file | Version / effective date |
|---|---|---|---|
| Comprehensive Rules (TXT) | https://media.wizards.com/2026/downloads/MagicCompRules%2020260925.txt (linked from https://magic.wizards.com/en/rules, saved as rules.html) | MagicCompRules_20260925.txt | "effective as of September 25, 2026" |
| Banned & Restricted list | https://magic.wizards.com/en/banned-restricted-list | banned-restricted-list.html/.txt | live page as of retrieval |
| Commander format page (brackets + Game Changers) | https://magic.wizards.com/en/formats/commander | formats_commander.html/.txt | CMS entry updatedAt 2026-04-24; GC colour lists updated 2025-10-22 (U,B,R,Multi,Colorless) and 2026-02-09 (W,G) |
| Commander B&R announcement, Feb 9 2026 | https://magic.wizards.com/en/news/announcements/commander-banned-and-restricted-february-9-2026 | ann_commander_br_2026-02-09.* | effective 2026-02-09 |
| General B&R announcement, Feb 9 2026 | https://magic.wizards.com/en/news/announcements/banned-and-restricted-february-9-2026 | ann_br_2026-02-09.* | 2026-02-09 (non-Commander formats) |
| Commander Brackets beta update, Feb 9 2026 | https://magic.wizards.com/en/news/announcements/commander-brackets-beta-update-february-9-2026 | ann_brackets_update_2026-02-09.* | 2026-02-09 |
| Scryfall bulk default_cards | https://data.scryfall.io/default-cards/default-cards-20261014090548.jsonl.gz | default-cards-20261014090548.jsonl.gz | updated_at 2026-10-14T09:05:48Z (see scryfall_snapshot_state.json) |

Extracted: `banlist.json` (42 named Commander bans + category bans + Lutri companion-only), `game_changers.json` (53 cards, parsed from the live page's embedded list; Scryfall `game_changer` flag cross-check: 53 = 53, identical apart from Tergrid's full DFC name).

## Verification of specifics
- **Lutri banned only as companion — CONFIRMED.** B&R page: "Lutri, the Spellchaser - only banned as a companion." Feb 9 announcement creates the "banned as a companion" designation; Lutri is NOT a Game Changer. Scryfall commander legality: legal.
- **Biorhythm unbanned and now a Game Changer — CONFIRMED.** Feb 9 Commander B&R: "Biorhythm is unbanned… will immediately be put on the Game Changers list." Absent from live Commander ban list; present in live GC list (Green). (Still banned in Oathbreaker.)
- **Farewell added to Game Changers — CONFIRMED.** Brackets update Feb 9 2026 introduces Farewell as a new GC; present in live GC list (White).

## Official policy (Wizards)
- Commander ban list per banlist.json; Lutri companion-only ban.
- Brackets (beta): Brackets 1–2 exclude Game Changers; Bracket 3 up to three; 4–5 unlimited. Brackets also set expectations on two-card infinite combos, extra turns, mass land denial.

## Voltaire house constraints (NOT official policy)
- Deck total ≤ $100 USD (priced per scryfall_snapshot_state.json rule).
- Bracket 2 (locked 2026-10-14) → zero Game Changers.
- No two-card infinite combos.
