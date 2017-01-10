#These are the functions for the scenes
import globals, functions
from time import sleep
from functions import choice
from random import randint
from threading import Timer, Thread
from race import race_loop
from fight1 import fighter, cat, ninja
from fight2 import fight2_start
from sys import exit

n = 'Joe'
skip = False

def intro():
	"""creates a name for the player"""
	global n
	print "Welcome to Final One!"
	print "By Frastlin"
	globals.player_name = functions.name_maker()
	n = globals.player_name
	print "Thank you %s, your story begins." % n

def fact2():
	sleep(1)
	print """Two hundred thousand miles till we are in surface viewing range. 
Jennifer do you have a status report on the radio signal activity around the 
planet?"""
	sleep(4)
	print """Nothing out of the ordinary captain,
the only unique thing about this place is the lack of asteroids in the area. I 
have been watching our M25 out 
of the view screens for the last few hours and I have not seen one
asteroid hit our field. This is not a professional report though.
Just a fellow thumb twiddler's observation."""
	sleep(7)
	print """Roger Jenny, Sam, how's your sun's game coming? That was rather 
ingenious to
play baseball in 0 gravity. Gives a little taste of Earth."""
	sleep(5)
	print "Hey Ward, what's up?"
	sleep(2)
	print """Hey captain, I think I found an anomaly in the area. Jenny's 
asteroid comment is spot on;
there is no debris in the area, just the moons and 
planets. This is really odd. Would you like me to alert central?"""
	sleep(5)
	print """I think we should wait till we get closer into the orbits of the 
planets;
this may just be a very clean area of space. That could account for 
the many smaller planets around the suns."""
	sleep(4)
	print """Good point, shouldn't base everything off our solar system. We're 
not quite close enough yet to start seeing much debris from other stars."""
	sleep(4)
	print """Hey captain, I am sending %s up to you with a printout I would like 
you to look at in hard copy. Map 9 is displaying funny. I would like you to 
take a look at it and tell me if it is these old eyes playing tricks on me, or 
if we should have the engineer's take a look at it.""" % n
	sleep(8)
	print "Thanks Sylvan, %s just ran into the room. What do you have %s?" % (n, 
n)
	sleep(4)
	print """Captain, we were looking at the different planets around the stars 
and noticed a very interesting anomaly. Do you see this lighter spot next to 
planet 23? It doesn't show up on the computer screen, but the printer 
evidently thought there was something there. We just thought it was one of the 
moons, but it looks like it is some kind of dark black shiny alloy. I doubt it 
could be carbon based because that would not reflect light like this. It 
almost looks polished. We tried to get a closer view of it, but when we tried 
focusing our telescopes on it, we were getting blank space readings. It 
doesn't seem to be doing much, which is why we didn't notice it before.
"""
	sleep(15)
	print "What do you think captain? Should we report this to central?"
	sleep(3)
	print """Yes, let's send a message to central asking them if they
 can get a 
closer look on it. Perhaps we can investigate it after we do a sweep of the 
planet."""
	sleep(6)
	print """Hey captain we just printed out another copy of map 9 and the black 
spot has tripled in size in the last 10 minutes. It is still not being picked 
up by the computers. I am sending a message to central and we'll see what they 
have to say. I am still not sure of the size, but currently it looks as large 
as the planet in our view screens."""
	sleep(8)
	print """Thanks Silvan, hey %s, can you go grab the new print out from the 
printer, I am interested to see the new dimensions of our strange little 
friend.""" % n
	sleep(6)
	print """Captain, something has managed to enter the disrupter field and is 
heading straight for us! I can't tell what it is, but if we don't manage to 
change our trajectory we will collide at a good solid ten thousand miles a 
second! I'm not sure how fast it is moving, but our speed alone is enough to 
vaporize us!"""
	sleep(10)
	print """Sam, is there any way you can launch some kind of projectile at the 
object?"""
	sleep(4)
	print "I hoped I could have heard the end of the baseball game..."
	sleep(2)
	print """If something is moving that fast, there is no way we will be able to 
move out of any 
possible collision."""
	sleep(4)
	print """Captain, I've checked the systems, but without any kind of automated 
targeting system, there is no way I could even consider hitting them. The best 
I could do is move the ship a little, but that is rather scary. Sylvan how 
close is the thing now?"""
	sleep(5)
	print """%s is on the way to show you captain, Sam I don't think there is 
anything we can do, we are heading straight for it and it is approaching at a 
good ten thousand miles per second. It should be here any moment.""" % n
	sleep(7)
	print """Thanks Sylvan, Sam, Jenny, Ron, everyone aboard the shuttle, I have 
sent repeated messages to command central, but it will be a few minutes before 
we hear anything back. By then we will be singing with the angels."""
	sleep(7)
	print """Haha! I don't think the angels could stand hearing me sing, they 
would probably throw me out of heaven faster than you could say 'oh 
god!'..."""
	sleep(5)
	print """Captain! The view screen has gone black and all instruments read 
null! I believe we have collided with the object. All system alarms are taking 
over, our oxygen level is unreadable, I have no idea wh.e.l..i.f.."""
	sleep(6)

def fact1():
	print "Please press 1 to read the scene or 2 to skip it."
	c = choice(2)
	if c == 0:
		fact2()

def fbridge3():
	sleep(2)
	print "*BOOM!!!*"
	sleep(3)
	print "The world goes dark"
	sleep(3)
	print """You awake to a strange fast percussive ha sound coming from all 
around you from many different places. The sound of many soft objects smacking 
against the metal hull make you reluctant to move from the protective shield 
that your partially closed capsule provides.
You close your eyes and take stock of your situation:
You must have air that is somewhat breathable because you are awake and 
hearing sounds.
Whatever breached the hull of the ship did so in a place the same temperature 
that humans can live at."""
	print "Please press 1 to continue."
	choice(1)
	print """
Whatever is in the ship is definitely not human and is technologically 
advanced enough to snatch a ship moving at ten thousand miles a second in 
space and gain control of it.
If the rest of the crew is alive, they are either on their way to command 
central, are stuck in their capsules, waiting for the launch sequence to 
trigger, or are in the custody of whatever captured the shuttle.
You take a deep breath and open the lid an inch and peep over the side."""
	print "Please press 1 to continue."
	choice(1)
	print """
You 
almost shout aloud in startlement, the percussive 'ha' sounds that fill the 
air come from large round globes that have the appearance of giant smiley 
faces. The faces are most definitely not human, the round blobs that float by 
as you stair are between two feet and six feet in diameter and are a pail 
green color. Each creature emits a soft glow that is enough to make the ship's 
interior visible. Two massive holes gape in the outer walls, showing where the 
creatures entered. As you watch a massive six foot blob squeezes through the 
small two foot wide hole in the hull. It reminds you of an octopus fitting 
through holes that look much too small for its massive body to ever squeeze 
through. When the massive green globe resumes its natural shape again, you 
take a closer look at its features."""
	print "Please press 1 to continue."
	choice(1)
	print """
The most prominent part is a big long slit in the middle of the creature that 
can either bend one way or the other in a crescent. On one side of the 
crescent cavity there are two smaller crescents that either shrink to small 
slits when the larger crescent bends toward them, or come closer together and 
become almost square when the large crescent is curved the other way. The 
inside of the crescent is black, so that must mean that the glow comes from 
the skin, rather than from some internal source. The creatures use the lack of 
gravity to move around. The 
Fleshy smack against the metal of the hull is created when the creatures 
connect with the exposed surfaces of the ship."""
	print "Please press 1 to continue."
	choice(1)
	print """
As you watch, a smaller than normal creature with the crescent pointing away 
from the two black spots that resemble more of a square, floats to the hole 
and begins to block any more creatures from coming in. You watch for a while 
and after about what seems like fifteen or twenty minutes, no creatures other 
than the little green fella appear. You decide to slowly open the lid
and emerge from your protective capsule.  
	"""

def fjoke():
	print """
You are struck by inspiration, this is the first alien race seen by humans! 
You put on your most ingratiating smile and think to yourself that you are 
going to be the first to talk to an alien!
Thinking for some reason of a garden you burst out:
'Take me to your weeder!'
You pause and think back over what you just said... Did you really ask the 
creature to take you to their 
weeder? You gasp in horror and try to cover up your laps in decorum. You reach 
out your hand and introduce yourself:
'Hello, I'm %s and am really sorry, I meant take me to your litter, it is a 
movie reference about cats.'
What! You begin to blush, This is so not going the way you planned, weeder, 
litter, cats? The green face hits the wall to the side of your head and you 
turn toward it:
""" % n
	print "Press 1 to continue."
	choice(1)
	print """
'My favorite button on the keyboard is the spacebar!'
You just wish the ground would swallow you up. All you can manage to do is 
stick a larger space boot into your mouth every time it opens. You open your 
mouth for one more go.
'This heater room is a rather unique space to meet my first alien, where did 
you guys park? We couldn't even find any parking meteors on any of our maps.'
You shut your mouth with an audible snap. Parking meteors really? Your mind 
races to think over what you have said and you just can't help yourself 
anymore. You burst into laughter, you just sounded so ridiculous!
You look up with tears of mirth streaming down your face and notice that the 
frowning looking creature is no longer frowning looking. The crescent slowly 
reverses direction and you hear a loud 'ha!' come out from inside the 
crescent. It is soon repeated by more 'ha' sounds and you realize the creature 
is laughing along with you.
As you wipe your tears from your eyes you see that the creature is spinning 
around, laughing as if there is no tomorrow. Grinning you head toward the main 
bridge where most of the other capsules are.
"""

def flogic():
	c = choice(8)
	if c == 3:
		return {'laser1': 'Please press 1 to continue.'}
	else:
		return {'logicd': 'Please press 1 to continue.'}

def fdesk4():
	print """You take a closer look at the items taped on the wall:
This is a picture of a blue sword. Under the sword reads the inscription:
"Whomsoever takes up this blade shall wield power eternal. Just as the blade 
rends flesh, so must power scar the spirit."
WOW, inscription under Frostmourne
On the blade of the sword there is some glossy plastic and a small red dot is 
sticking out. You touch the red dot and a baby's giggling comes from somewhere 
in the room.
The sheet of paper reads:
Onboard neutron Bomb entrusted to Sam Forze for use on C15D21.
Note this neutron bomb is meant to exterminate every living organic creature 
on the ship. The timer will last for two minutes and can either be tied to a 
carrier or detonated by hand. The bomb itself is fairly safe if handled, but 
because of the ease of activation, the bomb will be in a case.
The bomb will release radiation till it reaches vacuum. The radiation then 
stays on the outside of the hull till the metal has become enough unstable 
that a second blast of particles can trigger a nuclear explosion of the whole 
ship.
"""
	globals.sword_pressed = True
	check_turn()

def fpoke():
	check_turn()
	if globals.sword_pressed:
		print """
You poke the eye of the white haired guy and find the texture rather smooth. 
You then poke around the sword and the guy's arm. As you poke the center of 
the blue sword you hear a click and the door swings open.
"""
	else:
		print """
You head over and poke the guy with the white hair's eye. The surface feels 
rather smooth and you wonder if it is like a touchpad of some kind. You start 
poking the guy in all different places and eventually give up and retreat.
"""

def fpoke2():
	check_turn()
	if globals.sword_pressed:
		return {'break': 'Enter the metal door.', 'laser2': 'Find another door.'}
	else:
		return {'md': 'Please press 1 to continue.'}

def fbeer():
	if globals.beer_count >= 10:
		globals.beer_count += 5
		print """
You swig your next beer and know you are invincible, You think to yourself: 
"Thoss alierns will pay! Il blasht dem, blasht dem!!!" You somehow find 
yourself facing a crazy clown face and let out a startled laugh. You hug the 
clown and pat it on the back: "Thatch a good budshy." You find Da Big Gun and 
bump your way out the door. You realize you left the bullets back in the room. 
You stumble back into the room and realize you can't remember where Da Gun 
was. You find a bag of some likely looking ammo and make your way back out to 
the hall. You fumble with the loading mechanism, pulling out bits and pushing 
buttons. You just decide to put the ammo you found into the barrel of the gun. 
You stuff a round piece of ammo down the barrel and with a chuckle to yourself 
open the door. 'ya shee dish ya big green shucker? You'rs gown to be blown up! 
Here ish my big gun, hear it rore!!!'"""
		print 'Please press 1 to continue.'
		choice(1)
		print """
You pull the triggers and nothing happens. You begin to start laughing 
manically and look up. The giant green blob is slowly spinning towards you. 
You start pulling ammo from the bag you found and start throwing them at the 
blob. The blob doesn't seem to notice. You begin to sober up, but right before 
the green blob reaches you, you hurl Da Big Gun at the creature. The gun clips 
the green creature's side, but does little noticeable damage. At this point 
you think it would be a good idea to probably run away. You turn and run smack 
into the little creature you met when all this began. It doesn't look too 
happy to see you. You reach out to pat it on its membrane and as you touch it, 
you are treated to one of the most intense shocks of your life. It is so 
strong that you black out."""
	else:
		print """
You grasp one of the chilled cans and pop the top. The refreshing fizz fills 
your thoughts. You take a nice swig and look around for something else to 
fiddle with."""
		globals.beer_count += 1
		print "You have had %s beers so far." % globals.beer_count

def fbeer2():
	check_turn()
	if globals.beer_count < 13:
		return {'ping-pong': 'Please press 1 to continue.'}
	else:
		return {'death': 'Please press 1 to continue.'}

def fchill():
	check_turn()
	print """
A blue game controller? You reach over and grasp the controller with both 
hands. The whole room goes dark and a game screen is projected one hundred 
and eighty degrees around you. The words scroll across the screen:
'Welcome back!'
You grin to yourself as you lounge in your chair. The thought enters your head 
that you are probably way better at playing games than any old weapons expert.
The screen shows up with the heading
'Sarcan the Rat King'
'Fight!'"""
	print "Please press 1 to continue."
	choice(1)
	print """
A giant rat head slowly lifts out of the floor and a massive tail comes 
swinging around to whap your right side of the room. As the tail hits there is 
a smack sound and the game controller vibrates in your hand. A red number 9 
flashes in front of you and your eyes are drawn to the numbers on the ceiling. 
It says Socanda 91HP-100En, Rat King 100HP-90En.
You start pressing the buttons on the controller. The first button you press 
sends a large fist smashing into the rat king's face. Another red number 13 
appears and the numbers above the battle ground reflect the new totals.
Socanda 91HP-90En, Rat King 87HP-90En
The giant head lifts out of the ground and a large mouth of sharp glistening 
teeth comes at you.
CRUNCH!
A red 15 shows up for a few seconds and goes away.
Socanda 76HP-90En, Rat King 87HP-70En
The next button you press sends a large leg swinging from the wall to bunt the 
Rat King's backside.
CADUNK
18
Socanda 76HP-70En, Rat King 69HP-70En"""
	print "Please press 1 to continue."
	choice(1)
	print """
The rat king takes a deep breath and lets out a really loud shriek.
You notice two hands on either side of you, pressed against something.
That must mean you covered your ears.
0
Socanda 76HP-70En, Rat King 69HP-40En
The next button you press sends a massive head hurling at the Rat King.
A loud 'splat' resounds and the Rat King looks a little dazed.
30
Socanda 76HP-40En, Rat King 39HP-40En
The Rat King curls into a small ball and goes to sleep.
Socanda 76HP-40En, Rat King 39HP-55En
You guess the last button on the controller is to have you nap as well. You 
press it just to make sure.
A loud snoring comes out of the speakers and the rat king gets up.
Socanda 76HP-55En, Rat King 39HP-55En
The rat king swings his tail at you.
SPLAT!
10
Socanda 66HP-55En, Rat King 39HP-55En"""
	print "Please press 1 to continue."
	choice(1)
	print """
You think that you really liked that head bash, so you press that button 
again.
A giant head goes hurling toward the Rat King.
The rat king side steps and your head goes Wham on the floor.
Socanda 56HP-55En, Rat King 39HP-55En
The Rat King opens his mouth and lunges toward you.
CRUNCH!
20
Socanda 36HP-55En, Rat King 39HP-55En
You choose to kick the Rat King.
You deliver a massive roundhouse kick to the Rat King's backside.
CADUNK
25
Socanda 36HP-35En, Rat King 14HP-35En
The Rat King takes a deep breath and lets out a blood curdling shriek!
SCRITCH!
35
Socanda 1HP-35En, Rat King 14HP-5En"""
	print "Please press 1 to continue."
	choice(1)
	print """
You deliver a solid punch to the head of the Rat King.
10
Socanda 1HP-25En, Rat King 4HP-5En
The Rat King curls up to go to sleep.
Socanda 1HP-25En, Rat King 4HP-20En
You deliver a solid punch to the head of the Rat King.
12
Socanda 1HP-25En, Rat King -8HP-5En"""
	print "Please press 1 to continue."
	choice(1)
	print """
The message
'WINNER!'
Flows across the screen. You grin to yourself, oh yeah you are good."""

def fchill2():
	print """
'Sarsa the paw not-so-maiden of cats!'
'Fight!'
A small dainty cat strolls past the screen."""

def fchill2_2():
	check_turn()
	r = fighter(cat)
	if r != 'winner':
		print """
You frown to yourself, that wasn't supposed to happen... There must be an error, 
you can't lose."""
		return {'chill3': 'Start again.', 'break': 'Go explore something else.'}
	else:
		print "Winner!"
		return {'break': 'Explore something else.', 'chill4': 'Meet your next challenge!'}

def fchill3():
	print """
The room goes dark and a bright flash of lightning reveals a silhouette of a 
human figure with one arm above its head and its other arm in front of its 
face. The figure's legs are shoulder with apart.
A loud thunder crash sounds and the screen goes black. The white words:
'E-Con, ninja level %d'
Appear on the screen.
The light slowly comes up on a young man? In black tights?
'Fight!'""" % globals.number2

def fchill3_2():
	check_turn()
	m = fighter(ninja)
	if m != 'winner':
		print """
You frown to yourself, that wasn't supposed to happen... There must be an error, 
you can't lose."""
		return {'break': 'Go back to the break room.', 'chill': 'Just chill.', 'chill4': 'fight again.'}
	else:
		print "You have defeated all your challengers!"
		return {'break': 'Explore something else.', 'chill': 'Chill some more.'}

def ffiddle2():
	cl = ['red', 'blue']
	dl = ['Deathwish', 'Theobroma cacao mixture', 'with lace']
	cn = cl[randint(0, 1)]
	dn = dl[randint(0, 2)]
	print """
You snatch a cup out of the tube and open the powder container marked %s. You 
find a little spoon in there that you use to scoop 3 spoonful's into the cup. 
You fill the cup from the %s container and mix the liquid and powder together. 
You take a big drink.""" % (dn, cn)
	if cn == 'blue':
		print "You spit out the mixture. 'Bleh!'"
	else:
		print "You lick your lips. That is good!"
	check_turn()

def fkeypad():
	print "Hit return to cancel."
	s = '%d%d%d%d' % (globals.number1, globals.number2, globals.number3, globals.number4)
	print "You have %d trys remaining." % globals.turn
	ps = raw_input("[keypad] > ")
	if ps == "":
		print "Canceled."
		return {'laser2': 'Please press 1 to continue.'}
	elif ps == s and globals.turn != 0:
		print """
A slight humming sounds from inside the room and the lasers blink out. 
You did it!"""
		return {'laser2': 'Leave and let the field flash back on.', 'bom': 'Enter the room.'}
	elif ps != s and globals.turn != 1:
		print "BZZT!"
		globals.turn -= 1
		return {'keypad2': 'Please press 1 to continue.'}
	else:
		print "BZZT!"
		return {'keypad3': 'Please press 1 to continue.'}

def check_turn():
	if globals.turn < 4:
		globals.turn += 1

class frace(object):
	def __init__(self, time):
		self.time = time
	def begin(self):
		t = Timer(self.time, explode)
		globals.tt = t
		t.start()
	def starter(self):
		print "Please press 1 to continue."
		choice(1)
		globals.current_scene = 'racing'
		print "You shoot into the first hall."
		self.begin()
		race_loop()
		if globals.boom == False:
			return {'f2': """As you not-so-gracefully hit the side of the small docking bay, you see the 
little janitor robot coming after you. It thinks that you are trash!
Press 1 to continue."""}
		else:
			return {'main_menu': 'Please press 1 to go back to the main_menu.'}

def stop(self):
	self.time.cancel()

def ff2():
	if globals.boom == False:
		r = fight2_start()
		if r == True and globals.boom == False:
			return {'blast': 'Jump into the pod!'}
		elif globals.boom == True:
			return {'main_menu': 'Please press 1 to go to the main menu.'}
		else:
			frace(globals.tt).stop()
			return {'death': 'Please press 1 to continue.'}
	else:
		return {'main_menu': 'Please press 1 to go back to the main menu.'}

def x_checker():
	return globals.boom

def fblast():
	globals.blaster = True
	x = x_checker()
	while x != True:
		sleep(randint(3, 6))
		print "You drift."
		x = x_checker()
	globals.tt.join()
	return{'winner': 'Please press 1.'}

def explode():
	globals.boom = True
	if globals.blaster == False:
		print """
A bright light fills your whole body and as your world becomes fire you hear a 
massive boom. Light becomes so bright that it becomes black.
perhaps next time you will be faster at flying in zero grav."""
		globals.boom = True
		return {'main_menu': 'Please press 1 to go back to the main menu.'}
	else:
		print """
You feel a vibration as the ship behind you explodes. You feel the metal 
around you grow quite a bit hotter. This is kind of worrying because the hull 
is supposed to be insulated against just about anything. You hold your breath, 
but nothing seems to happen for a while. You let out your breath and grin to 
yourself. You made it! You are alive! You are the last one on the ship and the 
final one to get off the ship.
As this thought fills your mind you hear the collision jets turning on. You 
glance at the read-out telling the status of the pod. You groan to yourself. 
Your pod is detecting the surface that keeps the oxygen in the area around the 
aliens.
You think about what to do:"""
		print "Press 1 to continue"
		choice(1)
		print """
The aliens were able to get the ship into the bubble, so it must open 
somewhere. The oxygen doesn't escape, so that means the membrane must be 
pretty solid. As you are thinking the surface suddenly contracts and you hear 
a smack as it hits the hull of your ship. The collision jets spurt, but 
whatever the membrane is it is everywhere. Suddenly you feel acceleration 
again. You rub your eyes just to make sure your eyes aren't playing tricks on 
you. The bubble is moving away from you. You aren't in it anymore... You are 
free!!!
You are the final won!!!"""

def fdeath():
	death_scenes = [ds1, ds2, ds3, ds4]
	death_scenes[randint(0, len(death_scenes)-1)]()
	print "Thank you for playing!"

def ds1():
	print """
You come to your senses and find yourself back in your bunk on CD. You feel 
yourself, making sure you are all there and you suddenly remember that the 
planetary shuttle is going to be heading down to investigate the planets 
around the suns. Remembering your dream, you sit up as fast as you can and 
forget that the bunk above you is only two feet up. The next thing you know, 
you are in the medical bay and you are shouting for the captain to come to you 
and not to go down to the planets.
Sadly the planetary shuttle departed almost three hours before and it would be 
a significant amount of trouble to turn the ship around and bring it back.
The nurse assigned to you smiles dotingly on you and you forget everything 
about your earlier dream and enter into another state of mind where all you 
can think of is the perfect face in front of you."""

def ds2():
	print """
You wake up and you find yourself being carried by the green creatures. You 
begin to struggle remembering the insane alien you saw last, but the grasp the 
creatures have on you is unbreakable. This prompts you to look around and take 
stock of your situation. The creatures have each of your arms and legs grasped 
into their large crescent, making it seem as if all your limbs end in a ball 
shape. They are taking you through a dark metallic tunnel and you presume you 
are in the object indicated on the map. You suddenly realize your body is 
throbbing all over with pain. You shut your eyes and try to will away your 
pounding headache and when you open your eyes you instantly close them again. 
What you saw could not be real. You slowly open your eyes and look around in 
amazement, gasping at the improbability of what your senses are telling you."""

def ds3():
	print """You awake to darkness. Darkness all around. You flail in all directions, but 
no matter where you turn you feel nothing. You remember some song about 
floating, just floating along from earth, but you ask yourself why you are 
thinking about floating when you should be panicking. You start to take fast 
shallow breaths and flailing your arms spasmodically in all directions. You 
begin to see stars and a primal scream begins to build up in your throat. Your 
legs begin to jerk and kick. You feel a warm fluid dripping down your leg and 
you are sure you hear maniacal giggling from all directions. You realize you 
are in free-fall and if you were to encounter some hard object, you would 
probably be hurt rather bad. Your heart rate has increased to a point to where 
it feels as if someone shot you with several doses of adrenalin. You open your 
mouth to let the world know just how crewel it can be and open your eyes."""
	print "Please press 1 to continue." 
	choice(1)
	print """
The scream is torn out of your throat not because of the darkness, but because 
right in front of your face is a beastly visage so ugly and terrible that it 
makes your aunt Gronko look angelic.
SPLAT!!!
A sweet sticky substance coats your face. You end up taking a large mouthful 
and realize that the face that so scared you was the Halloween decorated cake 
the cook of the C15D21's galley had baked the night before. You realize that 
you are going to be in huge trouble with the formidable woman. You extract 
yourself from the gooey mess and eat the larger chunks that persistently 
adhere to your face rather than letting them go to waste.As you drift """
	print "Please press 1 to continue."
	choice(1)
	print """
backwards away from the demolished cake, you ask yourself how you managed to 
get in this sticky situation in the first place. You grasp one of the passing 
rails and make your way to the shower rooms. You undress and as you wash the 
warm sticky frosting off your face, you surmise that you must have not 
fastened your free-fall belt correctly to your sleeping bunk. The strange 
grinning aliens were just a nightmare and everything is all right.
You throw your soiled clothes into the laundry shoot and drift back to bed. 
The open sleeping bunk looks inviting and you gratefully slide into the warm 
covers. You make sure this time you are securely fastened and as you drift off 
to sleep you notice a green light shining through your closed eyelids and the 
sound of a percussive "Ha" seems to come from just outside your bunk, but at 
that point sleep claims you and you know nothing more."""

def ds4():
	print """You open your eyes and feel an irresistible urge to laugh. There are a 
multitude of green creatures around you and they are all giggling 
uncontrollably. You feel your mouth open and close as the percussive sound 
explodes out of your middle. You begin to rotate, thanks to the zero gravity. 
Soon you find yourself drifting among the glowing green aliens. Slowly the 
crowd begins to exit the ship. They begin to slip out of the holes and as you 
follow a thought fleetingly comes, wondering how you managed to squeeze 
through an opening three inches in diameter."""


def fdeath2():
	return {'main_menu': 'Please press 1 to return to the main menu.'}

def fquit():
	if raw_input("Press y to answer yes and any other key to answer no: > ") == "y":
		functions.leave()
	else:
		return {'main_menu': 'Press 1 to go back to the main menu.'}

def fload():
	print """Please choose your saved game from the list below. If you wish to delete a
saved game, choose it and hit delete from the next menu:"""
	f = functions.list_saves()
	c = choice(len(f)+1)
	if c == 0:
		return {'main_menu': 'Press 1 again to go back to the main menu.'}
	else:
		c -= 1
		sav = f[c]
		functions.restore(sav)
	if globals.current_scene == 'main_menu':
		return {'main_menu': 'Press 1 to go back to the main menu.'}
	else:
		return {globals.current_scene: 'Press 1 to go to your saved location.'}

def fd2():
	print """Crisco:
Top of his class from Andromeda University in combat systems and battle 
simulators. Crisco has developed CON FI, the combat Orientation Navigation 
Fighter intelligence used in almost all homing missiles. He just recently has 
taken up a pursuit in destructive chemistry, but has shown very little 
aptitude for it so far.
Ray (Rays):
Ray graduated with a double major in defensive security systems and music. His 
systems have been used in the White house and the labs of Histro INC. He has 
stated that number %d is his favorite number and he often puts his favorite 
number in any of his creations. He is the ship's WEAPs specialist with a focus 
in A. The music he is particularly into happens to be Mozart, Wagner and 
Puccini.""" % globals.number3

def fd3():
	print """Letters to love:
Dear my beloved,
Your eyes shine in my dreams; your heart is music to my ears. I dream of just 
one brush of your skin, not even caring if it is the soul of your foot. I hear 
your laugh when I am sitting alone in my chair. You have stolen my being and 
all my life is for you
Fair queen of the night, the moon shines on your hair and your skin glows from 
the light of the stars. I could gays for hours on such sublime beauty. The 
smell of you brings me higher than anything else could ever do. To say my 
heart bursts is like saying a water balloon pops when the ocean is poured into 
it. With you in the night the universe needs no other light.
Pictures of a woman... Oh my...
Sheet music for a song called %dP Ways...
%d ways I can love you,
I can love you *******
The rest of the song is scratched out as if the writer was unhappy with his 
writing.""" % (globals.number4, globals.number4)

def fp2():
	print """The next paper reads:
Memo to Crisco
I keep telling you that w is %d! You have got to let W be itself or the lab 
goes boom! I don't have problems with boom, but not in my room!
Thank you Sir, I know W is kind of important to the reaction, but I guess I 
didn't make it a high enough priority.
Crisco, W is the most important part of the formula; you have got to remember 
your WEAPs! This is elementary stuff, I am requiring you to retake module 4 
from section 5 in the training manual. We can't have this happening any more.""" % globals.number1

def fmain_menu():
	print "Welcom to Final1."
	print "Press a number and hit return to choose an option."
