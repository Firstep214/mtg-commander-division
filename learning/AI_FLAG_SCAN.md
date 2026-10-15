# AI_FLAG_SCAN (CH001-LEARN-03)

Scanned decks: decks/A_tokens_V1.2.txt, decks/B_control_V1.3.txt, decks/C_aristocrats_V1.3.txt, decks/D_spellslinger_V1.3.txt (not the *_PENDING files).
Card scripts: forge/app/res/cardsfolder/cardsfolder.zip (Forge 2.0.15; paths below are inside the zip, line = line in the card script).
Cast counts are the number of games (out of 200) in which the deck cast the card. A12 uses batch 4. B13/C13/D13 use batch 5 (forge/playtest_batch5, the V1.3 lists). Batch 4 ran V1.1 for B/C/D, so I used batch 5 for those three decks. Lands are never "cast", so for lands I counted plays and mana use.

## Verdict
1. **`AI:RemoveDeck:All` = the AI will never cast or activate that card's spells/abilities, but the card is not stripped from the deck at load.**
   - Forge source, AiController.getSpellAbilityToPlay() (forge-ai/.../AiController.java, ~L1517-1571 on current master): `saList.removeIf(... ComputerUtilCard.isCardRemAIDeck(spellAbility.getHostCard()))`, with the comment "don't include removedAI cards".
   - ComputerUtilCard.isCardRemAIDeck() returns `getAiHints().getRemAIDecks()`, which is the RemoveDeck:All flag only.
   - The 2.0.15 jar we run has the same references. forge/ai/AiController.class and forge/ai/ComputerUtilCard.class both contain RemAIDeck symbols. I couldn't decompile it (no javap on the box).
   - Mana abilities go through a separate path, so a flagged land is still played and still taps for its plain {T} ability.
2. **No stripping at deck load in our mode.** Our mode is the headless `sim -d X.dck`, forge.view.SimulateMatch.
   - SimulateMatch has no RemAIDeck or unplayable-card handling (I checked both the class strings and the source).
   - The other uses of getRemAIDecks are for the GUI warning (VLobby, Deck$UnplayableAICards), random/themed deck generators, and PlayerControllerAi's sideboard plan (pca L156). None of them apply here.
   - Log evidence: two flagged cards show up in play constantly.
     - Skycloud Expanse (RemoveDeck:All): played in 58/200 batch 4 games (e.g. playtest_batch4/g194.log:1326) and in 62 batch 5 logs. It has 0 `Mana: Skycloud Expanse` lines; its only ability is {1},{T}, so it's a dead land.
     - Fetid Heath: played in 55 batch 5 logs, and 204 of its mana lines are all `{T}: Add {C}`. Its {W/B} filter was never used.
   - The .dck files match the deck lists exactly (C13.dck vs ~/.forge copy: identical).
3. **Toxic Deluge is confirmed flagged** (t/toxic_deluge.txt:6 `AI:RemoveDeck:All`). It was cast 0/200 in batch 5, with 0 log mentions at all. That fits: it's never cast, and in those 200 games it was never one of the 93 C13 hand-size discards. By comparison, Massacre Girl shows in 22 logs and Go for the Throat in 43. The guild Signets (also RemoveDeck:All) behaved the same way in batch 4 (SIGNET_CHECK.md).
4. **`AI:RemoveDeck:Random` and `NonCommander` cards play normally.** Those flags only affect random deck generation and non-Commander formats. Darkest Hour 48, Living Death 48, Frantic Search 49/61, Rally the Ranks 58, Soulherder 59, Haughty Djinn 57, and so on. `SVar:PlayMain1`, `NeedsToPlay` and `AIPreference` are play-pattern hints, not avoid flags.

## Flagged cards that matter (RemoveDeck:All)
| Deck | Card | Script (cardsfolder.zip) | Flag | Cast/use |
|---|---|---|---|---|
| A12 | none | - | - | - |
| B13 | Skycloud Expanse | s/skycloud_expanse.txt:5 | AI:RemoveDeck:All | played often, never tapped for mana |
| C13 | Toxic Deluge | t/toxic_deluge.txt:6 | AI:RemoveDeck:All | 0/200 cast (batch 5) |
| C13 | Fetid Heath | f/fetid_heath.txt:6 | AI:RemoveDeck:All | played, filter never used (only {T}: Add {C}) |
| D13 | none | - | - | - |

## Other AI hints (informational, not avoided)
- RemoveDeck:Random: Intangible Virtue i/intangible_virtue.txt:6 (A, 46); Rally the Ranks r/rally_the_ranks.txt:7 (A, 58); Archivist of Oghma a/archivist_of_oghma.txt:9 (A, 40); Loran of the Third Path l/loran_of_the_third_path.txt:9 (A, 52); Soulherder s/soulherder.txt:12 (B); Frantic Search f/frantic_search.txt:8 (B, D); Darkest Hour d/darkest_hour.txt:6 (C); Living Death l/living_death.txt:8 (C); Haughty Djinn h/haughty_djinn.txt:10 (D). All of them are cast regularly.
- RemoveDeck:NonCommander (harmless in Commander): Arcane Signet a/arcane_signet.txt:5, Commander's Sphere c/commanders_sphere.txt:6, Command Tower c/command_tower.txt:5.
- Play hints: SVar:PlayMain1, NeedsToPlay, AIPreference, AIPriorityModifier (Galvanic Iteration g/galvanic_iteration.txt:7) on many cards. These shape timing, not whether a card gets played.
- Reproduce with /tmp/scan.py (it unzips the cardsfolder to /tmp/cf).

## Suggested sim-only replacements (recommendations only; need Arbiter/Nemesis price and bracket verification)
Prices are approximate and unverified. Target: no net budget increase, stay within the $100 aim / $120 cap, Bracket 2, no Game Changers, no 2-card infinites. Check each replacement's own script for RemoveDeck:All before adopting it.
- C13 Toxic Deluge -> **Damn** (BB, wrath / overload) or **Crux of Fate**. Both scripts carry no AI: flag (checked), cost a few dollars, and aren't Game Changers. A lower-priority option is Kaya's Guile (not a sweeper).
- C13 Fetid Heath -> **Orzhov Guildgate** or **Silent Clearing** (both unflagged). Or simply a Plains/Swamp.
- B13 Skycloud Expanse -> **Azorius Guildgate** (unflagged), or a basic Island/Plains.
- Paper lists can keep the originals. These swaps only stop the sims from undercounting B and C because of dead cards.
