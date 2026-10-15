exec(open('forge_and_price.py').read().split("L=[(i")[0])
import sys;sys.path.insert(0,'/workspace/mtg/audits/arbiter_scripts');import audit as A
deck={x.split(' ',1)[1].strip().lower() for x in open('decks/E_clean.txt') if x.strip()}
C=['Worn Powerstone','Prismatic Lens','Star Compass','Everflowing Chalice','Legion Loyalist','Goblin Instigator','Beetleback Chief','Mardu Ascendancy','Boros Reckoner','Hellrider','Rally the Ranks','Raid Bombardment','Inspired Sphinx','Thraben Inspector','Siege-Gang Commander','Brimaz, King of Oreskos','Combat Celebrant','Leonin Relic-Warder','Fervent Champion','Dragon Fodder','Lightning Helix','Ox of Agonas','Assemble the Legion','Basri\'s Lieutenant','Myriad Landscape','Rally the Peasants','Iroas, God of Victory','Coat of Arms','Purphoros, God of the Forge']
for n in C:
  c=A.cards.get(n.lower()); f=idx.get(n.lower())
  fl=[l for l in f[1].splitlines() if 'RemoveDeck' in l] if f else ['NO FORGE SCRIPT']
  print(n,'|in deck' if n.lower() in deck else '|absent',c['color_identity'],c['legalities']['commander'],'GC' if (c.get('game_changer') or n.lower() in A.GC) else '-',st.get(n.lower()),fl,c['type_line'])
