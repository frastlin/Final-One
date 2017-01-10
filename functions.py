#Functions that have been created
import pickle, globals, os

def name_maker():
	"""Creates a name that is not white space. if the player does make a name that is white space they will be called froo froo roberts."""
	m = True
	while m == True:
		x = str(raw_input("Space cadet what should you be called? > ").strip() or 'Foo Foo Roberts')
		if x.strip():
			m = False
			return x
		else:
			print "I'm sorry?"

def old_choice(max):
	"""This function is not used here, it is the bones of the choice function below.
This is a really strong function that will only except valid numbers up to the max. It will then return a number that is minus 1 for the list grabbing. If there is a better way to do this I would love to know, because I have a function nested 4 times."""
	while True:
		try:
			x = int(raw_input("Please choose an option: > "))
			if x <= max and x > 0:
				return x-1
		except ValueError:
			print "I'm sorry?"

def choice(max):
	"""This is a really strong function it checks the player's input to see if it has a power command like q or s and if it does it performs a function, then returns the player back to the loop. it subtracts 1 from the player's answer if it is a valid number so it can work in lists. If there is a better way to do this I would love to know, because I have a function nested 4 times."""
	while True:
		x = raw_input("Please choose an option: > ")
		task_checker(x)
		if x == "":
			x = 1
		try:
			x = int(x)
			if x <= max and x > 0:
				return x-1
		except ValueError:
			pass

def task_checker(c):
	"""I need to find a better way of doing many or statements with the same half of the or being the same. But this calls quit and save."""
	if globals.current_scene == 'main_menu' or globals.current_scene == 'load' or globals.current_scene == 'death' or globals.current_scene == 'start' or globals.current_scene == 'Pre_intro' or globals.current_scene == 'racing' or globals.current_scene == 'f2' or globals.current_scene == 'blast' or globals.current_scene == 'winner':
		pass
	elif c == "s":
		save_globals()
		print "Saved."
	elif c == "h":
		print """To save your progress press s at any time. If you would like to quit press q and if you wish you can press return instead of pressing 1 to continue. To repeat\nthis message press h."""
	elif c == "q":
		print "Are you sure you want to quit?"
		m = raw_input("Press y to answer yes and any other key to answer no: > ")
		if m == "y":
			leave()
	elif c == "cs":
		print globals.current_scene
#	elif c == "ln":
#		print "%d%d%d%d" % (globals.number1,globals.number2,globals.number3,globals.number4)

def glist():
	"""Makes a list of global values from the globals.py file. I should make the globals.py file into a dict, so this wouldn't need to be here."""
	return [globals.player_name, globals.number1, globals.number2, globals.number3, globals.number4, globals.sword_pressed, globals.beer_count, globals.turn, globals.blaster, globals.boom, globals.current_scene]

def save_globals():
	"""Saves all the globals to a name.save file that is pickled."""
	file = open("%s.save" % globals.player_name, 'wb')
	l = glist()
	for g in l:
		pickle.dump(g, file, 2)
	file.close()

def restore(sav):
	"""This is why I should have the dict for my globals file. instead of one or two lines of code, I have all the globals below."""
	print "Press 1 to restore this sav or 2 to delete it."
	if choice(2) == 1:
		os.remove(sav)
		globals.current_scene = 'main_menu'
		print "Your save has been deleted."
	else:
		file = open(sav, 'rb')
		globals.player_name = pickle.load(file)
		globals.number1 = pickle.load(file)
		globals.number2 = pickle.load(file)
		globals.number3 = pickle.load(file)
		globals.number4 = pickle.load(file)
		globals.sword_pressed = pickle.load(file)
		globals.beer_count = pickle.load(file)
		globals.turn = pickle.load(file)
		globals.blaster = pickle.load(file)
		globals.boom = pickle.load(file)
		globals.current_scene = pickle.load(file)
		file.close()

def list_saves():
	"""Prints the .save files to the screen that are in the same directory of the run file. If there is a way to get the .save extenchan out of there I would like to know."""
	l = []
	x = 2
	print "1. Go back to the main menu."
	for files in os.listdir("."):
		if files.endswith(".save"):
			print "%d. %s" % (x, files)
			l.append(files.split(".")[0])
			x += 1
	return l

def leave():
	"Exits and saves if the player wishes."""
	if globals.current_scene != 'quit' and globals.current_scene != 'load':
		print "If you would like to save your progress press s now. Otherwise press 1 to\ncontinue."
		choice(1)
	exit()

