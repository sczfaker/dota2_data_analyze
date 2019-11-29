import io,sys
sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding="utf-8")
import json
import os
os.chdir("dota")
dic=json.load(open("hero.json"))
assert len(dic)==117

for i in dic:
	s=dic[i]
	break
for j in s:
	print (j)



































"""
abaddon
['Mist Coil', 'Aphotic Shield', 'Curse of Avernus', 'Borrowed Time']
alchemist
['Acid Spray', 'Unstable Concoction', "Greevil's Greed", 'Chemical Rage']
ancient-apparition
['Cold Feet', 'Ice Vortex', 'Chilling Touch', 'Ice Blast']
anti-mage
['Mana Break', 'Blink', 'Counterspell', 'Mana Void']
arc-warden
['Flux', 'Magnetic Field', 'Spark Wraith', 'Tempest Double']
axe
["Berserker's Call", 'Battle Hunger', 'Counter Helix', 'Culling Blade']
bane
['Enfeeble', 'Brain Sap', 'Nightmare', "Fiend's Grip"]
batrider
['Sticky Napalm', 'Flamebreak', 'Firefly', 'Flaming Lasso']
beastmaster
['Wild Axes', 'Call of the Wild Boar', 'Call of the Wild Hawk', 'Inner Beast', 'Primal Roar']
bloodseeker
['Bloodrage', 'Blood Rite', 'Thirst', 'Rupture']
bounty-hunter
['Shuriken Toss', 'Jinada', 'Shadow Walk', 'Track']
brewmaster
['Thunder Clap', 'Cinder Brew', 'Drunken Brawler', 'Primal Split']
bristleback
['Viscous Nasal Goo', 'Quill Spray', 'Bristleback', 'Warpath']
broodmother
['Spawn Spiderlings', 'Spin Web', 'Incapacitating Bite', 'Insatiable Hunger']
centaur-warrunner
['Hoof Stomp', 'Double Edge', 'Retaliate', 'Stampede']
chaos-knight
['Chaos Bolt', 'Reality Rift', 'Chaos Strike', 'Phantasm']
chen
['Penitence', 'Holy Persuasion', 'Divine Favor', 'Hand of God']
clinkz
['Strafe', 'Searing Arrows', 'Skeleton Walk', 'Burning Army']
clockwerk
['Battery Assault', 'Power Cogs', 'Rocket Flare', 'Hookshot']
crystal-maiden
		9876 150 200 250 300
['Crystal Nova', 'Frostbite', 'Arcane Aura', 'Freezing Field']
dark-seer
['Vacuum', 'Ion Shell', 'Surge', 'Wall of Replica']
dark-willow
['Bramble Maze', 'Shadow Realm', 'Cursed Crown', 'Bedlam', 'Terrorize']
dazzle
['Poison Touch', 'Shallow Grave', 'Shadow Wave', 'Bad Juju']
death-prophet
['Crypt Swarm', 'Silence', 'Spirit Siphon', 'Exorcism']
disruptor
['Thunder Strike', 'Glimpse', 'Kinetic Field', 'Static Storm']
doom
['Devour', 'Scorched Earth', 'Infernal Blade', 'Doom']
dragon-knight
['Breathe Fire', 'Dragon Tail', 'Dragon Blood', 'Elder Dragon Form']
drow-ranger
['Frost Arrows', 'Gust', 'Precision Aura', 'Marksmanship']
earth-spirit
['Boulder Smash', 'Rolling Boulder', 'Geomagnetic Grip', 'Magnetize']
earthshaker
['Fissure', 'Enchant Totem', 'Aftershock', 'Echo Slam']
elder-titan
['Echo Stomp', 'Astral Spirit', 'Natural Order', 'Earth Splitter']
ember-spirit
['Searing Chains', 'Sleight of Fist', 'Flame Guard', 'Fire Remnant']
enchantress
['Untouchable', 'Enchant', "Nature's Attendants", 'Impetus']
enigma
['Malefice', 'Demonic Conversion', 'Midnight Pulse', 'Black Hole']
faceless-voids
['Time Walk', 'Time Dilation', 'Time Lock', 'Chronosphere']
grimstroke
['Stroke of Fate', "Phantom's Embrace", 'Ink Swell', 'Soulbind']
gyrocopter
['Rocket Barrage', 'Homing Missile', 'Flak Cannon', 'Call Down']
huskar
['Inner Fire', 'Burning Spear', "Berserker's Blood", 'Life Break']
invoker
['Quas', 'Wex', 'Exort', 'Invoke']
io
['Tether', 'Spirits', 'Overcharge', 'Relocate']
jakiro
['Dual Breath', 'Ice Path', 'Liquid Fire', 'Macropyre']
juggernaut
['Blade Fury', 'Healing Ward', 'Blade Dance', 'Omnislash']
keeper-of-the-light
['Illuminate', 'Blinding Light', 'Chakra Magic', 'Will-O-Wisp']
kunkka
['Torrent', 'Tidebringer', 'X Marks the Spot', 'Ghostship']
legion-commander
['Overwhelming Odds', 'Press The Attack', 'Moment of Courage', 'Duel']
leshrac
['Split Earth', 'Diabolic Edict', 'Lightning Storm', 'Pulse Nova']
lich
['Frost Blast', 'Frost Shield', 'Sinister Gaze', 'Chain Frost']
lifestealer
['Rage', 'Feast', 'Open Wounds', 'Infest']
lina
['Dragon Slave', 'Light Strike Array', 'Fiery Soul', 'Laguna Blade']
lion
['Earth Spike', 'Hex', 'Mana Drain', 'Finger of Death']
lone-druid lone-druid
['Summon Spirit Bear', 'Spirit Link', 'Savage Roar', 'True Form']
luna
['Lucent Beam', 'Moon Glaives', 'Lunar Blessing', 'Eclipse']
90/180/270/300 
lycan
['Summon Wolves', 'Howl', 'Feral Impulse', 'Shapeshift']
magnus 
['Shockwave', 'Empower', 'Skewer', 'Reverse Polarity']
mars
['Spear of Mars', "God's Rebuke", 'Bulwark', 'Arena Of Blood']
medusa
['Split Shot', 'Mystic Snake', 'Mana Shield', 'Stone Gaze']
meepo
['Earthbind', 'Poof', 'Ransack', 'Divided We Stand']
mirana 
['Starstorm', 'Sacred Arrow', 'Leap', 'Moonlight Shadow']
monkey-king
['Boundless Strike', 'Tree Dance', 'Jingu Mastery', "Wukong's Command"]
morphling
['Waveform', 'Adaptive Strike (Agility)', 'Adaptive Strike (Strength)', 'Attribute Shift (Agility Gain)', 'Morph']
naga-siren
['Mirror Image', 'Ensnare', 'Rip Tide', 'Song of the Siren']
natures-prophet
['Sprout', 'Teleportation', "Nature's Call", 'Wrath of Nature']
necrophos
['Death Pulse', 'Ghost Shroud', 'Heartstopper Aura', "Reaper's Scythe"]
night-stalker
['Void', 'Crippling Fear', 'Hunter in the Night', 'Dark Ascension']
nyx-assassin
['Impale', 'Mana Burn', 'Spiked Carapace', 'Vendetta']
ogre-magi
['Fireblast', 'Ignite', 'Bloodlust', 'Multicast']
omniknight
['Purification', 'Heavenly Grace', 'Degen Aura', 'Guardian Angel']
oracle
["Fortune's End", "Fate's Edict", 'Purifying Flames', 'False Promise']
outworld-devourer
['Arcane Orb', 'Astral Imprisonment', 'Equilibrium', "Sanity's Eclipse"]
pangolier
['Swashbuckle', 'Shield Crash', 'Lucky Shot', 'Rolling Thunder']
phantom-assassin
['Stifling Dagger', 'Phantom Strike', 'Blur', 'Coup de Grace']
phantom-lancer
['Spirit Lance', 'Doppelganger', 'Phantom Rush', 'Juxtapose']
phoenix
['Icarus Dive', 'Fire Spirits', 'Sun Ray', 'Supernova']
puck
['Illusory Orb', 'Waning Rift', 'Phase Shift', 'Dream Coil']
pudge
['Meat Hook', 'Rot', 'Flesh Heap', 'Dismember']
pugna
['Nether Blast', 'Decrepify', 'Nether Ward', 'Life Drain']
queen-of-pain
['Shadow Strike', 'Blink', 'Scream Of Pain', 'Sonic Wave']
razor
['Plasma Field', 'Static Link', 'Unstable Current', 'Eye of the Storm']
riki
['Smoke Screen', 'Blink Strike', 'Cloak and Dagger', 'Tricks of the Trade']
rubick
['Telekinesis', 'Fade Bolt', 'Arcane Supremacy', 'Spell Steal']
sand-king
['Burrowstrike', 'Sand Storm', 'Caustic Finale', 'Epicenter']
shadow-demon
['Disruption', 'Soul Catcher', 'Shadow Poison', 'Demonic Purge']
shadow-fiend
['Shadowraze', 'Necromastery', 'Presence of the Dark Lord', 'Requiem of Souls']
shadow-shaman
['Ether Shock', 'Hex', 'Shackles', 'Mass Serpent Ward']
silencer
6/5
['Arcane Curse', 'Glaives of Wisdom', 'Last Word', 'Global Silence']
skywrath-mage
['Arcane Bolt', 'Concussive Shot', 'Ancient Seal', 'Mystic Flare']
slardar
['Guardian Sprint', 'Slithereen Crush', 'Bash of the Deep', 'Corrosive Haze']
slark
['Dark Pact', 'Pounce', 'Essence Shift', 'Shadow Dance']
sniper
['Shrapnel', 'Headshot', 'Take Aim', 'Assassinate']
spectre
['Spectral Dagger', 'Desolate', 'Dispersion', 'Haunt']
spirit-breaker
['Charge of Darkness', 'Bulldoze', 'Greater Bash', 'Nether Strike']
storm-spirit
['Static Remnant', 'Electric Vortex', 'Overload', 'Ball Lightning']
sven
['Storm Hammer', 'Great Cleave', 'Warcry', "God's Strength"]
techies
['Proximity Mines', 'Stasis Trap', 'Blast Off!', 'Minefield Sign', 'Remote Mines']
templar-assassin
['Refraction', 'Meld', 'Psi Blades', 'Psionic Trap']
terrorblade
['Reflection', 'Conjure Image', 'Metamorphosis', 'Sunder']
tidehunter
['Gush', 'Kraken Shell', 'Anchor Smash', 'Ravage']
timbersaw
['Whirling Death', 'Timber Chain', 'Reactive Armor', 'Chakram']
tinker
['Laser', 'Heat-Seeking Missile', 'March of the Machines', 'Rearm']
tiny
['Avalanche', 'Toss', 'Tree Grab', 'Grow']
treant-protector
["Nature's Guise", 'Leech Seed', 'Living Armor', 'Overgrowth']
troll-warlord
["Berserker's Rage", 'Whirling Axes (Ranged)', 'Fervor', 'Battle Trance']
tusk
 36 24 12
['Ice Shards', 'Snowball', 'Tag Team', 'Walrus PUNCH!']
underlord
['Firestorm', 'Pit of Malice', 'Atrophy Aura', 'Dark Rift']
4 473 2% 1000
undying
['Decay', 'Soul Rip', 'Tombstone', 'Flesh Golem']
ursa
['Earthshock', 'Overpower', 'Fury Swipes', 'Enrage']
vengeful-spirit
['Magic Missile', 'Wave of Terror', 'Vengeance Aura', 'Nether Swap']
venomancer
['Venomous Gale', 'Poison Sting', 'Plague Ward', 'Poison Nova']
viper
['Poison Attack', 'Nethertoxin', 'Corrosive Skin', 'Viper Strike']
visage
['Grave Chill', 'Soul Assumption', "Gravekeeper's Cloak", 'Summon Familiars']
warlock
['Fatal Bonds', 'Shadow Word', 'Upheaval', 'Chaotic Offering']
weaver
['The Swarm', 'Shukuchi', 'Geminate Attack', 'Time Lapse']
windranger
['Shackleshot', 'Powershot', 'Windrun', 'Focus Fire']
winter-wyvern
['Arctic Burn', 'Splinter Blast', 'Cold Embrace', "Winter's Curse"]
witch-doctor
['Paralyzing Cask', 'Voodoo Restoration', 'Maledict', 'Death Ward']
wraith-king
['Wraithfire Blast', 'Vampiric Aura', 'Mortal Strike', 'Reincarnation']
zeus
['Arc Lightning', 'Lightning Bolt', 'Static Field', "Thundergod's Wrath"]
[Finished in 0.2s]
"""

	# for j in dic[i]['ability'][0]:
	# 	print (j,end="::::::::")
	# 	print (dic[i]['ability'][0][j])
	# if i=="invoker":
	# 	for j in dic[i]['ability'][0]:
	# 		print (j,end="::::::::")
	# 		print (dic[i]['ability'][0][j])
	# 	break
	# print ()