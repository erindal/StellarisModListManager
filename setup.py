# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

import getpass
import os
import psutil

current_user = getpass.getuser()

path_stellaris_folder = "C:/Users/" + current_user + "/Documents/Paradox Interactive/Stellaris/"
path_save_folder = path_stellaris_folder + "SMLM3/"
path_mod_data = path_stellaris_folder + 'mods_registry.json'  # Mod data
path_load_order = path_stellaris_folder + 'game_data.json'  # Load order
path_mod_list = path_stellaris_folder + 'dlc_load.json'  # Mod list


def confirm_stellaris():  # returns false if no stellaris dir exists or if cannot create modlist dir

	# Ensure settings file exists
	if not os.path.exists(path_stellaris_folder):
		print("You must run Stellaris at least once before using this program. Exiting...")
		return False

	else:
		print("Stellaris folder detected.")

		# Create saved folder directory
		if not os.path.exists(path_save_folder):
			path = path_save_folder
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


def is_stellaris_running():  # Return true is Stellaris or Stellaris Launcher is running
	stellaris_apps = ['stellaris.exe', 'Paradox Launcher.exe']
	for proc in psutil.process_iter():
		pname = proc.as_dict(attrs=['name'])
		# print(pname)
		if pname['name'] in stellaris_apps:
			print("Stellaris or a Paradox Launcher is currently running. Please close it before continuing")
			return True
	return False
