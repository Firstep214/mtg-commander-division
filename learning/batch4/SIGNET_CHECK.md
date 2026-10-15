# SIGNET_CHECK (CH001-LEARN-02), Batch 4

## Verdict
**This is a Forge AI quirk, not a parsing miss.** The 2-colour guild Signets (Azorius/B11, Orzhov/C11, Izzet/D11) were drawn but the Forge AI never cast them in any of the 200 games. **Arcane Signet is fine.** It was cast and logged normally, and the stats parser counted it (B4_CARD_STATS.txt:21, :116, :174, :250).

## Evidence
- The decks loaded the right cards: /home/box/.forge/decks/commander/B11.dck:10 `Azorius Signet`, C11.dck:8 `Orzhov Signet`, D11.dck:8 `Izzet Signet` (they match decks/*_V1.1.txt).
- The guild Signets were drawn: they appear in 31 logs, and the only way they ever leave the hand is a cleanup discard. There are 31 discard lines, with no `cast`, `Resolve Stack` or `Mana:` lines for them. Examples:
  - g170.log:557-559: on turn 22, B11 casts Hallowed Burial (line 550) and then discards Talisman of Progress, Thought Vessel and Azorius Signet. The deck had made a land drop most turns (lines 225, 305, 406), so it had had 2 mana available for many turns while holding the Signet.
  - g178.log:748 `Ai(3)-D11 discards Izzet Signet (265).`; g192.log:1239 `Ai(4)-C11 discards Orzhov Signet (334).`; also g121.log:512, g082.log:308, g024.log:530.
- The only time a guild Signet reached the battlefield was through Sun Titan returning it from the graveyard (g170.log:995-998, g181.log:2564, g078.log:1249). Even after that, there are 0 `Mana: Azorius Signet` activations in any log.
- For comparison, Arcane Signet logs normally: g084.log:1247 `Add To Stack: Ai(1)-B11 cast Arcane Signet`, plus `Mana: Arcane Signet (50) - {T}: ...` at g084.log:1356.
- The parser is fine for spells: learning/batch4/b4_cards.py:9 matches `Add To Stack: Ai(n)-DECK cast X`, which is the exact format Forge uses for every spell, including artifacts.
- Root cause in Forge's card scripts (forge/app/res/cardsfolder/cardsfolder.zip):
  - `azorius_signet.txt`: `A:AB$ Mana | Cost$ 1 T | Produced$ W U` and `AI:RemoveDeck:All`.
  - `arcane_signet.txt`: `Cost$ T` and only `RemoveDeck:NonCommander`.
  - Forge's own script flags the guild Signets as cards the AI can't use. That is because their mana ability is a filter ({1},{T}). The AI doesn't count a filter as a net mana gain, so it never chooses to cast the card.

## Side finding (parser)
The parser only counts `cast`, so every land shows up as "never cast" in the stats (Command Tower, Glacial Fortress and so on, at B4_CARD_STATS.txt:133/199/265). Lands are logged as `Land: Ai(n)-DECK played X` (for example g084.log:59). Those entries don't mean anything is wrong with the lands. A fix is to add `played` to the regex at b4_cards.py:9, or track lands separately.

## Recommended fix
1. Don't judge the guild Signets from Forge results. The AI won't play them, so their win-rate numbers mean nothing. Decks running a guild Signet are effectively playing a dead card in these sims, which slightly understates B11, C11 and D11.
2. For sim accuracy, swap each guild Signet for a rock the AI does cast, at similar budget. Talismans get cast (B4_CARD_STATS.txt:123, :189, :261), as do Mind Stone and Fellwar Stone. Keep the Signet in the real paper list if people want it. Any swap must stay within the budget rule (aim for $100, hard cap $120).
3. Parser: count `Land: ... played` lines so lands drop out of the "never cast" list.
