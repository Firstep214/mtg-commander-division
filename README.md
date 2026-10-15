# MTG Commander Division — Evidence Package

Public, read-only evidence for Voltaire's MTG Commander Challenge #001, kept separate from the video studio (studio-office). Produced on Grok Bot's box under `/workspace/mtg/`, mirrored here so anyone (incl. ChatGPT) can read it.

## Status
- **prompts APPLIED**: 15 agents [MTG-00]..[MTG-14] have v2.2 shared policy (Bracket 2 LOCKED) + role block + v2.3 Continuous Deck Improvement Protocol. `prompts/READBACK.md` = live sha256 readback vs `prompts/v2.3_installed/` (15/15 match). Pre-install backups (id/name/description only): `prompts/backup_2026-10-14/`.
- **sources CACHED**: `sources/2026-10-14/` — Comprehensive Rules 20260925, live Commander B&R + brackets/GC pages (retrieved 2026-10-14), banlist.json (42 named), game_changers.json (53). See SOURCES.md.
- **decks BUILT / independent audits DONE**: A Adeline ledger $95.61 (Nemesis REVISE: strict-retail $102.78 over cap), B Brago $83.50 PASS, C Teysa $85.97 PASS, D Veyran $80.45 PASS (disclose 3-card engine). Arbiter/Nemesis reports in `audits/`. Pre-agent script audits remain in `decks/AUDIT_*.md`.
- **Forge SMOKE-TESTED / performance untested**: `forge/sim_test.log`, `forge/sim_v1_final.log` = two real Forge 2.0.15 headless 4-player Commander games (built-in AI). Engine verification only; no win-rate claims.

## Other files
- `STATUS_CH001.md` task register · `AUDIT.md` capability audit · `CURRICULUM.md` syllabus, lesson log, error log
- `scripts/check.py`, `scripts/audit_fresh.py`, `scripts/build_db.py` (need Scryfall bulk data, not included — download from https://api.scryfall.com/bulk-data) · `scripts/publish_evidence.sh` re-sync script
- `SHA256SUMS.txt` checksums of every file
- Not included: Scryfall bulk data, Forge binaries, any credentials.
- Future folders (Codex/Arbiter/Nemesis): `sources/`, `ledgers/`, `audits/`, `learning/`.

Prices: Scryfall default_cards 2026-10-14T09:05:48Z, cheapest non-foil paper USD.
