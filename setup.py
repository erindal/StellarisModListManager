#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!

import getpass
import os

currentuser = getpass.getuser()
settings_path = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt"
mod_folder_path = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/mod/"
save_folder_path = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SMLM/"

def confirmStellaris(): #returns false if no stellaris dir exists or if cannot create modlist dir

	#Ensure settings file exists
	if not os.path.exists("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt"):
		print("You must run Stellaris at least once before using this program. Exiting...")
		return False
		
	else:
		print("Stellaris folder detected.")
		
		#Create saved folder directory	
		if not os.path.exists(save_folder_path):
			path = save_folder_path
			try:
				os.mkdir(path)
			except:
				print("Failed to create mod list directory. Check permissions!")
				print(path)
				return False
			else:
				print("Mod list directory created.")
	
		else:
			print("Mod list directory found.")
	
		return True