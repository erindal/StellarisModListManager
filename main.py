#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!


import setup
import gui
import util

def run():
	doRun = setup.confirmStellaris()
	if doRun:
		gui.start()
		
		
def dev():
	setup.confirmStellaris()
	test = util.readSettingsFile()
	testDict = util.decompileSettings(test)
	testDict["Mods"] = "\n"
	testOut = util.compileSettings(testDict)
	util.writeSettingsFile(testOut)
		
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   #run()
   dev()