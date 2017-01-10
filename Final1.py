#Is the room switcher and is the module we run to play the game
#Our imports, scenes is the place where the descriptions are stored. Also a foolproof choice maker.
import scenes
from functions import choice
import globals

#The class here has a function that puts the dict of the options into a list so the user can choose them, then gets the key from the list and calls it from the dict.
class scene_changer(object):
	def __init__(self, options):
		self.options = options
	def list_creator(self):
		"""Puts the dict that options is into a list so the user can then choose an option and call the key from the list. This list is a list of keys. It nullifies the unorderness of a dict."""
		l = []
		for j in self.options:
			l.append(j)
		return l
	def list_printer(self, list):
		"""Prints the list from list_creator, adding a number to each of the options."""
		n = 1
		for j in list:
			print str(n) + '. ' + str(self.options[j])
			n +=1
	def run(self):
		"""The function we call. It calls the list creator and the list printer. Then it gets the user's input from the function we imported above, choice(). It then returns the key that we stored in the list."""
		list = self.list_creator()
		self.list_printer(list)
		c = list[choice(len(list))]
		return c


def main():
	"""The function here is the scene runner. Our first scene is specified here, then below we have the scene looping."""
	#Not only does this instanchiate the class from scenes and get the options dict from there, but it instancheates the class we defined in this module and returns a key we can 	#use in another line like this. I could have used current_scene = 'first_scene', but I wrote it like this, so it really doesn't matter.
	current_scene = scene_changer(scenes.scene_dict.get('main_menu').read()).run()
	while current_scene != 'death2':
		#The line below is just like the line above, it calls an instance from scenes and an instance of the class from here and gets something like 'death'. if it gets 'death the 		#whole thing ends.
		globals.current_scene = current_scene
		current_scene = scene_changer(scenes.scene_dict.get(current_scene).read()).run()

#Starts the scene engine
main()