# WINOTA_VERIFICATION: E_winota_V1.0_SUBMITTED.txt (Arbiter, 2026-10-15 PHT)
Scripts: learning/arbiter_winota/ (forge_and_price.py, repl.py, forge_price.json, plus the full audit via audits/arbiter_scripts/audit.py). The submitted deck file was not edited. Checks ran on a scratch copy (decks/E_clean.txt) with only the " (Commander)" tag removed from line 1.

## Verdict: **FAIL** (Forge AI flags only). The deck PASSES every rules, Bracket 2 and budget check.

## Winota Game Changer check (done first)
- **game_changers.json** (retrieved 2026-10-14 10:56:58Z = 18:56 PHT; Wizards per-colour lists updated 2025-10-22 for Multicolor): Winota, Joiner of Forces is **not listed**. The full list has 53 cards.
- **Scryfall `game_changer` flag** (default_cards bulk 2026-10-14 09:05Z = 17:05 PHT): **false**.
- **Result: Winota is not a Game Changer per the provided files.**
- Winota appears in the sources only as **banned in Pioneer** (banned-restricted-list.txt L485) and in a Historic note (ann_br_2026-02-09.txt L1060). She is not on the Commander ban list. Scryfall commander legality: legal.

## Checks
| Check | Result | Evidence |
|---|---|---|
| Card names resolve | PASS, with a format note | Line 1 `1 Winota, Joiner of Forces (Commander)` does not resolve as written: the " (Commander)" tag is not part of the card name. Everything resolves once the tag is stripped. The tag can break parsers that expect plain names |
| 100 cards / singleton (CR 903.5a/b) | PASS | 100 total (8 Mountain at L45, 14 Plains at L56); no duplicates |
| Commander (CR 903.3) | PASS | Legendary Creature — Human Warrior; legal; no partner ability |
| Colour identity RW (CR 903.4/903.5c) | PASS | 0 off-colour cards |
| Bans | PASS | None in banlist.json and none not-legal on Scryfall |
| Game Changers, all 100 cards (json + Scryfall flag) | PASS | 0 |
| 2-card infinites | PASS | None from the known-pair list or manual review. Zealous Conscripts is present, but no Kiki-Jiki or Felidar Guardian partner is |
| Extra turns / MLD | PASS | None. Blasphemous Act and Vanquish the Horde hit creatures; Wear // Tear and Generous Gift are single-target |
| Price | PASS | Ledger **$87.43**, strict retail **$87.92**: under the $100 target and well under the $120 cap. All 100 cards priced |

## Forge `AI:RemoveDeck` scan (all cards; forge/app/res/cardsfolder/cardsfolder.zip)
| Line | Card | Script | Exact line | Assessment |
|---|---|---|---|---|
| L13 | Boros Signet | b/boros_signet.txt | `AI:RemoveDeck:All` | **FAIL**: the AI never casts it (the same issue as the guild Signets in SIGNET_CHECK) |
| L47 | Odric, Master Tactician | o/odric_master_tactician.txt | `AI:RemoveDeck:All` | **FAIL** |
| L3 | Angrath's Marauders | a/angraths_marauders.txt | `AI:RemoveDeck:Random` | **FAIL under the "any RemoveDeck flag" rule (LEARN-03)**. :Random only excludes the card from Forge's random deck generation. The AI does play it |
| L5 | Archon of Emeria | a/archon_of_emeria.txt | `AI:RemoveDeck:Random` | as above |
| L10 | Bomat Courier | b/bomat_courier.txt | `AI:RemoveDeck:Random` | as above |
| L40 | Loran of the Third Path | l/loran_of_the_third_path.txt | `AI:RemoveDeck:Random` | as above. Note: Deck A also runs Loran |
| L4 | Arcane Signet | a/arcane_signet.txt | `AI:RemoveDeck:NonCommander` | OK in Commander (the AI casts it; see SIGNET_CHECK) |
| L20 | Command Tower | c/command_tower.txt | `AI:RemoveDeck:NonCommander` | OK in Commander |
| L51 | Path of Ancestry | p/path_of_ancestry.txt | `AI:RemoveDeck:NonCommander` | OK in Commander |

## Replacements
All suggestions below are absent from the deck, commander-legal, inside RW, not Game Changers (json + flag) and free of RemoveDeck flags. Strict-retail prices shown.

| OUT (line, $) | IN ($) | Why |
|---|---|---|
| Boros Signet (L13, 0.54) | **Worn Powerstone** (0.26) | Net-mana rock the AI casts. Alternatives: Star Compass (0.49) or Everflowing Chalice (0.28). Not Prismatic Lens, which has `AI:RemoveDeck:All` |
| Odric (L47, 0.36) | **Beetleback Chief** (0.22) | Non-Human Goblin that brings two non-Human tokens, which feed Winota triggers. Alternative: Siege-Gang Commander (0.26) |
| Angrath's Marauders (L3, 0.28) | **Hellrider** (0.53) | Non-Human attack payoff. Alternative: Raid Bombardment (0.23) |
| Archon of Emeria (L5, 1.06) | **Boros Reckoner** (0.25) | Non-Human RW body. Swapping it loses Archon's stax-lite effect. Alternative: Leonin Relic-Warder (0.32) |
| Bomat Courier (L10, 0.29) | **Goblin Instigator** (0.30) | Two non-Human bodies for Winota |
| Loran of the Third Path (L40, 4.99) | **Leonin Relic-Warder** (0.32) | Non-Human Cat that answers an artifact or enchantment |

Approximate strict totals:
- Only the two :All swaps: $87.92 − 0.90 + 0.48 = **≈ $87.50**.
- All six swaps: **≈ $82.79**.
- Both stay under $100.

The Random-flag swaps are optional if the team accepts that :Random only affects random deck generation. That is a policy call for Forge or the Manager.

## Bracket 2 power note
Winota passes every hard Bracket 2 check: not a Game Changer, no 2-card infinite, no extra turns, no MLD. But she is one of the most explosive RW commanders.
- **How she works:** each attacking non-Human puts a random Human from the library onto the battlefield tapped and attacking, indestructible this turn.
- **What she can pull here:** Adeline, Hero of Bladehold, Captain of the Watch, Pia and Kiran Nalaar, Lena, Thalia, Zealous Conscripts (Human Shaman, steals a blocker or Winota-protects) and Angrath's Marauders (non-Human, not hit). Combined with Ornithopter, Memnite and the token makers, this can produce turn-4/5 lethal swings in a 4-player pod.
- **Assessment:** legal, but a high-end Bracket 2 deck that may feel like Bracket 3. Disclose it to the pod.
- **Optional de-tuning:** fewer free 0-mana non-Humans (Memnite, Ornithopter, Phyrexian Walker) or fewer top-end Humans.
- **Alternative RW commanders, if Voltaire wants a softer face (suggestions only, not rebuilt):**
  - Feather, the Redeemed (spells matter).
  - Gisela, the Broken Blade (token doubling).
  - Aurelia, the Warleader (extra combat, which is not an extra turn).
  - Osgir, the Reconstructor (artifacts).
  - Tajic, Legion's Edge (combat).
  - Verify any of these before use.

## Source gaps
- The local sources have no per-bracket expectation text (the same gap as earlier audits). The Bracket 2 judgement uses house rules and Arbiter's judgement.
- Combo detection is a curated pair list plus manual review, not an exhaustive combo database.
- Prices are Scryfall 2026-10-14 bulk only; not live retail.
