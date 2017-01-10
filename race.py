#Tests using a little threading without a class
#Import all the modules. random's import of uniform is to get a randint in a decimal number.
import threading
from time import sleep
from random import randint, uniform
from functions import choice
import globals

#Going tells the timer when to stop and correct_turn tells a later function that the turn was correct. I could probably make things work without it, but I'm too lazy to atm.
going = True
correct_turn = False

def countdown():
	"""loops till the player has hit enter and turned going to False. There is a random sleep time and a random number of loops to go to the wall. At the end of this function we call a function that will check if the player made it or not."""
	global going
	sleep(2)
	x = randint(5, 11)
	s = uniform(0.7, 1.8)
	while going == True and x != 1 and globals.boom == False:
		x -= 1
		print "%s feet to the wall" % x
		sleep(s)
	didhit(x)
#*~*
def didhit(final_number):
	"""Checks what message should be printed when the player makes it or not with a check at the top that checks if the player turned or not."""
	global correct_turn, going
	if globals.boom == True:
		pass
	elif correct_turn == False:
		sleep(1)
		print "You slide against the wall and mannage to wedge yourself into a corner."
		sleep(1.5)
		print "You rub your rist"
		sleep(1.5)
		print "You unwedge yourself from the corner"
		sleep(2)
		if going:
			print "What direction should you face?"
			raw_input("Hit return to push off. > ")
		print "You get into a good starting position to head strait down the correct hall."
		sleep(2)
		print "You shoot off and head down the hall."
		sleep(1.5)
	elif final_number in range(4,6):
		print "You smoothely glide into the next hall."
		sleep(1)
	elif final_number < 4:
		print "You waited too long before shooting your legs out and couldn't stop yourself in time."
		failed()
	else:
		f = final_number-5
		r = randint(1,4)
		if r >= f:
			print "You mannaged to launch off the wall and shoot into the next hall."
		else:
			print "You misjudged the distance it was to the upcoming wall and overcompinsated."
			failed()
	correct_turn = False

def failed():
	"""The messages that say that the player failed."""
	sleep(0.5)
	print "You slam into the wall!"
	sleep(1)
	print "You shake your head to clear it from the stars."
	sleep(2)
	print "********"
	sleep(1)
	print "*****"
	sleep(2)
	print "You right yourself and head into the next hall."
	sleep (3)

def direction():
	"""chooses the direction of the hall that is the next hall at the end of the tunnel."""
	d = randint(0,1)
	if d:
		print "Turn right!"
	else:
		print "Turn left!"
	return d

def player_choice():
	"""checks if the player chooses the direction they need to go."""
	global correct_turn
	if direction() == choice(2):
		print "You point your feet toward the upcoming hall."
		correct_turn = True
	else:
		print "You turn your body and realise you are heading strait for a wall!"
		correct_turn = False

def main():
	"""Has one iteration of this script."""
	global going
	going = True
	count = threading.Thread(target=countdown)
	count.start()
	player_choice()
	going = False
	count.join()

def race_loop():
	"""Loops the main script a random amount of times. This is the script you would call to run this."""
	x = randint(7, 10)
	while x != 0 and globals.boom == False:
		main()
		x-=1
