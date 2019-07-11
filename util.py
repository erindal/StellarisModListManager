#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!

import setup


def readSettingsFile():
	settings_file = open(setup.settings_path, 'r')
	fileString = settings_file.read()
	settings_file.close()
	return fileString
	
	
def writeSettingsFile(stringtowrite):
	settings_file = open(setup.settings_path, 'w')
	settings_file.write(stringtowrite)
	settings_file.close()
	print("Wrote to settings file")
	
def decompileSettings(settingsString):
	settingsDict = {}
	
	index1 = settingsString.find("last_mods={") #finds beginning of mod list
	
	index2 = settingsString.find("}\nautosave") #finds end of mod list
	
	settingsDict["Beginning"] = settingsString[0:index1+11] #first part of settings file
	
	settingsDict["Mods"] = settingsString[index1+12:index2-1] #this is the indented mod list
	
	settingsDict["End"] = settingsString[index2:] #second part of settings file
	
	return settingsDict
	
def compileSettings(settingsDict):
	settingsString = settingsDict["Beginning"] + settingsDict["Mods"] + settingsDict["End"]
	return settingsString