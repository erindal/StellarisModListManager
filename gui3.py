# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

from appJar import gui
from time import sleep
import util
import setup

app = gui("Stellaris Mod List Manager", "800x700")

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
	newProfile = True

# Functions

# Status Function - Called every second
def updateStatus():
	app.setLabel("current_profile", State.currentProfile)

	# Status bar
	if State.isSaved:
		app.setStatusbar("Saved", 0)
		app.setStatusbarBg("green", 0)
	else:
		app.setStatusbar("Not Saved", 0)
		app.setStatusbarBg("red", 0)

	if State.isActivated:
		app.setStatusbar("Activated", 1)
		app.setStatusbarBg("green", 1)
	else:
		app.setStatusbar("Not Activated", 1)
		app.setStatusbarBg("red", 1)

# Fix enable/disable bug
def fixCheckboxes():
	app.openFrame("LEFT")
	app.openScrollPane("Available Mods")
	for i in allMods:
		app.addCheckBox("NULL")
		app.removeCheckBox("NULL")
	app.stopScrollPane()
	app.stopFrame()

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

	# State update
	State.isActivated = False
	State.isSaved = False


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

	# State update
	State.isActivated = False
	State.isSaved = False


# Populate Mod UI - Run to reset the mod list in app
def populateModList(ignore=[]):
	app.openFrame("RIGHT")
	app.openScrollPane("Current Mods")
	app.emptyCurrentContainer()
	app.stopScrollPane()
	app.stopFrame()

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
	#app.emptyCurrentContainer()

	for i in State.profileToLoad:
		app.setCheckBox(i, callFunction=True)

	app.stopScrollPane()
	app.stopFrame()


# Menu Buttons
def menuButtons(button):
	if button == "Create New Profile":
		if not State.isSaved:
			saveProfile(autosave=True)
			print("Profile not saved...autosaving!")
		app.showSubWindow("Create Profile")
	elif button == "Change Profile":
		if not State.isSaved:
			saveProfile(autosave=True)
			print("Profile not saved...autosaving!")
		State.profileList = util.getAllProfiles()
		app.changeOptionBox("Profile List", State.profileList)
		app.showSubWindow("Change Profile")
	elif button == "Export/Share":
		app.infoBox("NYI", "")
	elif button == "Import":
		app.showSubWindow("Import Mod List")
	# elif button == "Activate Profile":
	#	pass
	elif button == "Settings":
		app.infoBox("NYI", "")
	elif button == "Quit":
		app.stop()


# Create Profile
def createProfile():
	if app.getEntry("CreateName") is not "":
		if app.getEntry("CreateVersion") is not "":
			app.hideSubWindow("Create Profile")
			State.currentProfile = str(app.getEntry("CreateName") + "_" + app.getEntry("CreateVersion"))
			if State.newProfile:
				State.selectedModNames = []
				populateModList()
				fixCheckboxes()
			else:
				State.newProfile = True
			# State update
			State.isActivated = False
			State.isSaved = False
		else:
			app.errorBox("Need Version", "Please choose a version number!", parent="Create Profile")
	else:
		app.errorBox("Need Name", "Please enter a name!", parent="Create Profile")


# Change Profile
def changeProfile():
	State.currentProfile = app.getOptionBox("Profile List")
	app.hideSubWindow("Change Profile")
	State.selectedModNames = []  # Clean mods
	State.profileToLoad = util.parseSavedProfile(State.currentProfile, allMods)

	app.queueFunction(populateModList)
	app.queueFunction(populateSelectedMods)
	app.queueFunction(fixCheckboxes)

	# State update
	State.isActivated = False
	State.isSaved = True


# Share
def shareMenu():
	pass


# Activate Profile
def activateProfile():
	if State.isSaved:
		pass
	else:
		saveProfile(autosave=True)
		print("Profile not saved...autosaving!")

	State.settingsFileDict["Mods"] = State.modString
	settingsString = util.compileSettings(State.settingsFileDict)
	util.writeSettingsFile(settingsString)
	State.isActivated = True


# Settings
def settingsMenu():
	print(State.selectedModNames)  # DEBUG


# Save Profile
def saveProfile(autosave=False):
	if State.currentProfile != "":
		if State.selectedModNames != []:
			pathList = util.nameListToPathList(State.selectedModNames, allMods)
			State.modString = util.pathListToString(pathList)
			file = open(setup.save_folder_path + State.currentProfile + ".txt", "w")
			file.write(State.modString)
			State.isSaved = True
		else:
			if not autosave:
				app.infoBox("No mods selected", "No mods selected")
	else:
		if not autosave:
			app.infoBox("No profile name", "No profile name")


# Import
def importModList():
	app.hideSubWindow("Import Mod List")
	State.selectedModNames = []  # Clean mods
	State.settingsFileDict = util.decompileSettings(util.readSettingsFile())
	State.profileToLoad = util.cleanModString(State.settingsFileDict["Mods"], allMods)

	State.newProfile = False
	app.showSubWindow("Create Profile")

	app.queueFunction(populateModList)
	app.queueFunction(populateSelectedMods)
	app.queueFunction(fixCheckboxes)

# Export
def exportMenu():
	pass


# APP CONFIG
app.setBg("#6B7A8F")
app.setFont(family="Verdana")

# Menu bar
fileMenus = ["Settings", "Quit"]
profileMenus = ["Create New Profile", "Change Profile", "-", "Import", "Export/Share"]

app.addMenuList("File", fileMenus, menuButtons)
app.addMenuList("Profile", profileMenus, menuButtons)

# Frames

# TOP CENTER
app.startFrame("CENTER_TOP", row=0, column=0, colspan=2)

app.addLabel("Stellaris Mod List Manager")
app.addLabel("current_profile", State.currentProfile)
app.registerEvent(updateStatus)
# TODO BANNER

app.stopFrame()

# LEFT FRAME
app.startFrame("LEFT", row=1, column=0)
app.setBg("white")
app.addLabel("l1", "Available Mods")

app.startScrollPane("Available Mods")
# temporary fixes toward forcing a larger size
app.setScrollPaneHeight("Available Mods", 500)
app.setScrollPaneSticky("Available Mods", "both")
# app.addLabel("None loaded")

app.stopScrollPane()

app.stopFrame()

# RIGHT FRAME
app.startFrame("RIGHT", row=1, column=1)
app.setBg("white")
app.addLabel("r1", " Current Mods")

app.startScrollPane("Current Mods")

# temporary fixes toward forcing a larger size
app.setScrollPaneHeight("Current Mods", 500)
app.setScrollPaneSticky("Current Mods", "both")

app.stopScrollPane()

app.stopFrame()

# BOTTOM FRAME
app.startFrame("BOTTOM", row=2, column=0, colspan=2)
app.addNamedButton("Save", "SaveBtn", saveProfile)
app.addNamedButton("Activate", "ActivateBtn", activateProfile)
app.stopFrame()

# CREATE PROFILE SUBWINDOW
# TODO clean entry upon creating a new profile
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

# IMPORT MOD LIST SUBWINDOW
app.startSubWindow("Import Mod List", modal=True)
app.setSize(300, 200)
app.addMessage("Import Label", "This will take whatever mods are currently selected in the Stellaris launcher "
	"and import it into a profile. \n\nPLEASE CLOSE THE STELLARIS LAUNCHER BEFORE PRESSING OKAY")
app.addNamedButton("Okay", "ImportOkay", importModList)
app.stopSubWindow()

# Status bar (Saved and Activated)
app.addStatusbar(fields=2, side="Bottom")
app.setStatusbar("Not Saved", 0)
app.setStatusbarBg("red", 0)
app.setStatusbar("Not Activated", 1)
app.setStatusbarBg("red", 1)


# EXIT CHECK
def checkStop():
	saveProfile(autosave=True)
	if not State.isActivated:
		app.infoBox("Warning!", "Your selected mod list has not been activated.")
	return app.yesNoBox("Confirm Exit", "Are you sure you want to exit the application?")


app.setStopFunction(checkStop)


# RUN APP
def runApp():
	app.go()
