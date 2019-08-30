# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

class Profile:  # Holds data for current profile and contains various functions
	def __init__(self, fileName):
		self.name = ""
		self.version = ""
		self.fileName = fileName
		self.modList = []
		self.settingsText = ""

	def readProfile(self):  # Imports data from file into program
		pass
		# TODO
		# util.parseSaveProfile -> self.modlist
		# read any metadata

	def updateProfile(self, newModList):  # Updated modlist is passed
		pass
		# Should also update settings text

	def writeProfile(self):  # Write data to file
		pass

	def activateProfile(self):  # Writes mod list to settings file
		pass

	def duplicateProfile(self, newName):  # Creates a new copy of the profile under a passed name
		pass

	def mergeProfile(self, secondProfile, newName):  # Creates a new profile merging two existing profiles
		#Should handle duplicate mods
		#TODO write a util to clean a mod list
		pass


def startup():
	pass
	# This will scan all the existing profiles and import them into the program
