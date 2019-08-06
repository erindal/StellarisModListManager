# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

from appJar import gui
from time import sleep
import util
import setup

app = gui("Stellaris Mod List Manager", "800x600")

# Objects

allMods = util.getAllMods()
allMods.sort(key=util.sortModList)

class State:
	settingsFileDict = util.decompileSettings(util.readSettingsFile())
	modString = ""
	currentProfile = ""
	isSaved = False
	isActivated = False
	selectedModNames = []


class StringMod:  # This holds the variables added onto mod names to separate them, for when a mod name conflicts
	right = "-RIGHT"
	left = "-LEFT"


# Functions

# Status Function - Call to update status bar
def updateStatus():
	pass

def runThreadedUpdate():
	sleep(2)
	app.thread(threadedUpdate)

def updateModLists(modDict):
	for i in modDict:
		if modDict[i]:
			if i not in State.selectedModNames:
				State.selectedModNames.append(i)
		else:
			if i in State.selectedModNames:
				State.selectedModNames.remove(i)

def threadedUpdate():
	modDict = app.getAllCheckBoxes()
	app.queueFunction(clearAllPanes)
	app.queueFunction(updateModLists, modDict)
	app.queueFunction(populateModList, State.selectedModNames)
	app.queueFunction(populateSelectedMods)

# Update Mod UI - Call to update the mod list in application
def updateModList():
	modDict = app.getAllCheckBoxes()
	clearAllPanes()
	#print(modDict)
	for i in modDict:
		if modDict[i]:
			if i not in State.selectedModNames:
				State.selectedModNames.append(i)
		else:
			if i in State.selectedModNames:
				State.selectedModNames.remove(i)

	print(State.selectedModNames)

	populateModList(ignore=State.selectedModNames)
	populateSelectedMods()

# Clear both scroll panes to avoid conflicts
def clearAllPanes():
	app.openFrame("LEFT")
	app.openScrollPane("Available Mods")
	app.emptyCurrentContainer()
	app.stopScrollPane()
	app.stopFrame()
	app.openFrame("RIGHT")
	app.openScrollPane("Current Mods")
	app.emptyCurrentContainer()
	app.stopScrollPane()
	app.stopFrame()

# Populate Mod UI - Run after to reset the mod list in application
def populateModList(ignore=[]):
	app.openFrame("LEFT")
	app.openScrollPane("Available Mods")

	app.emptyCurrentContainer()

	for i in allMods:
		if i.name not in ignore:
			try:
				app.addCheckBox(i.name)
				app.setCheckBoxChangeFunction(i.name, runThreadedUpdate)
			except:
				print("Skipping " + i.name)

	app.stopScrollPane()
	app.stopFrame()

def populateSelectedMods():
	app.openFrame("RIGHT")
	app.openScrollPane("Current Mods")

	#app.emptyCurrentContainer()

	for i in State.selectedModNames:
		app.addCheckBox(i)
		app.setCheckBox(i, ticked=True)
		app.setCheckBoxChangeFunction(i, runThreadedUpdate)

	app.stopScrollPane()
	app.stopFrame()


# Menu Buttons
def menuButtons(button):
	if button == "Create New Profile":
		populateModList()
		#createProfile()
	elif button == "Change Profile":
		changeProfile()
	elif button == "Export/Share":
		shareMenu()
	elif button == "Import":
		pass
	elif button == "Activate Profile":
		pass
	elif button == "Settings":
		pass
	elif button == "Quit":
		app.stop()

# Create Profile
def createProfile():
	pass

# Change Profile
def changeProfile():
	pass

# Share
def shareMenu():
	pass

# Activate Profile
def activateProfile():
	pass

# Settings
def settingsMenu():
	pass

# Save Profile
def saveProfile():
	pass

# Import
def importMenu():
	pass

# Export
def exportMenu():
	pass


# APP CONFIG
app.setBg("#6B7A8F")
app.setFont(family="Verdana")

# Status bar (Saved and Activated)
app.addStatusbar(fields=2, side="Bottom")
app.setStatusbar("Not Saved", 0)
app.setStatusbar("Not Activated", 1)

# Menu bar
fileMenus = ["Settings", "Quit"]
profileMenus = ["Create New Profile", "Change Profile", "-", "Import", "Export/Share", "-", "Activate Profile"]

app.addMenuList("File", fileMenus, menuButtons)
app.addMenuList("Profile", profileMenus, menuButtons)


# Frames

# TOP CENTER
app.startFrame("CENTER_TOP", row=0, column=0, colspan=2)

app.addLabel("TOP")
# TODO BANNER

app.stopFrame()

# LEFT FRAME
app.startFrame("LEFT", row=1, column=0)
app.setBg("white")

app.startScrollPane("Available Mods")
# temporary fixes toward forcing a larger size
app.setScrollPaneHeight("Available Mods", 500)
app.setScrollPaneSticky("Available Mods", "both")
app.addLabel("None loaded")

app.stopScrollPane()

app.stopFrame()

# RIGHT FRAME
app.startFrame("RIGHT", row=1, column=1)
app.setBg("white")


app.startScrollPane("Current Mods")
app.addLabel("None enabled")

app.stopScrollPane()

app.stopFrame()

# RUN APP
def runApp():
	app.go()
