#This is the simple turned based system in the lounge

from functions import choice
from globals import number2
from random import randint

#The hp and default fo
fo = 'The Rat King'
mhp = 100
php = 100
men = 100
pen = 100

class engine(object):
	def __init__(self, name, oname):
		self.name = name
		self.oname = oname
	def hit(self, first_message, hit_message, miss_message, ac, str, co):
		"""A pretty ginaric fighter, takes the weapon object and delivers a number. Dammage here is +10, so if I wish, I could make another argument and put that as the hit range. You need to put any list into this function with *listName so it can unpack the list."""
		print(first_message.format(self.name, self.oname))
		didHit = randint(1, 10)
		dammage = randint(str, str+10)
		if didHit == 10 and dammage == str+10:
			print "CRITICAL HIT!"
			a = str+10
			crit = 2*a
			print(hit_message.format(self.name, self.oname) + " %s") % crit
			coster(self.name, co)
			return crit
		elif didHit <= ac:
			print(hit_message.format(self.name, self.oname) + " %s") % dammage
			coster(self.name, co)
			return dammage
		else:
			print(miss_message.format(self.name, self.oname) + ' 0')
			coster(self.name, co/2)
			return 0
	def sleep(self, message):
		print(message.format(self.name))
		return 15
	def who(self):
		return self.name

#These are just short aliases to call the class with sertan values.
ninja_name = 'E-Con, ninja level %s' % number2

cat = engine('Sarsa the cat paw not-so-maiden', 'you')
ninja = engine(ninja_name, 'you')
player = engine('you', fo)

#These are all the attacks. I could add more if I wished, but these are fine for now
punch = ['You lift your hand to punch', 'You deliver a solid punch to the head of {1}.', 'You swing your fist at {1}, but epicly miss.', 9, 8, 10]
kick = ["You choose to kick {1}.", "You deliver a massive roundhouse kick to\n{1}'s backside.", "You swing your leg, but mannage to only hit the air.", 7, 15, 20]
headbut = ["Your giant head goes hurling toward {1}.", "A loud 'splat' resounds and {1} looks a little dazed.", "{1} side steps and your head goes Wham on the floor.", 4, 30, 30]
psleep = ["You begin to furiously saw the rafters."]

bat = ["{0} lifts up a dainty black paw.", "Faster than lightning {0} brings it down, lacerating your side.", "With a glint in her eye {0} slashes the air right in front of your nose.", 8, 10, 10]
pounce = ["{0} crouches down.", "With a tremendous yowl {0} springs at you, landing \nwith all 900 pounds of feline fury on top of you.", "With a tremendous yowl {0} springs at you, but\nseeing 900 pounds of cat coming at you does wonders for your speed and\nyou dodge to the side.", 5, 20, 40]
legkick = ["{0} rolls onto her back and splays her legs out.", "Thinking you can get an extra punch in you bring your fist down. \n{0} grabs onto your fist with her two front legs and with her back legs she speedily rakes her claws repeatedly along your upper body.", "Thinking there is some kind of trap involved you avoid getting anywhere near the seemingly relaxed cat.", 1, 40, 40]
csleep = ["{0} curls into a ball and closes her eyes."]

chop = ["With a cry {0} raises his hands up in the air.", "As if his girlfriend was right behind him, {0} brings both his hands down, delivering a powerful double chop to your body.", "As if his sensei was scrutinizing his every move, {0} weekly\nflicks his hands out, failing to even come close to hitting you.", 5, 15, 10]
fly = ["{0} takes a few quick steps back.", "With a shout, {0} comes racing toward you and launches himself into the air. With a crack his foot connects with your chest, nocking you down.", "With a shout, {0} runs forward but trips over his own feet and goes sprawling.", 2, 35, 40]
firebreath = ["{0} takes a bottle of some red liquid from his gi and gulps\na mouthful.", "Opening his mouth as wide as it can go, {0} lets out a huge \ngout of flame that burns strait for your poor hair.", "Opening his mouth as wide as it will go, {0} begins to cough. A big blast of flame explodes, scorching {0}'s eyebrows.", 1, 50, 40]
nsleep = ["{0} falls over, apparently dead to the world. Too bad it\ndoes not count."]

def coster(name, cost):
	"""Calculates the energy cost of an attack for both the player and the mob"""
	global pen
	global men
	if name != 'you':
		men -= cost
	else:
		pen -= cost

def headbut_miss(num):
	"""The headbut costs HP if the player misses, so this class calculates that"""
	global php
	if num == 0:
		php -= 10
		return 0
	else:
		return num

def player_turn():
	"""is the player's turn. it prints and calls the combat class. This is because printing with something like the mob's fighting class would be very dificult."""
	global pen
	l = [punch, kick, headbut]
	print "1. punch"
	print "2. Kick"
	print "3. Head but"
	print "4. Sleep"
	while True:
		x = choice(4)
		if x == 3 and pen < 85:
			pen += player.sleep(*psleep)
			return 0
		elif x == 3:
			print "You are too full of energy!"
		elif pen - l[x][5] >= 0 and x == 2:
			return headbut_miss(player.hit(*l[2]))
		elif pen - l[x][5] >= 0:
			return player.hit(*l[x])
		else:
			print "You don't have enough energy."

def cat_turn():
	"""The reason why I have two mob turns is because of the list of attacks. I could have put this list in an __init__ call, but didn't"""
	global men
	l = [bat, pounce, legkick]
	x = randint(0, 3)
	if men >= 85 and x == 3:
		x = randint(0,2)
	if x != 3 and men - l[x][5] >= 0:
		return cat.hit(*l[x])
	else:
		men += cat.sleep(*csleep)
		return 0

def ninja_turn():
	"""The reason why I have this in its own function rather than calling it in an __init__ is because of the sleep, it would have been rather anoying to have to calculate the random number and pull sleep from the above class, It could be done, but I didn't do it here."""
	global men
	l = [chop, fly, firebreath]
	x = randint(0,3)
	if men >= 85 and x == 3:
		x = randint(0,2)
	if x != 3 and men - l[x][5] >= 0:
		return ninja.hit(*l[x])
	else:
		men += ninja.sleep(*nsleep)
		return 0

def op_set(op):
	"""This sets fo to what ever is the argument. This is because if I set it in another function, the global would still be what the fo was when the game started."""
	global fo
	if op == cat:
		fo = cat.who()
		return cat_turn
	elif op == ninja:
		fo = ninja.who()
		return ninja_turn
	else:
		print "This is no one's turn!!!"

def prompt():
	"""Prints out The HP and Energy of both player and mob. This is so players don't need to press a button to check on their health."""
	global mhp
	global php
	global pen
	global fo
	global men
	print "Socanda %dHP-%dEn, %s %dHP-%dEn" % (php, pen, fo, mhp, men)

def turn(t, op):
	"""Returns who's turn it is going to be. This is so if a mob or the player dies there won't be an extra attack, killing the winner, or letting a dead person fight. It also chooses someone to make the first attack if the game hasn't started yet."""
	global mhp
	global php
	if t == 1:
		php -= op()
		return 2
	elif t == 2:
		mhp -= player_turn()
		return 1
	else:
		return randint(1,2)

def restore():
	"""Very important! Restores the globals to full. Without this the globals would stay at what they are at the end of the last fight"""
	global mhp, php, men, pen
	mhp = 100
	php = 100
	men = 100
	pen = 100


def fighter(mob):
	"""This is the fight engine. You call this with either cat or ninja and it restores the defaults and starts the combat loop. It makes calling this fight really easy as you only need to call this function from the importing module"""
	global player
	restore()
	op = op_set(mob)
	t = None
	player = engine('you', fo)
#	print fo
	while mhp > 0 and php > 0:
		t = turn(t, op)
		prompt()
	if mhp <= 0 and php > 0:
		return 'winner'
	elif php <= 0 and mhp > 0:
		return 'game_death'
	else:
		print "You both seemed to have died..."
		return 'game_death'
