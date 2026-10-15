# Batch 4 card-level notes (prepared 2026-10-15 ~8:30 AM PHT, read-only analysis, no deck changed)
Source: forge/playtest_batch4/g001-g200.log, parsed by b4_cards.py -> B4_CARD_STATS.txt.
Method: for each deck, the share of games it won among games where it cast a card at least once. Caveat: cards cast later appear mostly in longer games, so this is correlation, not cause. Lands show as "never cast" because they are played, not cast; ignore them.

## Headline
- A12 won 94/200 (47%); B11 44 (22%), C11 35 (17.5%), D11 27 (13.5%). A is clearly ahead; B, C, D need the next improvement round.
- Projected costs from SWAP_VERIFICATION.md: B $80.48, C $87.08, D $76.76, so each has roughly $13-23 headroom to the $100 target (hard cap $120).

## Spells never cast in 200 games (cut candidates, check for Forge AI misuse first)
- C11: Viscera Seer, Grim Haruspex, Undying Evil (also Orzhov Signet).
- D11: Faithless Looting (also Izzet Signet).
- B11: Ghostly Flicker, Deputy of Detention, Azorius Signet, Reliquary Tower.
- A12: Unbreakable Formation.
- Signets never cast in any deck: may be a Forge AI or parsing quirk; check a log before cutting.

## Weak when cast (well below the deck's base rate, n>=30)
- B11 (base 22%): Supreme Verdict 7/47, Hallowed Burial 6/39, Reflector Mage 9/53. Its three sweepers also hurt its own board.
- C11 (base 17.5%): Path to Exile 4/43, Despark 8/57, Night's Whisper 5/33.
- D11 (base 13.5%): Blasphemous Act 4/42, Sol Ring 6/58, Talrand 6/54, Third Path Iconoclast 6/51.

## Strong when cast
- B11: Agent of Treachery 27/47, Fact or Fiction 29/65, Angel of Serenity 23/55.
- C11: Blood Artist 14/36, Midnight Reaper 14/40, Liesa 15/43.
- D11: Increasing Vengeance 10/31, Fact or Fiction 16/57, Ral, Storm Conduit 14/54, Niv-Mizzet 11/43.
