# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

import setup
import os
import json


class Mod:  # holds mod info
	def __init__(self, uid, name, path):
		self.name = name
		self.uid = uid
		self.path = path
		
		
class GameData:
	def __init__(self):
		self.loadOrder = getLoadOrder()
		self.activeMods = getSelectedMods()
		self.allModsList = getModData()
		self.shareLoadOrder = []
		
	def sortModOrder(self):
		sortOrder = []
	
		# Sort
		self.allModsList.sort(reverse=True, key=sortModObj)
	
		# Write uid
		for mod in self.allModsList:
			sortOrder.append(mod.uid)
		
		# Update data
		self.loadOrder = sortOrder
		
	def removeMod(self, uid):
		for mod in self.allModsList:
			if mod.uid == uid:
				temp = mod.path
				break
	
		self.activeMods.remove(temp)
		
	def addMod(self, uid):
		for mod in self.allModsList:
			if mod.uid == uid:
				temp = mod.path
				break
				
		self.activeMods.append(temp)
		
	def displayOrderedActiveMods(self):
		for uid in self.loadOrder:
			for mod in self.allModsList:
				if uid == mod.uid:
					if mod.path in self.activeMods:
						print(mod.name)
		
	def updateLoadOrder(self):
		self.shareLoadOrder = []
		
		for uid in self.loadOrder:
			for mod in self.allModsList:
				if uid == mod.uid:
					if mod.path in self.activeMods:
						self.shareLoadOrder.append(mod.uid)
		
		
	def writeAllData(self):
		writeModOrder(self.loadOrder)
		writeModList(self.activeMods)
		
	def importData(self, filePath):
		
		saveFile = open(filePath, 'r')
		
		dataDict = json.load(saveFile)
		
		self.loadOrder = dataDict['load_order']
		self.activeMods = dataDict['loaded_mods']
		
		saveFile.close()
		
	def exportData(self, fileTitle):
		
		saveFile = open(setup.pathSaveFolder + fileTitle + ".json_smlm", "w")
		
		dataDict = {'load_order':self.loadOrder, 'loaded_mods':self.activeMods}
		
		json.dump(dataDict, saveFile)
		
		saveFile.close()
		
		
		
def getModData(): # Returns list of Mod objects of all installed mods
	allModsList = []
	
	# Extract data
	modDataFile = open(setup.pathModData, 'r')
	modData = json.load(modDataFile)
	modDataFile.close()
	
	# Get needed mod data
	for mod in modData:
		name = modData[mod]["displayName"]
		try:
			path = modData[mod]["gameRegistryId"]
		except KeyError: # Handle missing path
			print("")
			print("Missing game reg id!")
			print("This mod was not installed correctly!")
			print("You should unsubscribe and clear your .../Stellaris/mod/ folder to fix this")
			print("Back up the folder first, especially if you've ever made mods yourself")
			print(name)
			print("")
			
			path = None
		
		
		
		allModsList.append(Mod(mod, name, path)) # mod is the uid
		
	return allModsList	

def getLoadOrder(): # Returns current load order in list form, using mod's uid
	modOrder = []
	
	# Extract data
	loadOrderFile = open(setup.pathLoadOrder, 'r')
	loadOrderData = json.load(loadOrderFile)
	loadOrderFile.close()
	
	modOrder = loadOrderData["modsOrder"]
	
	return modOrder
	
def getSelectedMods(): # Returns current mod list in list form, using mod's path
	modList = []
	
	# Extract data
	modListFile = open(setup.pathModList, 'r')
	modListData = json.load(modListFile)
	modListFile.close()
	
	modList = modListData["enabled_mods"] # WHY IS THIS INCONSISTENT ??? Come on paradox
	
	return modList	
	
def writeModOrder(modOrder):
	# Open file
	loadOrderFile = open(setup.pathLoadOrder, 'r+')
	loadOrderData = json.load(loadOrderFile)
	loadOrderData["modsOrder"] = modOrder
	loadOrderFile.seek(0)
	json.dump(loadOrderData, loadOrderFile)
	loadOrderFile.truncate() # Technically this shouldn't be necessary but just in case
	loadOrderFile.close()
	print("Wrote updated load order")

	
def writeModList(modList):
	# Open file
	modListFile = open(setup.pathModList, 'r+')
	modListData = json.load(modListFile)
	modListData["enabled_mods"] = modList
	modListFile.seek(0)
	json.dump(modListData, modListFile)
	modListFile.truncate()
	modListFile.close()
	print("Wrote updated mod list")
	

def sortModObj(val):  # use as a key
	return val.name


