# MTG Commander Division — Capability Audit (2026-10-14, 17:40–18:00 Manila)
Auditor: Grok Bot executor. Source: Slack C0C6RUK92Q5 thread 1791969594.215289 (parent + 2 replies). Kept separate from the video studio; no OSL/OOT agent touched.

| Capability | Status | Evidence |
|---|---|---|
| Persistent independent agents | **LIVE** — 15 agents [MTG-00]..[MTG-14] exist, created 2026-10-14 by the Studio Manager via CreateAgent | Manager confirmation (CreateAgent) |
| Naming / department tags `[MTG-##] Name \| Dept \| Role` | LIVE (name strings) | Used in agents, prompts/, office |
| Role prompts | **APPLIED** (v2.2 + v2.3) | prompts/v2.3_installed/; READBACK.md 15/15 match |
| Scryfall data | **LIVE** on box | data/oracle.jsonl.gz (updated 2026-10-14T09:01:55Z = 17:01 Manila), data/default.jsonl.gz (09:05:48Z = 17:05 Manila); carddb.json 35,335 names, 53 Game Changers flagged. Shared to any agent on this box (shared filesystem). Refresh: build_db.py |
| Slack orchestration | LIVE connector (user-Slack read/send). Outgoing posts still need Voltaire's approval card | Read the request thread successfully |
| Java | **LIVE** — installed openjdk-21-jre-headless (21.0.12.1) this session (17 not available on Debian 13) | `java -version` |
| Forge engine (Card-Forge) | **LIVE, headless sim works** — forge-2.0.15 (released 2026-09-28) at forge/app | `java -Djava.awt.headless=true -jar forge-gui-desktop-2.0.15-jar-with-dependencies.jar sim -d A.dck B.dck C.dck D.dck -f Commander -n 1 -c 600` ran a real 4-player Commander game; logs forge/sim_test.log, forge/sim_v1_final.log. Decks must sit in ~/.forge/decks/commander/ |
| Hidden information | Engine-enforced for Forge AI (AI players see only their own hands) | Forge design; not separately tested |
| Persona-driven players (Kael/Nyx/Vex/Thorne piloting) | **PLANNED** — Forge sim uses Forge's built-in AI, not the agents. Agents can only pick decks/seats and analyse logs | Blocker |
| Ongoing autonomous learning | PLANNED — only when an agent actually runs; curriculum logs are empty except real build errors | CURRICULUM.md |
| Win-rate stats | NOT STARTED — 2 smoke games only, no statistical claims | — |

## Blockers
1. v2.3 prompts APPLIED by Studio Manager (prompts/READBACK.md 15/15 match); verification pending.
2. RESOLVED: Bracket 2 LOCKED by Voltaire 2026-10-14 (Slack ts 1791973731.389819); zero GC, no 2-card infinites, 3-card combos only if disclosed.
3. Forge AI ≠ named player agents; persona play needs custom tooling (no Forge API for external decision-making found in this audit).
4. Official CR / ban-list documents not yet downloaded into data/ (Codex task); Scryfall legality field used meanwhile.
5. Prices move daily; Deck A has only $4.39 headroom.

## Deploy steps / owners
| # | Task | Owner |
|---|---|---|
| 1 | Approve 4 V1 decks (Bracket 2 already locked) | Voltaire |
| 2 | Install prompts MTG-00,02,04,07,08 first, then rest | Studio Manager (UpdateAgent) |
| 3 | Download CR + Commander ban list/bracket docs, dated | MTG-02 Codex |
| 4 | Re-run audit_fresh.py independently on V1 | MTG-07 Arbiter, MTG-08 Nemesis |
| 5 | Rotating-seat plan: 4 decks × 4! seat orders, N≥10 games each, via `forge sim` | MTG-14 Sentinel |
| 6 | Analyse logs, report win rates with sample size | MTG-09 Oracle |
| 7 | Run first curriculum quiz (≥95%) | MTG-00 Magnus |
