#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!

import logic
from appJar import gui

def main():
	#startup
	logic.main()
	
	#MAIN WINDOW
	appMain = gui("Stellaris Mod List Manager", "800x600")
	appMain.addLabel("title", "Stellaris Mod List Manager")
	appMain.setLabelBg("title", "blue")
	appMain.setFont(18)
	appMain.setBg("gray")

	#LOAD WINDOW
	def pressokayload(btn):
		loadmodlist()
		appMain.hideSubWindow("Mod Lists")
	
	appMain.startSubWindow("Mod Lists", modal=True)
	appMain.addLabelOptionBox("Choose a mod list:", "")
	appMain.addNamedButton("Okay", "loadokay", pressokayload)
	appMain.stopSubWindow()
	
	#Load logic
	def loadmodlist():
		try:
			logic.load_modlistfile(appMain.getOptionBox("Choose a mod list:"))
		except:
			appMain.infoBox("List not loaded", "Error: Your mod list was not loaded.", parent=None)
		else:
			appMain.infoBox("List loaded", "Your mod list was loaded.", parent=None)
			
			
	#SAVE WINDOW
	def pressokaysave(btn):
		#Get data
		filename = appMain.getEntry("Enter list name")
		gameversion = appMain.getEntry("Enter Stellaris Version Number")
	
		#Make sure file isn't blank, if it is ask for a new name, cancel will cancel.
		while filename == "":
			filename = appMain.stringBox("Need name", "Please enter a name for your mod list:", parent=None)
			if filename == None:
				appMain.warningBox("Not Saved", "Your mod list was not saved!", parent=None)
				return
	
		#Does file exist, overwrite or not
		filepath = logic.get_modlistfilepath(filename, gameversion)
		if logic.does_file_exist(filepath):
			if appMain.yesNoBox("Overwrite", "This file exists. Overwrite?", parent=None):
				savemodlist(filepath)
			else:
				appMain.warningBox("Not Saved", "Your mod list was not saved!", parent=None)
		else:
			savemodlist(filepath)
			
		appMain.hideSubWindow("Save New Mod List")
	
	#Save Logic
	def savemodlist(filepath):
		try:
			logic.save_modlistfile(filepath)
		except:
			appMain.infoBox("List not saved", "Error: Your mod list was not saved.", parent=None)
		else:
			appMain.infoBox("List saved", "Your mod list was saved.", parent=None)
	
	appMain.startSubWindow("Save New Mod List", modal=True)
	appMain.addLabelEntry("Enter list name")
	appMain.addLabelEntry("Enter Stellaris Version Number")
	appMain.addNamedButton("Okay", "saveokay", pressokaysave)
	appMain.stopSubWindow()
	
	def mainButtons(button):
		#LOAD
		if button == "Load":
			backup = makeBackup_window()
			if backup:
				logic.make_backup()
			
			filelist = logic.get_modlists()
			
			appMain.showSubWindow("Mod Lists")
			appMain.changeOptionBox("Choose a mod list:", filelist)
				
				
				
				
		#SAVE		
		elif button == "Save":
			appMain.showSubWindow("Save New Mod List")
				
				
		#READ		
		elif button == "Read":
			try:
				logic.read_modlist()
				
			except:
				print("ERROR")

	appMain.addButtons(["Load", "Save", "Read"], mainButtons)
		
	#LOAD WINDOW
	def makeBackup_window():
		return appMain.questionBox("Backup?", "Make a backup of your current mod list?")
	
	#MUST BE AT BOTTOM
	#STARTS APP
	appMain.go()
	
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   main()