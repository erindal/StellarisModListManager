#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!


from appJar import gui
import util
import setup


def start():
	app = gui("Stellaris Mod List Manager", "800x600")
	
	#STARTUP
	allMods = util.getAllMods()
	allMods.sort(key = util.sortModList)
	
	class ReadWrite:
		settingsFileDict = util.decompileSettings(util.readSettingsFile())
		modString = ""
		currentSaveFile = ""
		
		
		
	
	class SaveState: #Holds save status
		isSaved = False
		everSaved = False
		
	
	app.setBg("#6B7A8F")
	app.setFont(family="Verdana")
	
	#def resetChecks():
	#	for i in allMods:
	#		app.setCheckBox(i.name, ticked=False)
	
	#FILE MENU
	def menuPress(button):
		if button == "New":
			if SaveState.isSaved:
				app.clearAllCheckBoxes()
				SaveState.everSaved = False
				SaveState.isSaved = False
			else:
				if app.questionBox("Clear mod list", "Your mod list has not been saved, would you like to clear it anyway?"):
					app.clearAllCheckBoxes()
		elif button == "Load":
			pass
		elif button == "Save":
			if not SaveState.everSaved:
				app.showSubWindow("Save Dialog")
				SaveState.everSaved = True
			else:
				saveModList()
			SaveState.isSaved = True
			print("Mod list saved")
		elif button == "Save As":
			app.showSubWindow("Save Dialog")
		elif button == "Export to pastebin":
			print(app.getAllCheckBoxes())
		elif button == "Settings":
			pass
		elif button == "Exit":
			app.stop()
		
	
	fileMenus = ["New", "Load", "Save", "Save As", "-", "Export to pastebin", "Settings", "-", "Exit"]
	app.addMenuList("File", fileMenus, menuPress)
	
	
	#TOP CENTER
	app.startFrame("CENTER_TOP", row=0, column=0, colspan=2)
	
	app.addLabel("TOP")
	
	app.stopFrame()
	
	#LEFT FRAME
	app.startFrame("LEFT", row=1, column=0)
	app.setBg("white")
	
	app.startScrollPane("All Mods")
	
	def notSaved():
		SaveState.isSaved=False
	
	for i in allMods:
		app.addCheckBox(i.name)
		app.setCheckBoxChangeFunction(i.name, notSaved)
	
	app.stopScrollPane()
	
	app.stopFrame()
	
	#RIGHT FRAME
	app.startFrame("RIGHT", row=1, column=1)
	app.addLabel("right")
	app.stopFrame()
	
	
	#BOTTOM CENTER
	app.startFrame("CENTER_BOTTOM", row=2, column=0, colspan=2)
	
	def putToSettings():
		if SaveState.isSaved:
			ReadWrite.settingsFileDict["Mods"] = ReadWrite.modString
			settingsString = util.compileSettings(ReadWrite.settingsFileDict)
			util.writeSettingsFile(settingsString)
		else:
			if SaveState.everSaved:
				app.infoBox("Please save", "Please save before activating")
			else:
				app.warningBox("Save required", "You have not yet saved your mod list, please save it before activating it")
		
	app.addButton("Activate", putToSettings)
	app.setButtonSticky("Activate", "")
		
	app.stopFrame()
	
	#SAVE/SAVE AS BOX
	app.startSubWindow("Save Dialog")
	
	def saveModList():
		nameList = util.boxDictToNameList(app.getAllCheckBoxes())
		pathList = util.nameListToPathList(nameList, allMods)
		ReadWrite.modString = util.pathListToString(pathList)
		file = open(setup.save_folder_path + ReadWrite.currentSaveFile, "w")
		file.write(ReadWrite.modString)
	
	def saveButton():
		ReadWrite.currentSaveFile = app.getEntry("Enter mod list name") + app.getEntry("Enter Stellaris Version Number") + ".txt"
		
		print(ReadWrite.currentSaveFile)
		
		saveModList()
		
		app.hideSubWindow("Save Dialog")
	
	app.addLabelEntry("Enter mod list name")
	app.setEntryDefault("Enter mod list name", "default")
	app.addLabelEntry("Enter Stellaris Version Number")
	app.setEntryDefault("Enter Stellaris Version Number", "default")
	app.addNamedButton("Okay", "saveBtn", saveButton)
	
	app.stopSubWindow()
	
	#Keep at bottom, runs app
	app.go()