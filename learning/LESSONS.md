# CH001-LEARN-01: LESSONS.md, a play guide for Decks A–D
Author: Sage (MTG-01) · 2026-10-15 (PHT)
Sources (only these): learning/{A,B,C,D}_ANALYSIS.md, decks/*.txt, forge/PLAYTEST_BATCH1.md, forge/PLAYTEST_BATCH2.md (the batch logs live in forge/playtest_batch1/, forge/playtest_batch2/).
Every number below is quoted from those analyses. Game ids are Batch 2 (gNN) unless they are marked rot*. Pilots were Forge AI vs AI, n=50 in B2 (about ±14 pp per deck). Card-level splits are correlations, not causes.
**All 8 card swaps: Verified (SWAP_VERIFICATION.md); being applied as new deck versions by Forge.** Arbiter's checks (legality, colour identity, Game Changer, 2-card infinite, extra turns/MLD) all PASS. The swaps have not been playtested yet (Batch 3).

## Cross-deck caveats (apply to every section)
- The logs record no hands or draws. "Never cast" does not mean "never drawn", so mulligan guidance comes only from mulligan counts and land/cast timing.
- The log `Turn:` counter is 2× the report's "Turns" value (A §9, B method notes). Turn figures are not comparable across the two.
- AI TimeoutExceptions degraded g18, g28, g43 and g44 (A §9, C §9).
- Table dynamics: A11 is the table's main killer. It won 20 of B's 41 losses, 20 of C's 38 and 20 of D's 41. Every non-A deck should save sweepers and interaction for Adeline's board.

---
## Deck A: Adeline, Resplendent Cathar tokens (V1.1, decks/A_tokens_V1.1.txt)
Record: 30/74 (B1 10/24, B2 20/50). Strongest deck. (A §1)

**Game plan.** Go wide with Adeline, token makers and anthems, then alpha strike. Examples: g05 (Increasing Devotion then a 15+ Human token attack, l.1666/1701) and g40 (Intangible Virtue then Adeline + 5 Angel tokens, l.1148/1152). Recast Adeline through commander tax: she was cast in 74/74 games, 8 times in g28 (W) and 6 in g32 (W). (A §2)

**Mulligan / opening.**
- Keep 7 when you can. With any mulligan A won 4/16, against 26/58 without one. All 4 games that went to 6 cards were losses (incl. g03, g10). (A §6)
- Curve out. Adeline on own turn ≤3 went 9/18 across all games, and on turns 5–6 went 2/18. Late-cast wins (7+: 13/22) come from long games. Small n. (A §6)
- Going first matters most for A: 8/12 when first vs 12/38 otherwise in B2 (wins g05 g18 g21 g24 g28 g38 g49 g50). (A §2)

**Key cards & sequencing.** Higher-than-baseline win share (correlational): Collective Effort, Increasing Devotion, Cathars' Crusade, Hero of Bladehold, Benalish Marshal, Captain of the Watch, Dictate of Heliod, Hallowed Spiritkeeper, Path to Exile, Loran, Generous Gift, Jazal Goldmane (A §4). Sequence token makers, then the anthem or Crusade, then attack (g05, g40). Hold Path, Generous Gift and Loran for evasive commanders. Don't sweep your own board: Wrath was already cut in V1.1, and Sunfall has the same anti-synergy (A §5).

**Threats & how to play around them.** (A §3, §7)
1. B Brago: 785 damage to A by active player and 22 A eliminations. Flyers + blink, and ground tokens can't block them (g13 l.1898–1905; g02 Soldier swarm). Point removal at Brago and at the flyers.
2. D Veyran: Veyran is the biggest single damage source (260), plus Haughty Djinn 130 and Guttersnipe pings that can't be blocked (g19). Kill pingers on sight.
3. C Teysa: wins 16 of A's losses through drain (g22 Syr Konrad → Butcher). Close the game before drain accumulates.
- Common thread: A dies to evasive or non-combat damage. All 44 losses were "life total reached 0".

**Swaps (Verified (SWAP_VERIFICATION.md); being applied as new deck versions by Forge).** −Sunfall → +Ghostly Prison. −Mirror Entity → +Get Lost. The alternative is −Unbreakable Formation. All three cuts had 0 casts in 74 games. Post-swap total is $102.19 ledger / $106.87 strict retail (SWAP_VERIFICATION.md, recomputed totals). **Voltaire approved Deck A up to $106.87 strict retail on 2026-10-15.** (A §8)

**Gaps.** No standalone V1.1 price ledger (totals come from SWAP_VERIFICATION.md). Turn-counter mismatch. No hand/draw data.

---
## Deck B: Brago, King Eternal control (V1, decks/B_control.txt)
Record: B2 9/50 (g02 g03 g07 g13 g25 g33 g41 g42 g47). B1 6/24 is from the report only, because the B1 logs were not re-parsed. (B Record)

**Game plan.** Survive to a long game, resolve big ETB/flicker threats and blink them with Brago. Wins ended on report turns 24–36. B cast 28.0 spells per game in wins vs 17.3 in losses, so B loses when it dies before its engine takes over. (B Record, Why B lost)

**Mulligan / opening.**
- Land count is not the separator: B had 4 lands by turn 4 in 8/9 wins and 36/41 losses. B mulled to 6 only in g13 and g47 and won both, so a mulligan is not a death sentence. (B Mulligan)
- Prioritize early interaction and card flow, since the losses were throughput losses. First seat: 4/9 wins (g02 g07 g25 g47) vs 5/41 otherwise.

**Key cards & sequencing.** Brago (9/9 wins), Angel of Serenity (8/9), Fact or Fiction, Venser and Path (7/9 each), then Frost Titan, Agent of Treachery, Restoration Angel, Banishing Light, Mind Stone and Frantic Search (6/9 each). Protect Brago once he sticks: wins mostly had 1–3 casts, while losses often needed 3+ casts (up to 6). Get him attacking with ETB creatures and blink targets in play. (B Why B won, Key cards)
- Sweepers alone don't convert: Wrath 3W/15L, Supreme Verdict 1W/9L, Austere Command 0W/10L. A11's tokens rebuild. After sweeping, have a follow-up threat or card draw ready. (B Dead cards)

**Threats & how to play around them.** (B Threat assessment)
1. A11 tokens: won 20 of B's 41 losses, and a token was the lethal source in 26/41 (Human tokens in g04 g06 g12 g14 g21 g28 g32 g38 g49). Save sweepers for after A commits anthems, and keep blockers back.
2. D burn: 631 nontoken damage to B, the most of any source. Guttersnipe lethal in g11 and g29, Electrostatic Field in g10 and g44. Counter or kill pingers and don't rely on blockers.
3. C drain: kills on B's own turn (g09, g22, g35). Life total matters, so avoid paying life loosely.

**Swaps (Verified (SWAP_VERIFICATION.md); being applied as new deck versions by Forge).** −Conjurer's Closet → +Fumigate. −Mystic Confluence → +Settle the Wreckage (Bracket fit needs an auditor). Both cuts were never cast. Projected $80.48. (B Swaps)

**Gaps.** B1 logs not re-parsed. Drain life loss is not attributed to a source. Turn-counter ×2.

---
## Deck C: Teysa Karlov aristocrats (V1, decks/C_aristocrats.txt)
Record: B2 12/50 (g09 g14 g16 g20 g22 g23 g26 g27 g31 g35 g37 g43). B1 4/24 (report only). (C §1)

**Game plan.** Go long and let the death-trigger/drain engine (doubled by Teysa) finish. In all 12 wins the final life loss came from that engine: Zulaport (g14, g43), Vindictive Vampire (g20, g31, g37), Falkenrath Noble + Cruel Celebrant (g09), Syr Konrad (g27), Ministrant sac chain (g35), Spirit/Nightblade attacks (g16, g23, g26). C had more own turns in wins (16.8 vs 13.7) and cast more spells (22.9 vs 15.6). (C §1–2)
- g22 (corrected): B died on its own turn to **C's Liesa, Shroud of Dusk** ("Whenever a player casts a spell, they lose 2 life"). It was not a B card: no such effect is in decks/B_control.txt. In the g22 log, Liesa triggers on B's Thought Vessel and Spell Queller took B 8→6→4. Then on B's last turn, casting Brago + Brainstorm took B 4→2→0 (log lines ~1229–1245), after Liesa + Butcher combat had taken B 18→8 (l.1149). Lesson: with Liesa out, opponents at low life are taxed out of casting.

**Mulligan / opening.**
- Mulligan data is thin: C won 2 of 10 mulligan games (g09, g14) vs 10/40 without. Mana screw is not the main failure mode (45/50 games had 4+ lands by turn 4). (C §6)
- Don't rush Teysa. The first-cast mean was turn 6.33 in wins vs 5.17 in losses, so early Teysa alone doesn't win. Set up sac outlets and payoffs first. She was cast in all 12 wins. (C §4)
- Going first helps: 6/15 vs 6/35.
- The fast losses were undeveloped games (g04, g17, g29). Prioritize early board presence. (C §3)

**Key cards & sequencing.** Payoffs that closed games: Zulaport, Vindictive Vampire, Falkenrath Noble, Cruel Celebrant, Syr Konrad. Above-base-rate cards (small n): Utter End, Victimize, Path, Kaya's Guile, Ashnod's Altar, Midnight Reaper, Dark Prophecy, Liesa, Elenda, Spectral Procession. The engines with the most triggers were Elenda, Bastion of Remembrance and Dark Prophecy. (C §2, §4)
- **Turn off the Dark Prophecy risk at low life.** In g45, C died to its own Dark Prophecy triggers (2→1→0). (C §3)

**Threats & how to play around them.** (C §7)
1. A11 tokens: 20/38 losses. Single tokens dealt 18–26 damage (g05 g06 g08). Spot removal doesn't stop a wide board, so hold Damn and Kaya's Guile for it, and kill Adeline or the anthems early.
2. B Brago: flyers + flicker. Agent of Treachery stole Carrion Feeder (g25). Keep removal for Agent and Brago.
3. D Veyran: pings finish C at low life (g10 Niv-Mizzet, g36 Thermo-Alchemist, g44 Kessig). Keep a life buffer.

**Swaps (Verified (SWAP_VERIFICATION.md); being applied as new deck versions by Forge).** −Wake the Dead → +Massacre Wurm. −Sevinne's Reclamation → +Pestilence. Per Arbiter (SWAP_VERIFICATION.md), it is a mana-limited drain engine: each activation costs {B} and C has no infinite black mana, so with Teysa, Blood Artist and Bastion it is a strong but finite drain. It also hits C's own small creatures, which is an AI misuse risk. Both cuts were never cast. Projected $87.08. (C §8)

**Gaps.** The parser and its output sit outside learning/ (/workspace/c_parse.py, /workspace/c_parsed.json). B1 logs not re-parsed. Elimination order can't be measured. Token controllers are inferred.

---
## Deck D: Veyran, Voice of Duality spellslinger (V1, decks/D_spellslinger.txt)
Record: B2 9/50 (g10 g15 g17 g19 g29 g36 g39 g44 g45). B1 4/24 (rot1_g6, rot2_g1, rot3_g5, rot4_g2). (D §1)

**Game plan.** Assemble a "whenever you cast" pinger next to Veyran and chain cheap spells. In 7/9 wins the top damage source was a pinger: Guttersnipe (g19, g29, g45), Kessig Flamebreather (g36, g44), Electrostatic Field (g10, g17, g44), Thermo-Alchemist (g17), Niv-Mizzet (g10). Only g15 and g39 were combat wins. Spells cast: 31.3 per game in wins vs 20.1 in losses, with lands about equal. (D §2)

**Mulligan / opening.**
- No useful mulligan data: there was 1 mulligan in 50 games (g43, kept 6, lost). (D §6)
- The opening isn't the differentiator (first spell came on turns 1–4 in all games). Veyran's timing doesn't separate wins from losses either. Keep hands with cantrips and a path to a pinger. Going first didn't help: 4/14. (D §4, §6)

**Key cards & sequencing.** The pinger package (Guttersnipe, Kessig, Electrostatic Field, Thermo-Alchemist, Firebrand Archer, Niv-Mizzet). Play the pinger, then chain spells with Veyran out. Guttersnipe was cast in 3/9 wins but only 2/41 losses. Sweepers vs A11: Anger of the Gods (5/11 cast-games won), and Blasphemous Act with Veyran in g10 (l.452–456). Most-cast cards: Reality Shift, Fire // Ice, Fact or Fiction, Expressive Iteration, Arcane Denial. (D §2, §4)

**Threats & how to play around them.** (D §3, §7)
1. A11 tokens: killed D in 20/41 losses, last hits from A11 tokens in g05 g11 g12 … g50. Hold cheap sweepers (Anger, Act) for the token board, and keep the pinger alive after the sweep.
2. B Brago: 11 kills through evasive value (Glen Elendra in g01 g33 g47, Brago in g06 g37, Bird Illusions in g25 g42). Counters slow D's engine, so bait them first.
3. C drain: 9 kills (Zulaport g43, Vindictive Vampire g31, Nightblade g23/g26).

**Swaps (Verified (SWAP_VERIFICATION.md); being applied as new deck versions by Forge).** −Mizzix's Mastery → +Fiery Cannonade (it also kills D's own x/2 pingers). −Past in Flames → +Coruscation Mage. Both cuts were never cast. Projected $76.76. (D §8)

**Gaps.** Forge AI likely undervalues Past in Flames, Faithless Looting, Mizzix's Mastery and Reverberate. Elimination turn is approximated. Swaps are untested.

---
## Doc-level gaps
- No standalone V1.1 ledger for A (post-swap totals are in SWAP_VERIFICATION.md). B1 logs were parsed only for A. C's parser lives outside learning/.
- All guidance comes from AI-vs-AI games, and human piloting may differ (especially for D's graveyard cards).
