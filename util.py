# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

import setup
import os


class Mod:  # holds mod info
	def __init__(self, name, path):
		self.name = name
		self.path = path

def readSettingsFile():  # returns settings file string
	settings_file = open(setup.pathSettings, 'r')
	fileString = settings_file.read()
	settings_file.close()
	return fileString


def writeSettingsFile(stringtowrite):  # takes string, writes to settings file
	settings_file = open(setup.pathSettings, 'w')
	settings_file.write(stringtowrite)
	settings_file.close()
	print("Updated settings file")


def decompileSettings(settingsString):  # takes settings file string, returns separated dictionary of settings file
	settingsDict = {}
	try:
		index1 = settingsString.find("last_mods={")  # finds beginning of mod list
	except:  #What specific exception is this
		print("Please select at least one mod in your Stellaris launcher and close it, then restart the app.")

	index2 = settingsString.find("}\nautosave")  # finds end of mod list

	settingsDict["Beginning"] = settingsString[0:index1 + 11]  # first part of settings file

	settingsDict["Mods"] = settingsString[index1 + 12:index2 - 1]  # this is the indented mod list

	settingsDict["End"] = settingsString[index2:]  # second part of settings file

	return settingsDict


def compileSettings(settingsDict):  # takes settings dictionary, returns complete string for settings file
	settingsString = settingsDict["Beginning"] + settingsDict["Mods"] + settingsDict["End"]
	return settingsString


def readMods(settingsDict):  # takes settings dict returns list of mod name strings
	modString = settingsDict["Mods"]
	modString = modString.replace("\t", "")  # strip tabs
	modList = modString.split("\n")  # separate to list
	modNameList = []

	for i in modList:
		modNameList.append(modPathToName(i))

	return modNameList


def modPathToName(modPath):  # takes mod path and returns the mod name as a string
	# strip quotes
	modPath = modPath.replace('"', '')

	currentmodfile = setup.pathStellarisFolder + modPath
	try:
		tempmodfile = open(currentmodfile, 'r')
	except FileNotFoundError:
		print("An invalid mod path exists!")
		print(tempmodfile)
		return
	except PermissionError:
		print("Permission Error")
		print(tempmodfile)
		print("SMLM does not have access to this file.")
		return

	# TODO - search for name=" instead
	lineone = tempmodfile.readline()
	modname = lineone.replace('name="', '')
	modname = modname.replace('"\n', '')
	return modname


def getAllMods():  # returns list of Mod classes
	currentdir = setup.pathModFolder

	allModsList = []

	for filename in os.listdir(currentdir):  # go through mod directory
		if filename[-4:] == ".mod":  # to ignore mod directories
			try:
				tempfile = open(currentdir + filename, 'r')

				# clean mod name
				lineone = tempfile.readline()
				modname = lineone.replace('name="', '')
				modname = modname.replace('"\n', '')

				# create class with name and path
				allModsList.append(Mod(name=modname, path=filename))

			except PermissionError:
				print("Permission Error")
				print(filename)
				print("SMLM does not have access to this file.")

	return allModsList


def sortModList(val):  # use as a key
	return val.name


def listModNames(modObjList):
	for i in modObjList:
		print(i.name)


# check boxes to path funcs
def boxDictToNameList(boxDict):
	nameList = []

	for i in boxDict:
		if boxDict[i] == True:
			nameList.append(i)

	return nameList


def nameListToPathList(nameList, allMods):
	pathList = []

	for i in allMods:
		if i.name in nameList:
			pathList.append(i.path)

	return pathList


def pathListToString(pathList):
	pathString = "\n"

	for i in pathList:
		pathString = pathString + '\t"mod/' + i + '"\n'

	return pathString


def getAllProfiles():
	currentdir = setup.pathSaveFolder
	profileList = []

	for filename in os.listdir(currentdir):  # go through save directory
		if filename[-4:] == ".txt":  # to ignore sub directories
			profileList.append(filename[:-4])
			#print(filename)

	return profileList


def parseSavedProfile(profile, modDict):  #returns list of mod names
	file = open(setup.pathSaveFolder + profile + ".txt", "r")
	modString = file.read()

	returnlist = cleanModString(modString, modDict)
	return returnlist

def cleanModString(modString, modDict):
	tempString = modString.replace('\t"mod/', "")  # clear formatting
	tempString = tempString.replace('"', "")  # clear quote
	templist = tempString.split("\n")  # Split by newline
	returnlist = []
	for path in templist:
		if path == "":
			pass
		else:
			for mod in modDict:
				if mod.path == path:
					returnlist.append(mod.name)

	return returnlist