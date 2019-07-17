# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

from appJar import gui
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

# Functions

# Status Function - Call to update status bar
# TODO


# Update mods in mod list and all mods
# This should be set as the check box function
def updateModlist(): #TODO CONVERT NAMELIST TO PROPER MOD NAMES

	#Get selected mod
	app.openFrame("LEFT")
	app.openScrollPane("All Mods")

	nameList = util.boxDictToNameList(app.getAllCheckBoxes())

	app.stopScrollPane()
	app.stopFrame()

	# Get existing mods, update right
	app.openFrame("RIGHT")

	app.openScrollPane("Current Mods")

	currentModList = util.boxDictToNameList(app.getAllCheckBoxes()) + nameList
	currentModList.sort()

	app.emptyCurrentContainer()

	for i in currentModList:
		app.addCheckBox(i)
		app.setCheckBoxChangeFunction(i, updateModlist)

	app.stopScrollPane()
	app.stopFrame()

	# Update left side
	app.openFrame("LEFT")

	app.openScrollPane("All Mods")

	app.emptyCurrentContainer()
	populateMods(currentModList)

	app.stopScrollPane()
	app.stopFrame()




# Menu Buttons
def menuButtons(button):
	if button == "Create New Profile":
		createProfile()
	elif button == "Change Profile":
		pass
	elif button == "Share":
		pass
	elif button == "Export":
		pass
	elif button == "Activate Profile":
		pass
	elif button == "Settings":
		pass
	elif button == "Quit":
		app.stop()

# Create Profile
def createProfile():
	populateMods()

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

# Update mod list
def populateMods(notInclude=[]):
	app.openFrame("LEFT")

	app.openScrollPane("All Mods")

	for i in allMods:
		if i.name not in notInclude:
			app.addNamedCheckBox(i.name, i.name+"LEFT")
			app.setCheckBoxChangeFunction(i.name+"LEFT", updateModlist)

	app.stopScrollPane()

	app.stopFrame()


# APP CONFIG
app.setBg("#6B7A8F")
app.setFont(family="Verdana")

# Status bar (Saved and Activated)
app.addStatusbar(fields=2, side="Bottom")
app.setStatusbar("Not Saved", 0)
app.setStatusbar("Not Activated", 1)

# Menu bar
fileMenus = ["Settings", "Quit"]
profileMenus = ["Create New Profile", "Change Profile", "-", "Share", "Export", "-", "Activate Profile"]

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

app.startScrollPane("All Mods")

app.stopScrollPane()

app.stopFrame()

# RIGHT FRAME
app.startFrame("RIGHT", row=1, column=1)
app.setBg("white")

app.startScrollPane("Current Mods")

app.stopScrollPane()

app.stopFrame()

#Checkbox setup



#RUN APP
def runApp():
	app.go()