#This is a document for scenes and their choices
#This import stores all the functions for this document.
import scene_functions, globals

#aliases the scene_functions file to f
f = scene_functions

name = globals.player_name

#Creates a way for descriptions and choices to be stored in a dict
class reader(object):
	def __init__(self, desc, dict):
		self.desc = desc
		self.dict = dict
	def read(self):
		"""Checks to see if the description is a string or a function. If description is a string it prints it, if it is a function it adds the () to it and that runs it. Then it returns the dict they all have. There is a little script to check if the dict is a function that returns a dict or a dict. But what ever case, the dict is the choices."""
		if isinstance(self.desc, str):
			self.printer()
		else:
			self.function_printer()
#There are two ways to check for a function in self.dict, both are below.
		if not isinstance(self.dict, dict):
		#if hasattr(self.dict, '__call__'):
			return self.dict()
		else:
			return self.dict

	def function_printer(self):
		"""Adds a () to a function which runs it. There is no implamentation yet for returns, but there can be if I really want it."""
		self.desc()
	def printer(self):
		"""Just prints the description like normal..."""
		print self.desc


#Stores the scenes in a way that doesn't need each scene to be its own function.
scene_dict = {
'Pre_intro': reader(f.intro, {'intro1': 'Please press 1 to continue.'}),

'intro1': reader("""
Somewhere in the Milky Way galaxy, approaching the binary sun Mesarthim. The 
ship C15D21, shortened to CD by the crew is one of five thousand ships sent 
out by the solar counsel to map and explore the Earth-like planets of the 
Milky Way. The crew on CD are all highly trained space pilots who have spent 
the last thirty years of their life in an astronautics boot camp. Everyone has 
been given the full dose of CR, the drug to increase a human's life span up to 

three times its normal hundred and thirty year span.
The Mesarthim solar system is the twelfth solar system visited by this crew. 
Their massive ship is home to a drive system that propels them upward around 
two hundred thousand miles per second. The ship is fitted with a fission 
shield that disintegrates any matter within a hundred thousand miles, so the 
viewing monitors are often filled with exploding asteroids and comets. As they 
approach each system, a smaller ship is deployed with a crew to take a closer 
look at each of the planets in the solar system.
""", {'intro2': 'Please press 1 to continue.'}),

'intro2': reader("""
In the planetary shuttle CD7, seventy top notch space explorers approach the 
orbit of the planet named M25. The planet is three times the size of earth and 
the coolest temperature is around twenty degrees Fahrenheit in the Polar 
regions. Much of the planet's surface is warm water,
and the winter half of the planet is kept warm by volcanic activity.
Otherwise the planet would be much colder than earth. What also helps is that 
over much of the planet is a 
very thick atmosphere, and constant storms are circling the cooled air in with 
the warm air.
""", {'act1': 'Please press 1 to continue.'}),

'act1': reader(f.fact1, {'bridge1': 'Press 1 to continue.'}),

'bridge1': reader("""*You were on your way to the captain's room when the emergency 
systems kicked in. The only place to stowaway was next to the heating system 
in the most cramped and well insulated capsule on the shuttle. The capsules 
are meant to fire toward central while their occupants are sedated and kept in 
a strictly regulated environment.""", {'bridge2': 'Press 1 to continue.'}),

'bridge2': reader("""You find the opening of the capsule and realize that your six foot five frame 
will have to bend in order to fit in the just under six foot compartment. You 
pull open the capsule and manage to cram yourself into the small opening, but 
no matter how hard you try, the compartment will not shut. As you are 
struggling with the lid, power is cut from the shuttle and a very loud 
screeching noise fills the air. The whole ship begins to shake and the smell 
of hot metal and ozone begins to fill the air. You realize that if you are 
smelling ozone, either something extremely horrible is happening to the 
engines, or there is some kind of atmosphere outside and the massive shell of 
the shuttle has been breached.*""", {'bridge3': 'Press 1 to continue.'}),


'bridge3': reader(f.fbridge3, {'bridge4': 'Press 1 to continue.'}),

'bridge4':
reader("""As you tentatively push off from your Anker point and slowly inch your way 
along the rails that seem to still be in place, even after all the shuttle has 
been through, the little face shoots toward you, moving the corners of its 
crescent down even farther.""", {'scream': """Scream as if your life depends on it and hope it will scare away the little 
creature.""",
'joke': 'Tell the creature that looks like a green frowny face a joke.', 'hide': 'Move back to the somewhat protective capsule.',
'try_talking': 'Try talking to the creature and hope it does not eat you.'}),

'scream': reader("""You take a deep breath and let out a blood curdling scream, drawing a 
multitude of the creatures to your location. The little creature in front of 
you opens its mouth as wide as it will go and lets out the same kind of scream 
like sound, but the sound he makes is somewhat more destructive. It knocks you 
out cold.""", {'death': ''}),

'joke':
reader("""You burst out with the first joke that comes to your mind:
'What is a light-year?'
Without waiting for a response from the angry looking visage you hurry on
'A light year is just like a regular year, but with less calories!'
For a moment nothing happens, then suddenly you can't hold back your laughter 
anymore and you break down into uncontrollable giggles. The green face 
hesitates then joins you with gales of laughter.
You wipe tears from your face and take a breath. The green creature is 
spinning around; laughing as if there is no tomorrow. You grin and head toward 
the main bridge where most of the other capsules are.""", {'main_bridge1': 'Press 1 to continue.'}),

'hide':
reader("""You scramble as fast as you can in free-fall back to the protection of the 
capsule and try once more to close the lid. As you struggle, the green face 
comes around the top of the open lid and the two black holes above the 
crescent fill with a red light. You are entranced by the vivid colors.""", {'death': ''}),

'try_talking':
reader(f.fjoke, {'main_bridge1': 'Press 1 to continue.'}),

'main_bridge1':
reader("""The glowing green alien's laughter follows you as you turn to go into the 
bridge. As you approach the small access way into the much larger room, you 
realize the amount of laughing in front of you is significantly more than that 
behind you. You slowly inch your way toward the door and peek around the edge. 
What greets your eyes is something out of a horror story.
The room is filled with nearly a hundred giggling glowing green aliens and 
they are all in a large circle surrounding what is left of the ship's crew. As 
you watch you are shocked to see all the creatures focus their smaller two 
black holes toward a ship mechanic you recognize. The mechanic was one of the 
ones who ate at the same time as you, but he was rather reserved and didn't 
talk much. As you watch in dreadful fascination, the black holes of the green 
creatures begin to glow a deep read. The man in the circle begins to scream 
and he dives toward one of the capsules, but before he moves one step, he is 
hit with the combined force of the alien's red beams.""", {'main_bridge2': 'Press 1 to continue.'}),

'main_bridge2':
reader("""Before your eyes the man 
is morphed into a large green blob with a black crescent splitting the shape 
in half and two smaller holes on one side of the crescent. As you watch a 
laugh louder than all the rest begins. What used to be the mechanic begins to 
expand and rotate. The two black holes begin glowing a brighter red than any 
of the creatures in the circle. As the creature rotates back toward the few 
remaining crew, you see Jenny, the communications specialist notice you. As 
you watched mortified, she points a black device at you and you feel your 
phone vibrate. Here in space phones have become a means of short range 
communication between members of the crew on the same ship, rather than the 
longer ranged phones of Earth. You reach for your pocket and as you dig the 
miniature computer out, you see Jenny get caught by the red beams of the newly 
formed creature. Before your eyes the same process occurs, although this time 
the newer creature is much smaller and the two new creatures float off to join 
the circle of giggling green aliens.
Sickened, you turn away and look to see the message that Jenney sent you:
'kill us'""", {'main_bridge3': 'Press 1 to continue.'}),

'main_bridge3':
reader("""You gasp at the two words printed on the screen; does this mean the rest of 
the crew is hopelessly captured by the horrible green blobs?
'kill us' 
The two words repeat over and over in your head as you drift aimlessly down 
the hall. The sound of a short scream intrudes into your numb state.""", {'main_bridge4': """Throw yourself into the room and take out as many of the creatures as you 
can before you are turned into a giggling green thing""",
'main_bridge6': 'Find some way to obliterate all the creatures in one devastating attack.',
'main_bridge7': 'Recognize your survival is hopeless and find a way to kill yourself quickly\nand painlessly.', 'main_bridge5': 'Shout at the creatures and tell them to let your people go!'}),

'main_bridge4':
reader("""You spin around and drift back toward the room filled with not quite carnage. 
Your eyes fall on a loose section of railing that must have broken off when 
the things that made the holes penetrated the hull. You pull the two foot bar 
from its remaining supports and test swing it a few times. In free-fall your 
actions are much slower and less powerful as they would be on earth, but you 
think you have enough control to do some meteor damage.
You position yourself so that when you launch yourself into the large room, 
you will stab the closest of the green blobs.
You count to three and push off with your legs. Your acceleration brings you 
hurling toward the nearest alien as fast as you could manage to go. You feel 
the air rushing past your face. You close your eyes, just in case the impact 
with the creature results in a ton of blood and guts. You take a deep breath 
in and let out a loud shout of triumph. As the sound leaves your mouth though, 
a violent collision with something extremely hard brings your world to 
darkness.""",
{'death': 'Press 1 to continue.'}),

'main_bridge5':
reader("""You reverse direction and float back to the door. You see a navigator that you 
have met a few times; he is cowering with his hands over his head, looking 
very much as if he does not want to be where he is. You shout his name and he 
flinches. You run in and start yelling at the green blobs to let your friends 
go. The circle of blobs ignores you. You walk over to the nearest creature and 
raise your hand to tap it. As your skin makes contact with the glowing skin, a 
tremendous shock runs through your body. It is so powerful and so startling 
that you black out.""",
{'death': 'Press 1 to continue.'}),

'main_bridge6':
reader("""You frees and slowly inch your way into a small storage compartment that is 
somewhat intact after the invasion. You sit down and try to think.
The sound system may help in telling jokes to the whole ship, but it wasn't as 
if all the green creatures were frowning like the first creature. Perhaps only 
frowny creatures that become happy are somewhat nicer? You discard that idea. 
You rack your brain for any kind of weapons system that you could use. The 
only time you ever heard anyone talk about weapons was when the landing crew 
brought a minor defense mechanism out to work on it. You try and think about 
where the weapons may be.""", 
{'logic': 'Press 1 to continue.'}),

'main_bridge7':
reader("""You know in your heart that scream is signaling the end of humanity on the 
ship. Despondency fills you as you realize just how lonely you are. Your mind 
reluctantly turns to consider your plight. You are the only one who is not in 
the large chamber. You try and think about ways to die. You know spacing 
yourself is an option if you manage to get out of the strange bubble the ship 
is surrounded by.""",
{'logic': 'Press 1 to continue.'}),

'logic':
reader("""You know the weapons people have some stuff because you saw a protection unit 
that the landing crew brought out that needed repaired. You have never been in 
the weapons area, but you know the captain's hall is not near there because he 
keeps trying to get the ship remodeled so weapons is closer to him.
You know that when you are standing in the main annex, there are 8 halls in a 
line. From the left you start with hall 1 and all the way to the right is hall 
8.
You know the map people are in hall 2.
Computers are next to maps.
Sleeping chamber is 5 doors away from maps.
Maps is between communications and computers, because you keep seeing the 
computer guys walking with communication devices past the maps hall opening.
Mess hall is next to the kitchen.
The kitchen is near the sleeping chamber and is closer to computers than maps. 
Captain's quarters is not near weapons and is the last door.
What door is weapons in?""", f.flogic),

'logicd':
reader("""You start drifting toward the hall you think weapons is in. You reach the dark 
opening and halt. You look in the door and listen for any strange sounds. You 
drift into the darkness. You grope around; trying to figure out what room it 
is you have entered. You find a hole that was made by the creature's invasion 
and give into the temptation to look out. You stick your head out the two foot 
by two foot opening and realize you can't see anything. You squeeze a little 
farther out and look around. The darkness outside of the ship is total and 
complete. It is so thick, that it almost feels as if you are swimming in it. 
You take a deep breath of the atmosphere outside the ship. You shake your head 
in wonder and begin to pull your body back into the body of the ship. You 
manage to extricate your shoulders, but before you are fully inside the 
damaged hull, something hits the top of your head and shoots you back. You fly 
across the room and as you hit the opposite wall with enough force to knock 
you out, you see two red spots of light in front of you.""", {'death': 'Please press 1 to continue.'}),

'laser1':
reader("""You drift into the door you think weapons is in. As you reach the door you 
pause and question if this is a good idea. You slowly drift into the darkness. 
You keep moving till you hit an empty space suit secured to the wall. You ask 
yourself if you should put it on. You start feeling around the familiar 
compartments of the massive covering. To your surprise you find a flashlight. 
You flick it on and gape in amazement. The hall you are in has three doors. 
The one farthest above you is just a normal door, if a door comprised 
completely of lasers is considered normal. The one below that is a massive 
steel door with a poster on it. The one below that is just a gaping hole into a large room.
What door would you like to choose?""",
{'ld': 'Laser door.',
'md': 'Metal door.',
'hd': 'Gaping hole.'}),

'laser2':
reader("""
The hall you are in has three doors. 
The one farthest above you is just a normal door, if a door comprised 
completely of lasers is considered normal. The one below that is a massive 
steel door with a keypad. The one below that is just a gaping hole into a 
large room.
What door would you like to choose?""",
{'ld': 'Laser door.',
'md': 'Metal door.',
'hd': 'Gaping hole.'}),

'hd':
reader("""You head toward the black hole and suavely shine your flashlight into the 
hole. You see several desks filled with papers.""",
{'desk': 'Search the desks.',
'mad': 'Go on a mad frenzy.',
'laser2': 'leave'}),

'desk':
reader("""You take a closer look at the different papers scattered around this not so 
clean work space. You see a stack of papers on the left side of the desk under 
a magnetized pen holder. There is a drawer on the right side of the desk and 
there is a piece of paper taped to the wall behind the desk under a poster of 
a giant sword.""",
{'desk2': 'Shuffle through the papers under the pen holder.',
'desk3': 'Riffle through the drawer.',
'desk4': 'Check out the paper and poster taped to the wall.',
'laser2': 'go out'}),

'desk2':
reader("""You lift up the pen holder and begin to look through the papers. The top of 
the first paper reads:""", {'p1': 'Press 1 to continue.'}),

'p1':
reader("""roster for testing weap 521.
Check for velocity when traveling through vacuum, find max blast before boom, 
set combo.""",
{'p2': 'Press 1 to continue.'}),

'p2':
reader(f.fp2,
{'p3': 'Press 1 to continue.'}),

'p3':
reader("""The next paper reads:
Meeting to talk about secret project:
Food list:
Sam is bringing Twinkies
Loran is bringing patwals
Rays is bringing balls
Crisco is bringing drink
New folks remember WEAP!""",
{'desk': 'Press 1 to continue.'}),

'desk3':
reader("You pull out the drawer and begin removing files:",
{'d1': 'Press 1 to continue.'}),

'd1':
reader("""Files on personnel:
Sam:
Worked in galactic artillery and in particular those dealing with obliterating 
ships. He likes playing the historical games that were when Graphics cards and 
using external screens and headsets were the rage.
Loran:
Ponies!!! Growing up on Cupcakes and Rainbow Factory, Loran devoted her life 
to stop oppression in all forms. She was the head of the coalition that was 
formed to liberate slave ships. She worked in that sector for 20 years till 
she sustained a mass of major injuries while saving a group of ten slaves 
after her whole crew had been killed. She managed to get off the ship with the 
slaves, but was not able to return to that job after recovering somewhat. She 
devoted her life to studying oppression in alien civilizations and joined the 
planetary explorations in order to study and possibly encounter alien 
civilizations.""",
{'d2': 'Press 1 to continue.'}),

'd2':
reader(f.fd2,
{'d3': 'Press 1 to continue.'}),

'd3':
reader(f.fd3,
{'d4': 'Press 1 to continue.'}),

'd4':
reader("""You also find:
A couple novels and a box with a ring in it.
You put everything back and shut the drawer.
""",
{'desk': 'Press 1 to continue.'}),

'desk4':
reader(f.fdesk4,
{'desk': 'Press 1 to continue.'}),

'mad':
reader("""You let out a holler and using your best Bruce Lee impersonation, you fly 
forward and kick and punch the wood desks. Not much happens except for papers 
flying everywhere, creating a huge mess.""",
{'hd': 'Press 1 to continue.'}),

'md':
reader("""As you approach the extremely sturdy looking door you realize it would take 
more than a high powered blow torch to cut through this metallic monstrosity. 
There is a bar 6 inches in diameter lying horizontally across the door. The 
door makes no echo when you tap on it. On the top of the door there is a 
poster of a guy with white hair holding a massive sword. Under the poster 
there is a big red W.""",
{'pull': 'Pull on the bar till you get some hernias.',
'poke': 'Poke the poster in different places...',
'tug': 'Tug on the W.',
'laser2': 'Go back and choose another door.'}),

'pull':
reader("""You wrap your hands around the bar and just start pulling for all you are 
worth. You soon place your feet on the door to give you more leverage, but 
nothing happens. You take a breath and give one final heave. You hear 
something pop in your legs, but nothing changes with the door.""",
{'md': 'Please press 1 to continue.'}),

'poke':
reader(f.fpoke, f.fpoke2),

'tug':
reader("""You drift over and make a W sign with your right hand. You give the W on the 
door a nice hard high wive. Nothing seems to happen. You then start tugging 
and trying to shift the W, but nothing changes. After a while you give up and 
float back to consider your options.""",
{'md': 'Please press 1 to continue.'}),

'break':
reader("""You pull yourself past the sturdy door and find yourself in a strange looking 
room. There are all kinds of gadgets lining the walls and a Ping-Pong table 
set up in the middle of the room. A star chart covers the far wall and a smart 
screen is on the wall to your left. A couple beanbag chairs are to your right 
and a small chemistry lab is above your head.""",
{'explore': 'investigate the gadgets around the walls.',
'ping-pong': 'Scrutinize the Ping-Pong table.',
'chill': 'Sit on the beanbag chairs.',
'fiddle': 'Fiddle around with the chemistry lab.',
'laser2': 'Leave.'}),

'explore':
reader("""A large long tube catches your eye as you look closer at all the devices 
scattered around the walls. You move over to it and you see that the tube is about seven 
feet long and 3 inches in diameter. One end is just a hollow tube and the 
other curves outward and has padding on the flat part on the opposite end as 
the hole. There is some kind of complex mechanical contrivance on one side and 
you see some wording along one side of the contraption: 'Da Big Gun'
You see how it could be a gun, but it is one massive blaster!
You drift over to another interesting contrivance and see something that looks 
like a three foot wide quarter. One side is pocked with holes spaced every 
four inches apart and the other side has a huge clown face painted on.""",
{'break': 'Investigate something else in the room.',
'da_gun': 'Use one of the weapons to exterminate the aliens.'}),

'da_gun':
reader("""You grab Da Big Gun and thank your lucky stars there is no gravity. The thing 
looks like it is made out of solid steal. You find a case behind it and find 
that it is filled with what seems to be cartridges. You fiddle around with Da 
Gun for a while and finally manage to get everything fitted properly. You make 
your way out of the weapons armory and into the hallway. You nudge open the 
door to the main bridge where you last saw the rest of the crew. There are no 
humans left, just one big green blob rotating very fast in the center of the 
room. You brace the gun against your body and try to pull one of the levers. 
Nothing happens, so you begin pulling or pushing every lever you see. Finally 
after pulling out a little red lever you feel the gun begin to vibrate in your 
hands. You grin evilly and make sure the nozzle of the gun is pointed right at 
the spinning monstrosity. You see some red lights come on all over the gun, 
but pay them no heed. You start to feel your heart race and you just want to 
pull some levers, even if they don't do anything. You pull the largest lever 
and all your senses go blank. Perhaps it wasn't the best idea to shoot the gun 
in an atmosphere...""",
{'death': 'Please press 1 to continue.'}),

'ping-pong':
reader("""A Ping-Pong table in zero grav? How does playing Ping-Pong work when the balls 
don't stop going up? The table looks very battered and you guess the black 
spots are probably chemical burns. The netting is not really a netting more 
than a lot of stitched together ice-cream wrappers... Under the table you strike 
gold. A stash of beers is lined up, just itching for someone to pop their 
caps.""",
{'beer': 'Take a beer.',
'break': 'Go and investigate something else.'}),

'beer':
reader(f.fbeer, f.fbeer2),

'chill':
reader("""The Cush of the beanbag chairs is too inviting to pass up. You drift into the 
soft Styrofoam beans and start to relax as the comfyness saturates your body. 
You shut your eyes for a second, but are startled into reopening them when a 
bar hits your left arm. You look down and see a light blue game controller on 
a metallic arm waiting for you to take it.""",
{'chill2': 'Take the controller.',
'break': 'Push the controller away and investigate something else.'}),

'chill2':
reader(f.fchill, {'chill3': 'Please press 1 to continue.'}),

'chill3':
reader(f.fchill2, f.fchill2_2),

'chill4':
reader(f.fchill3, f.fchill3_2),

'fiddle':
reader("""You launch yourself off the Ping-Pong table and drift up to the chemistry lab. 
There are several tightly sealed cases bolted down. You try the first two but 
they are locked. The third case opens to reveal several powder cases and two 
liquid cases. The first powder case is marked with a bright red danger symbol 
and the title: 'deathwish'. The second case is labeled with a radiation sign 
and is labeled with a 'Theobroma cacao mixture'. The last powder case just has 
some black lace taped onto it. The two liquid containers are color coded, the 
one on the right is red and the one on the left is blue. There is also a long 
tube along the side of the blue container with a cup sticking out of the 
bottom. The tube has in big bold letters: 'for toxic liquids only'.""",
{'fiddle2': 'Pull a cup out and mix together some liquid and powder.',
'break': 'Go investigate something else.'}),

'fiddle2':
reader(f.ffiddle2, {'fiddle2': 'Mix another cup.', 'break': 'Go explore something else.'}),

'ld':
reader("""You drift toward the circular door and look around for some way to open the 
insubstantial but deadly door. The lazars seem to be reflecting off of 
mirrors, but you're not quite sure where the two bases are. You finger the 
surrounding frame and notice a little keypad. It looks like a phone keypad, 
and you surmise it is for deactivating the lazars.""",
{'keypad': 'Try and guess the sequence of keys to open the door.',
'laser2': 'Go back and find another door.'}),


'keypad':
reader("You scratch your head and begin:",
f.fkeypad),

'keypad2':
reader("You scratch your head and try again.", f.fkeypad),

'keypad3':
reader("""You hear a slight click from inside the door. You see a small whole form in 
the laser screen and a little clown head pops out. You look goggle eyed at the 
red-lipped grinning face in front of you. For some reason you feel some 
uncountable dread. The clown face opens its mouth and blows a tremendous 
raspberry at you. Even from where you are floating, you feel the creature's 
spit. The clown head then begins to giggle and soon it breaks out into a full 
throated maniacal laugh.
You reach up and begin to wipe the disgusting spit off your exposed face. All 
of a sudden the drops of liquid begin to burn and you begin to wipe faster. 
Soon the burning becomes unbearable. You begin to go crazy, bashing your head 
against the walls and screaming at the top of your lungs. One bash against an 
exposed pipe proves too much for your poor head and you black out.""",
{'death': 'Please press 1 to continue.'}),

'bom':
reader("""You take a hesitant look inside the newly exposed room. The whole thing is 
dark. You shine your flashlight around the opening. As you shine your light 
toward one end of the rectangular door, you almost let go of the flashlight. A 
clown face is grinning at you! You take a deep breath and try to slow your 
racing heart. You look away from those not-so-enticing red lips and begin to 
enter the room. As you inch your way into the dark room, you notice the walls 
seem to be empty. You frown and begin to question your sanity. That extremely 
deadly door must have been guarding something. You take a closer look around 
the room and notice a little black box about the size of your hand. You take a 
closer look at it and see radioactive signs covering the surface. You notice a 
little chord coming out of the box with a big red button on it. You resist 
your human instinct screaming at you to push it and you remove the box from 
the wall. On the other side of the led rectangle you see script. It says:
Custom built for use on C15D21 neutron bomb.
You gasp and as the implications of what this box means begins to sink in, you 
begin to laugh. Not one of those laughs one does after a funny joke, but a 
laugh one has when they become so excited about doing something dangerous that 
it is filled with insanity. You remember all those days when you were a child 
and you were so enthralled with anything that exploded. This box in your hand 
is the culmination of all your destructive childhood dreams mixed together in 
one explosive package!""",
{'bom2': 'Please press 1 to continue.'}),

'bom2':
reader("""You gleefully begin to make your way out the door and back through the 
hallway. You stop right outside the door of the main bridge and peek in. What 
you see makes you real glad you have a weapon of enforced radiation nestled in 
your palm. The green aliens have begun to come together and as they touch, 
they seem to meld into one another. The shape they are creating is a giant 
rotating green blob, filled with around two hundred and fifty of the 
creatures.""",
{'button': """Give in and press the button before throwing the explosive device at the 
creatures""",
'launch': """Launch into the room and begin to tell the aliens how they made such a big 
mistake attacking your ship and that they are all going to die now, slowly and 
with fire. Explain in detail everything that will happen, and once your 
soliloquy is over, press the button.""",
'video': """Take a video with your phone of this crazy creature and send it to your 
family back at central.""",
'drift': """Drift up to the creature and introduce yourself and explain how you are the 
smartest one on the ship and you would be willing to consider a peace treaty 
between the greens and the humans."""}),

'button':
reader("""With a great sigh of relief you let your finger snap to the button, but right 
before you press it down all the way the thought enters your head that you 
don't have an escape plan. You reluctantly let up on the button and think. 
After you press the button you will have two minutes to get into an escape pod 
and blast out of there. The one pod you do know you can fit in is almost on 
the other side of the ship, so you are going to have to use some very fast 
propulsion to get there after you press the button. You know it takes you 
between 4 and 5 feet to slow down and turn. If you manage to hit the wall from 
farther away you either end up stopping or just crashing into the wall. If you 
get closer you crash for sure. You have pretty good depth perception because 
when you are playing Rugby in 0 grav, you really need to be able to estimate 
distance or you will either hit the other players or miss the ball. When you 
get to the little pod you need to destroy the janitor robot, because it only 
lets the captain on the particular pod you are going on. After it is dead you 
can jump in the pod and get out of there.
Press 1 to turn left and 2 to turn right.""",
f.frace(120).starter),

'launch':
reader("""With the bomb in your left hand and the button in your right you shout: 'you 
big green ... alien! I will press this button and you will die! This bomb will 
fill you full of radiation!' You drift farther into the room: 'I don't think 
you know what radiation is do you? It is like invisible death! I press this 
button and not only will you have a miniature sun burning that bulging belly, 
but all the cells in that green carapace of yours will mutate and destroy your 
useless existence! In fact just to show you that you are going to die, I'll 
press the button, then you can know there is no hope for you.'
You press the red button. Nothing seems to happen. You are a little boggled at 
this, so press the button again. You look at the box and notice a little 
digital screen that says 1:43. As you watch the number changes to 1:42. You 
realize that you don't have a good escape plan. You press the button once more 
just so the alien gets the point and leave the bomb right behind the alien. 
You dash out of the room and think faster than you have ever thought before.""",
{'launch2': 'Please press 1 to continue'}),

'launch2':
reader("""The one pod you do know you can fit in is almost on the other side of the 
ship, so you are going to have to use some very fast propulsion to get there 
before the bomb explodes. You know it takes you between 4 and 5 feet to slow 
down and turn. If you manage to hit the wall from farther away you either end 
up stopping or just crashing into the wall. If you get closer you crash for 
sure. You have pretty good depth perception because when you are playing Rugby 
in 0 grav, you really need to be able to estimate distance or you will either 
hit the other players or miss the ball. When you get to the little pod you 
need to destroy the janitor robot, because it only lets the captain on the 
particular pod you are going on. After it is dead you can jump in the pod and 
get out of there.
Press 1 to turn left and 2 to turn right, Go, the clock is ticking!""",
f.frace(90).starter),

'video':
reader("""You take out your phone and press the video record button. You point it at 
yourself and start:
'Hey everyone, I'm in the middle of the planetary exploration ship. It is full 
of holes and aliens, but I'm still alive. None of the other crew members are 
alive they were all turned into these things.'
You point the camera at the spinning creature.
'Now here' You lift the bomb into the picture, 'Is the bomb I am going to use 
to destroy this alien. Please take note that I'm not insane, just desperate, 
there is a difference... Yeah there is a difference.'
You try and think what you should do next:""",
{'button': """Give in and press the button before throwing the explosive device at the 
creatures.""",
'launch': """Launch yourself into the room and begin to tell the aliens how they made such a big 
mistake attacking your ship and that they are all going to die now, slowly and 
with fire. Explain in detail everything that will happen, and once your 
soliloquy is over, press the button.""",
'drift': """Drift up to the creature and introduce yourself and explain how you are the 
smartest one on the ship and you would be willing to consider a peace treaty 
between the greens and the humans."""}),

'drift':
reader("""With the largest grin on your face and your hands holding the bomb behind your 
back, you drift into the room.
'Excuse me ... alien blob, my name is %s and I would just like to thank you for 
getting rid of all the other crew members. They really weren't that smart. 
They couldn't do half that I can do. I would like to propose a treaty between 
you guys, the greens, and us, meaning me, the humans. This treaty of course 
would need to be properly drafted and signed, but if we could just sit down 
and discuss this like the civilized, thinking beings we are, I know we can 
work something out that will be acceptable to both of us. You pull the bomb 
from behind your back. 'This is so not what it looks like. I would like to 
give this to you as a trust of faith. This is the most powerful weapon on the 
ship and I would like to give it to you.' You drift a little closer and hold 
the bomb out.""",
{'drift2': 'Please press 1 to continue.'}),

'drift2':
reader("""'Please take this... and stop spinning, you're making me feel 
sick... But if that is how you think I guess I will need to get used to it... Have 
you even heard a word I've said?' You watch the creature just spinning in 
circles and give a sigh of frustration. You glance down at the bomb and notice 
a screen that says 1:01. As the realization sets in that you must have pressed 
the button while you were giving your impassioned speech, the number changes 
to 1:00. You go as fast as you can out into the hall and regretfully turn your 
mind away from winning a piece prize for contacting the first alien race and 
drafting a treaty with them so they wouldn't attack the world, to figuring out 
a way to escape.""",
{'drift3': 'Please press 1 to continue.'}),

'drift3':
reader("""The one pod you do know you can fit in is almost on the other side of the 
ship, so you are going to have to use some very fast propulsion to get there 
before the bomb explodes. You know it takes you between 4 and 5 feet to slow 
down and turn. If you manage to hit the wall from farther away you either end 
up stopping or just crashing into the wall. If you get closer you crash for 
sure. You have pretty good depth perception because when you are playing Rugby 
in 0 grav, you really need to be able to estimate distance or you will either 
hit the other players or miss the ball. When you get to the little pod you 
need to destroy the janitor robot, because it only lets the captain on the 
particular pod you are going on. After it is dead you can jump in the pod and 
get out of there.
Press 1 to turn left and 2 to turn right, Hurry, the clock is ticking!""",
f.frace(60).starter),

'f2':
reader("""Press 1 to kick the janitor, 2 to pull parts off the janitor and 3 to see the 
janitor's health.""",
f.ff2),

'blast':
reader("""You throw open the pod and jump in. You pull the hatch shut and palm the launch 
button. You feel the comforting press of acceleration as you leave the mother\nship.
You float into space.
You wait for the fireball.""",
f.fblast),


'winner':
reader("""
CongradulationsYou have won!
You are the final one!
""", {'main_menu': 'Please press 1 to go back to the main menu.'}),

'death':
reader(f.fdeath, f.fdeath2),

'main_menu':
reader(f.fmain_menu, {'load': 'Load a saved game.', 'start': 'Start a new game.', 'quit': 'Exit.'}),

'load':
reader("You have chosen to load a saved game.", f.fload),

'start':
reader("""**********
Final1
To save your progress press s at any time. If you would like to quit press q 
and if you wish you can press return instead of pressing 1 to continue. To 
repeat this message in the game press h.""", {'Pre_intro': 'Please press 1 to continue.'}),

'quit':
reader("Are you sure you wish to quit?", f.fquit),

}
