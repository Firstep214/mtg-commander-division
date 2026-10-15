# Deck A (Adeline tokens, V1.1) — Playtest Analysis (CH001-LEARN-01)
Author: Kael · 2026-10-15 (PHT) · Deck file NOT modified.
Sources: forge/PLAYTEST_BATCH1.md, forge/PLAYTEST_BATCH2.md, PLAYTEST_RULES.md (at /workspace/mtg/PLAYTEST_RULES.md, not forge/), forge/playtest_batch1/rot*_g*.log (24), forge/playtest_batch2/g01–g50.log (50), decks/A_tokens_V1.1.txt, decks/A_tokens_V1.1_CHANGELOG.md, decks/PRICE_LEDGER_A_tokens.md, data/default.jsonl.gz (Scryfall snapshot 2026-10-14).
Every number below was computed by `learning/a_stats.py` (output: `a_stats.txt`, per-game JSON: `a_stats.json`) by regex over log lines:
`Game Result: ... Ai(n)-X has won`, `Game Outcome: Ai(n)-A11 has lost because ...`, `Mulligan: Ai(n)-A11 ...`, `Add To Stack: Ai(n)-A11 cast <card>`, `Damage: <src> (id) deals N ... damage to Ai(n)-A11.`, `Turn: Turn N (Ai(n)-X)`.
Caveat: Forge AI vs AI; samples small (batch reports quote ±10–14 pp). "Cast in W/L games" counts are correlational (a card cast more in long games looks better/worse for reasons unrelated to the card).

## 1. Results
| Batch | Games | A11 wins | Source |
|---|---|---|---|
| 1 (random start) | 24 | 10 | matches PLAYTEST_BATCH1.md |
| 2 (d20 seating) | 50 | 20 | matches PLAYTEST_BATCH2.md |
| Total | 74 | 30 (40.5%) | 30/74 |
Batch 2, A11 went first in 12 games, won 8 (g05,g18,g21,g24,g28,g38,g49,g50 W; g31,g33,g39,g44 L) — matches report. Not first: 12/38.
Winners of the 44 games A lost: C 16, B 15, D 13 (B1: B6 C4 D4; B2: C12 B9 D9).
All 44 A11 eliminations: "life total reached 0" (no decking/poison/concede).

## 2. Why it wins (evidence)
- Wide alpha strikes snowballing off Adeline + token makers + anthems. g05 (A11 won, first player): line 1701 "Ai(4)-A11 assigned Knight of the White Orchid, Human Token ×15, Servo Token ×3, Inspiring Overseer … to attack Ai(3)-D" right after line 1666 "A11 cast Increasing Devotion".
- g40 (shortest B2 game, Game Outcome Turn 17): line 1152 "A11 assigned Adeline, Angel Token ×5 and Resolute Reinforcements to attack Ai(1)-B" following "cast Intangible Virtue" (l.1148).
- Adeline resilience: she was cast in 74/74 games, and re-cast after removal often (Batch 2 cast lines per game range 1–8, e.g. g28: 8 casts, A won; g32: 6, won). Commander tax recasting is the deck's main engine.
- Going first matters most to A: 8/12 (67%) when first vs 12/38 (32%) otherwise in Batch 2.

## 3. Why it loses (evidence)
Damage dealt TO A11 by source, all 74 games (top): Veyran 260, Brago 239, Haughty Djinn 130, Soldier Token 90, Spirit Token 71, Yahenni 58, Restoration Angel 57, Teysa Karlov 56, Angel of Serenity 55, Dream Trawler 48.
Damage to A11 by active player: B 785, D 643, C 420. A11 eliminated during turn of: B 22, D 9, C 8, A11 5 (own-turn deaths = drain/trigger damage).
- Evasive/flying commander beats: g13 l.1898–1905 "Brago deals 2 … Spell Queller deals 2 … Mulldrifter deals 2 … Life: A11 11 > -3". g02 l.1345 "Life: A11 11 > -7" from a Soldier Token swarm on B's turn.
- Non-combat burn/drain A can't block: g19 l.829–865 "Guttersnipe deals 2 non-combat damage … A11 1 > -1" (D win); g22 l.900–931 Syr Konrad drain then "Butcher of Malakir deals 5 combat … A11 5 > 0" (C win).
- Pattern: A has no way to stop flyers/unblockable commanders hitting it while it goes wide; ground chump-blocks don't cover Brago/Veyran/Djinn.

## 4. Key cards (cast-in-W vs cast-in-L counts, 30 W / 44 L games; correlational)
Higher W-share than baseline 30:44: Collective Effort 13/5, Increasing Devotion 12/5, Cathars' Crusade 12/6, Hero of Bladehold 11/5, Benalish Marshal 10/5, Captain of the Watch 13/8, Dictate of Heliod 9/4, Hallowed Spiritkeeper 9/5, Path to Exile 11/7, Loran 11/7, Generous Gift 11/7, Jazal Goldmane 13/10.
Commander: Adeline (always cast).

## 5. Dead / weak cards
- Never cast in 74 games: **Sunfall, Mirror Entity, Unbreakable Formation** (0/0). Lands Castle Ardenvale, Emeria, Secluded Steppe were played (checked "A11 played <land>" lines) — not dead.
- Data gap: logs don't show hands/draws, so "never cast" ≠ "never drawn"; the AI may have held them. Sunfall is also the same self-sweeper anti-synergy that got Wrath of God cut in V1.1.
- Low W-share: Sigil of the Empty Throne 3/12, Wayfarer's Bauble 5/16, Return to Dust 5/13, Skullclamp 7/14, Arcane Signet 3/8, Gift of Estates 4/8, Tocasia's Welcome 4/9. Confounded by game length; not proof of weakness.

## 6. Mulligans / openings
- A mulliganed (any "mulliganed down to" line) in 16/74 games, won 4 (B1: 3 games, 0 wins; B2: 13 games, 4 wins) vs 26/58 without mulligan. Went to 6 cards in 4 games (B1 2, B2 g03,g10) — all losses.
- Adeline cast on A's own turn N (Batch 2): T≤3: 14 games/7 wins; T4: 11/5; T5–6: 10/0; T7+: 15/8. All 74: ≤3 18/9, 4 16/6, 5–6 18/2, 7+ 22/13. Non-monotonic → curving out early helps, but late-cast wins come from long games; small n.

## 7. Threat assessment
1. B Brago (control/flyers): most damage to A by active player (785) and most A eliminations (22). Flyers + blink; A's ground army can't block.
2. D Veyran: single biggest damage source (Veyran 260, Haughty Djinn 130) plus non-combat Guttersnipe pings (g19).
3. C Teysa: wins the most games A loses (16) via drain (Syr Konrad, Yahenni, Butcher) — damage A can't block.
Common thread: evasive or non-combat damage; A lacks pillowfort/flyer defense and cheap flexible removal.

## 8. Swap proposals (max 2, one-for-one, NOT applied)
Prices: Scryfall snapshot data/default.jsonl.gz (2026-10-14), cheapest non-foil USD printing (same method as PRICE_LEDGER). game_changer=false and commander=legal from same data. Not re-verified live; strict-retail prices unverified.
1. **−Sunfall (+$0.31) → +Ghostly Prison ($5.68, PLST)**. Reason: Sunfall was never cast in 74 games and exiles A's own tokens; Ghostly Prison taxes the creature attacks that dealt most damage to A (Brago 239, Veyran 260, Djinn 130). Net +$5.37.
2. **−Mirror Entity ($1.01) → +Get Lost ($3.22, LCI)**. Reason: Mirror Entity never cast in 74 games; Get Lost is 2-mana instant-speed removal for a creature/enchantment/planeswalker (Veyran, Brago, Guttersnipe, Teysa). Net +$2.21.
Rule v2.3 check: neither is a Game Changer (snapshot flag false); no 2-card infinite introduced (pillowfort + removal, no combo pieces); Bracket 2 appropriate.
Budget: ledger V1 $95.61 → V1.1 (−Wrath $1.03 +Inspired Charge $0.03) = $94.61 → with both swaps $102.19 (ledger basis). Changelog quotes V1 strict retail $102.78; V1.1 never re-priced, so strict-retail total with swaps is unverified. Needs Voltaire OK for "slightly over".
Alternative if budget is tight: −Unbreakable Formation (also 0 casts, $0.75) instead of Mirror Entity.

## 9. Data gaps / anomalies
- PLAYTEST_RULES.md is at /workspace/mtg/PLAYTEST_RULES.md (not forge/).
- "Game Outcome: Turn N" equals ~half the last `Turn: Turn N` line in the logs (e.g. g05: Outcome Turn 28, last log turn 56). Batch reports' "Turns" use the Outcome value, so "global counter" may actually be rounds×2 or similar — worth checking before using turn stats.
- Hands/draws not logged → cannot measure dead-in-hand, only never-cast.
- AI TimeoutExceptions degraded a few games (B1 rot1_g1/g3; B2 g18,g28,g43,g44).
- V1.1 has no price ledger.
