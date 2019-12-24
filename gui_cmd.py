# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!


from tkinter import filedialog
from tkinter import *
import util
import setup
import json
import sys
import time

data = util.GameData()

def displayMenu():
	print("------------------")
	print("1. Sort load order")
	print("2. View mod list")
	print("3. Add/remove a mod")
	print("4. Save mod list")
	print("5. Import/load mod list")
	print("6. Share your mod list")
	print("7. Apply changes to Stellaris")
	print("8. Instructions")
	print("9. Close SMLM")
	print("------------------")
	
def appLoop():
	isSaved = True
	isApplied = True
	
	while True:
		displayMenu()
		
		user_in = input("> ")
		
		if user_in == "1": # Sort
			print("Sorting mod list")
			data.sortModOrder()
			isSaved = False
			isApplied = False
			print("Done")
			
			
		elif user_in == "2": # Print mods
			data.displayOrderedActiveMods()
			
		elif user_in == "3": # Add/remove mods
			print("NYI")
			
		elif user_in == "4": # Save
			if not isSaved:
				print("Enter a file name: ")
				fileTitle = input("> ")
				
				data.exportData(fileTitle)
				
				isSaved = True
				
			else:
				print("Already saved!")
			
		elif user_in == "5": # Load
			root = Tk()
			root.filename =  filedialog.askopenfilename(initialdir = setup.pathSaveFolder,title = "Select mod list file",filetypes = (("SMLM Files","*.json_smlm"),("all files","*.*")))			
			temp = root.filename
			root.destroy()
			
			data.importData(temp)
			
			isApplied = False
			isSaved = False
			
			print("Mod list loaded")
			
		elif user_in == "6": # Share
			print("NYI")
			
		elif user_in == "7": # Apply
			data.writeAllData()
			
			isApplied = True
			
		elif user_in == "8":
			print("----")
			print("Enter a number to access an application function")
			print("Stellaris mod list manager stores all changes internally until you apply your changes to Stellaris")
			print("----")
			time.sleep(2)
	
		elif user_in == "9":
			if not isSaved:
				print("Your changes have not been saved to a file!")
			
			if not isApplied:
				print("Your changes have not been applied to Stellaris!")
				
			if isSaved and isApplied:
				sys.exit()
			else:
				print("If you don't care, simply close this window")
				time.sleep(2)
				
			
#appLoop()
