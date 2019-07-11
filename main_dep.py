#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!


import getpass
import os
import shutil
import gui

currentuser = getpass.getuser()

def main():

	#Ensure settings file exists
	if not os.path.exists("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt"):
		print("You must run Stellaris at least once before using this program. Exiting...")
		
	else:
		print("Stellaris folder detected.")
		
		#Create saved folder directory	
		if not os.path.exists("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists"):
			path = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists"
			try:
				os.mkdir(path)
			except:
				print("Failed to create mod list directory. Check permissions!")
			else:
				print("Mod list directory created.")
	
		else:
			print("Mod list directory found.")
	
	
		
		print("!!")
		print("Warning, this tool will copy your ENTIRE settings file.")
		print("This means if you make changes to your ingame settings, then load a mod list, those changes will be lost.")
		print("!!")
		
		selection()
		
def selection():
	print("Would you like to load or save a modlist? Type 'load' or 'save'")
	print("To read the current mod list, type 'read'")
	print("To use the gui beta, type 'gui'")
	saveorload = input("> ")
	
	if saveorload == 'load':
		load_modlist()
		
	elif saveorload == 'save':
		save_modlist()
		
	elif saveorload == 'read':
		read_modlist()
		
	elif saveorload == 'dev':
		dev()
		
	elif saveorload == 'gui':
		gui.main()
		
	else:
		print("Invalid command. Try again. To quit close this window.")
		selection()
		return
	
def read_modlist(): #Prints mod names of current mod list
	settings_path = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt"

	settings_file = open(settings_path, 'r')
	
	#Cleans file and makes it ready to read
	filestring = settings_file.read() 
	filestring = filestring.replace('\n', ',')
	filestring = filestring.replace('\t', '')
	filesplit = filestring.split(',')
	
	modfilelist = []
	modlist = []
	found = False
	
	#Get mod list
	for i in filesplit:
		#if found is false, program searches for beginning of mod list string
		if found is False:
			if i == 'last_mods={':
				print('Found mod list, parsing')
				print("")
				found = True
		else:	#once found is true, each entry is added to the modlist.
			if i != '}':
				modlist.append(i)
			else:
				found = False

	#strip extra quotes
	for i in modlist:
		#print(i)
		i = i.replace('"','')
		i = i.replace('mod/','')
		modfilelist.append(i)

	#Gets the mod title from the mod file
	for i in modfilelist:
		currentmodfile = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/mod/" + i
		try:
			tempmodfile = open(currentmodfile, 'r')
		except:
			print("!!")
			print("An invalid mod id exists. The mod may not have downloaded, or many not exist. ID: " + i + ". Exiting")
			return
		
		lineone = tempmodfile.readline()
		modname = lineone.replace('name="','')
		modname = modname.replace('"\n','')
		print(modname)
		
	#Run again	
	print("")
	selection()
		
def dev():
	print()
		
def load_modlist():
	#Make backup
	print("Making backup")
	shutil.copyfile("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt", "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists/_settings_backup.txt")

	#Get list of mod lists
	path = "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists"
	filelist = os.listdir(path)
	print("The following mod lists are available: ")
	print(filelist)
	print("Please enter the full file name of the modlist you want to load (Do not include .txt):")
	listtoload = input("> ")
	
	#Copy and replace settings file
	try:
		shutil.copyfile("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists/" + listtoload + ".txt", "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt")
	except FileNotFoundError:
		print("File doesn't not exist. Please check your spelling and try again.")
	else:
		print("Mod list loaded.")
		
	#Run again
	print("")
	selection()
	
def save_modlist():
	print("Please enter a name for your modlist. You may wish to include a Stellaris version number as well")
	savename = input("> ")
	
	newfilepath = ("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists/" + savename + ".txt")
	
	#Check if file already exists
	if os.path.isfile(newfilepath) is True:
		print("File already exists, Y or N for overwrite")
		dooverwrite = input("> ")
		
		#confirm overwrite or abort
		if dooverwrite == "Y":
			try:
				shutil.copyfile("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt", "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists/" + savename + ".txt")
			except:
				print("An unknown error occured. Mod list not saved.")
			else:
				print("File saved")
		
		else:
			print("Mod list not saved.")
	
	#Copy the file	
	else:
		try:
			shutil.copyfile("C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/settings.txt", "C:/Users/" + currentuser + "/Documents/Paradox Interactive/Stellaris/SavedModLists/" + savename + ".txt")
		except: #Known errors: when using bad characters such as "?"
			print("An unknown error occured. Mod list not saved.")
		else:
			print("File saved")

	print("")
	selection()
	
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()