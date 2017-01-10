#This is the fight between the Janitor and the player in real-time
#Threading is so we can have two things going on at once
import threading, globals
from time import sleep
from random import randint
#These should be in another file, but because this is just in this file, I am not going to worry about it
playerHP = 100
mobHP = 35

#Is meant for bigger and better things, but has a name argument. It can probably take level arguments as well.
class engine(object):
	def __init__(self, name):
		self.name = name
	def hit(self, first_message, hit_message, miss_message, ac, str, sp):
		"""A pretty generic fighter, takes the weapon object and delivers a number. Damage here is +10, so if I wish, I could make another argument and put that as the hit range. You need to put any list into this function with *listName so it can unpack the list."""
		print first_message
		didHit = randint(ac, 10)
		dammage = randint(str, str+10)
		if didHit == 10 and dammage == str+10:
			sleep(sp)
			print "CRITICAL HIT!"
			a = str+10
			crit = 2*a
			print "%s %s" % (hit_message, crit)
			return crit
		elif didHit > ac:
			sleep(sp)
			print "%s %s" % (hit_message, dammage)
			return dammage
		else:
			sleep(sp*0.6)
			print miss_message + '0'
			return 0

#Because I'm a lazy typer I made these
janitor = engine('the janitor')
player = engine('player')

#If there is a better way to do this, I would like to know! You use the syntax:
#player.hit(*kick)
#I created a list for all the args. This is much faster than creating a class for everything.
grab = ["You reach out and try to pull a loose part off the janitor.", "You find a metal piece and yank it off.", "You couldn't find any loose metal pieces.", 6, 7, 1]
kick = ["You lunge at the Janitor, hoping to deliver a solid kick.", "You smash your foot into the janitor's metal body.", "You smash your foot into... Air...", 8, 3, 0.7]
broom = ["The janitor swings his broom.", "Wham! You are hit quite hard by the janitor's broom. Ouch!", "You manage to dodge out of the way of the janitor’s attack just in time.", 6, 3, 1]
acid = ["The janitor points a red hose at you and starts to make a pumping noise.", "A stream of liquid sprays out the end of the hose, hitting you in the face!", "A stream of liquid comes out of the hose, missing you by just an inch.", 4, 10, 1.5]

def death_checker(mobHP, playerHP):
	"""Just checks who is dead. If I need a return I can put it in here."""
	if mobHP <= 0 and playerHP > 0:
		print """You see the robot is on its last leg and you kick it till a little puff of\nsmoke comes out of the creature's middle and the arms stop their last few\ntwitches."""
		return True
	elif mobHP > 0 and playerHP <= 0:
		print """As the janitor's last attack registers in your brain, you find yourself blacking out. A final whack of the broom sends you completely into darkness."""
		return False
	else:
		print """You both find that you are too tired to fight any more and you both fall to the ground and know no more."""
		return False

def player_fight():
	"""Choice taker and thread for the player. I know I'm using globals, but that is because I would rather not use another file."""
	global mobHP
	global playerHP
	while playerHP > 0 and mobHP > 0 and globals.boom == False:
		x = raw_input("> ")
		if x == "2":
			mobHP -= player.hit(*kick)
		elif x == "1":
			mobHP -= player.hit(*grab)
		elif x == "3":
			print "The janitor has %s HP" % mobHP
		print "H%s" % playerHP

def mob_fight():
	"""A thread for the mob to fight. Something kind of amusing, if the robot is in the middle of an attack when he is dead, his attack finishes, even though he is dead. Need to figure out how to stop this. Perhaps I need to use a checker in sleep with the engine above... But the reason why I have sleep at the end of this is because he was doing a full attack after he was dead and that was a little too much."""
	global playerHP
	global mobHP
	while playerHP > 0 and mobHP > 0 and globals.boom == False:
		choice = randint(1, 2)
		if choice == 1:
			playerHP -= janitor.hit(*acid)
		else:
			playerHP -= janitor.hit(*broom)
		print "H%s" % playerHP
		sleep(randint(0, 7))

def clear_screen():
	"""A function to clear the screan."""
	for j in range(5):
		print "\n"

def fight2_start():
	"""Runs the whole battle between the player and the janitor."""
	global playerHp, mobHp
	#These are the two lines of code that create threads
	mob_thread = threading.Thread(target=mob_fight)
	player_thread = threading.Thread(target=player_fight)
	mob_thread.start()
	player_thread.start()
	mob_thread.join()
	player_thread.join()
	j = death_checker(mobHP, playerHP)
	
	#Makes sure people don't over return the end of the battle, they need to hit y to continue
	c = False
	while c != "y":
		print "Press y to clear the screen."
		c = raw_input("> ")
	
	#clears the screen of the battle spam
	clear_screen()
	return j
