#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!

import getpass
import os

currentuser = getpass.getuser()

def confirmStellaris():

	#Ensure settings file exists
	if not os.path.exists("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt"):
		print("You must run Stellaris at least once before using this program. Exiting...")
		return False
		
	else:
		print("Stellaris folder detected.")
		
		#Create saved folder directory	
		if not os.path.exists("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists"):
			path = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists"
			try:
				os.mkdir(path)
			except:
				print("Failed to create mod list directory. Check permissions!")
				print(path)
			else:
				print("Mod list directory created.")
	
		else:
			print("Mod list directory found.")
	
		return True