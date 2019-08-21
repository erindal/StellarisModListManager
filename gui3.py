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
	profileToLoad = []
	profileList = []


# Functions

# Status Function - Call to update status bar
def updateStatus():
	pass

# Called to enable mod in app
def enableModFunc(mod, reload=False):
	# Remove from left
	app.openFrame("LEFT")
	app.openScrollPane("Available Mods")
	app.removeCheckBox(mod)
	app.stopScrollPane()
	app.stopFrame()
	# Add to right
	app.openFrame("RIGHT")
	app.openScrollPane("Current Mods")
	app.addCheckBox(mod)
	app.setCheckBoxChangeFunction(mod, disableModFunc)
	app.stopScrollPane()
	app.stopFrame()
	# Update internal mod list
	if not reload:
		State.selectedModNames.append(mod)

# Called to disable mod in app
def disableModFunc(mod):
	# Remove from right
	app.openFrame("RIGHT")
	app.openScrollPane("Current Mods")
	app.removeCheckBox(mod)
	app.stopScrollPane()
	app.stopFrame()
	# Add to left
	app.openFrame("LEFT")
	app.openScrollPane("Available Mods")
	app.addCheckBox(mod)
	app.setCheckBoxChangeFunction(mod, enableModFunc)
	app.stopScrollPane()
	app.stopFrame()
	# Update internal mod list
	State.selectedModNames.remove(mod)

# Populate Mod UI - Run to reset the mod list in app
def populateModList(ignore=[]):
	app.openFrame("LEFT")
	app.openScrollPane("Available Mods")
	app.emptyCurrentContainer()

	for i in allMods:
		try:
			app.addCheckBox(i.name)
			app.setCheckBoxChangeFunction(i.name, enableModFunc)
		except:  # TODO catch ONLY appJar ItemLookupError
			print("Skipping " + i.name)  # This shouldn't happen anymore, if it does there's a bug

	app.stopScrollPane()
	app.stopFrame()

# Populate Selected Mods - Run after loading an existing mod list
def populateSelectedMods():
	app.openFrame("RIGHT")
	app.openScrollPane("Current Mods")
	app.emptyCurrentContainer()

	for i in State.profileToLoad:
		app.setCheckBox(i, callFunction=True)

	app.stopScrollPane()
	app.stopFrame()


# Menu Buttons
def menuButtons(button):
	if button == "Create New Profile":
		app.showSubWindow("Create Profile")
	elif button == "Change Profile":  # TODO Check if current profile is saved
		State.profileList = util.getAllProfiles()
		app.changeOptionBox("Profile List", State.profileList)
		app.showSubWindow("Change Profile")
	elif button == "Export/Share":
		shareMenu()
	elif button == "Import":
		pass
	elif button == "Activate Profile":
		pass
	elif button == "Settings":
		settingsMenu()
	elif button == "Quit":
		app.stop()

# Create Profile
def createProfile():
	if app.getEntry("CreateName") is not "":
		if app.getEntry("CreateVersion") is not "":
			app.hideSubWindow("Create Profile")
			State.currentProfile = str(app.getEntry("CreateName") + "_" + app.getEntry("CreateVersion"))
			populateModList()
		else:
			app.errorBox("Need Version", "Please choose a version number!", parent="Create Profile")
	else:
		app.errorBox("Need Name", "Please enter a name!", parent="Create Profile")


# Change Profile
def changeProfile():
	State.currentProfile = app.getOptionBox("Profile List")
	app.hideSubWindow("Change Profile")
	State.profileToLoad = util.parseSavedProfile(State.currentProfile, allMods)

	populateModList()
	populateSelectedMods()


# Share
def shareMenu():
	pass

# Activate Profile
def activateProfile():
	# TODO confirm saved
	State.settingsFileDict["Mods"] = State.modString
	settingsString = util.compileSettings(State.settingsFileDict)
	util.writeSettingsFile(settingsString)

# Settings
def settingsMenu():
	print(State.selectedModNames)  #DEBUG


# Save Profile
def saveProfile():
	pathList = util.nameListToPathList(State.selectedModNames, allMods)
	# TODO Make sure a profile is selected and the mod list is not empty
	State.modString = util.pathListToString(pathList)
	file = open(setup.save_folder_path + State.currentProfile + ".txt", "w")
	file.write(State.modString)

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
#app.addLabel("None loaded")

app.stopScrollPane()

app.stopFrame()

# RIGHT FRAME
app.startFrame("RIGHT", row=1, column=1)
app.setBg("white")


app.startScrollPane("Current Mods")
#app.addLabel("None enabled")

app.stopScrollPane()

app.stopFrame()

# BOTTOM FRAME
app.startFrame("BOTTOM", row=2, column=0, colspan=2)
app.addNamedButton("Save", "SaveBtn", saveProfile)
app.addNamedButton("Activate", "ActivateBtn", activateProfile)
app.stopFrame()

# CREATE PROFILE SUBWINDOW
app.startSubWindow("Create Profile", modal=True)
app.setSize(400, 250)
app.addEntry("CreateName")
app.addEntry("CreateVersion")
app.setEntryDefault("CreateName", "Profile Name")
app.setEntryDefault("CreateVersion", "Stellaris Version")
app.addNamedButton("Done", "CreateDone", createProfile)
app.stopSubWindow()


# CHANGE PROFILE SUBWINDOW
app.startSubWindow("Change Profile", modal=True)
app.setSize(400, 250)
app.addOptionBox("Profile List", State.profileList)
app.addNamedButton("Done", "ChangeDone", changeProfile)
app.stopSubWindow()


# EXIT CHECK
def checkStop():
	return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")


app.setStopFunction(checkStop)  # TODO Check save and activated status



# RUN APP
def runApp():
	app.go()
