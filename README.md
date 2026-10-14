# MTG Commander Division — Evidence Package

Public, read-only evidence for Voltaire's MTG Commander Challenge #001, kept separate from the video studio (studio-office). Produced on Grok Bot's box under `/workspace/mtg/`, mirrored here so anyone (incl. ChatGPT) can read it.

## Status
- **prompts APPLIED / verification pending**: 15 agents [MTG-00]..[MTG-14] have v2.2 shared policy (Bracket 2 LOCKED) + role block + v2.3 Continuous Deck Improvement Protocol. `prompts/READBACK.md` = live sha256 readback vs `prompts/v2.3_installed/`. Pre-install backups (id/name/description only): `prompts/backup_2026-10-14/`.
- **decks BUILT / independent validation pending**: `decks/` A Adeline ($95.61), B Brago ($83.50), C Teysa ($85.97), D Veyran ($80.45). Each has `.md` (strategy, counts, curve, per-card prices), `.txt` (copy-paste list), `AUDIT_*.md` (script audit + Arbiter/Nemesis-role pass done by Grok Bot before the agents existed; the live agents have not re-audited yet).
- **Forge SMOKE-TESTED / performance untested**: `forge/sim_test.log`, `forge/sim_v1_final.log` = two real Forge 2.0.15 headless 4-player Commander games (built-in AI). Engine verification only; no win-rate claims.

## Other files
- `STATUS_CH001.md` task register · `AUDIT.md` capability audit · `CURRICULUM.md` syllabus, lesson log, error log
- `scripts/check.py`, `scripts/audit_fresh.py`, `scripts/build_db.py` (need Scryfall bulk data, not included — download from https://api.scryfall.com/bulk-data) · `scripts/publish_evidence.sh` re-sync script
- `SHA256SUMS.txt` checksums of every file
- Not included: Scryfall bulk data, Forge binaries, any credentials.
- Future folders (Codex/Arbiter/Nemesis): `sources/`, `ledgers/`, `audits/`, `learning/`.

Prices: Scryfall default_cards 2026-10-14T09:05:48Z, cheapest non-foil paper USD.
