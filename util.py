#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!

import setup


def readSettingsFile():
	settings_file = open(setup.settings_path, 'r')
	filestring = settings_file.read()
	settings_file.close()
	return filestring
	
	
def writeSettingsFile(stringtowrite):
	settings_file = open(setup.settings_path, 'w')
	settings_file.write(stringtowrite)
	settings_file.close()
	print("Wrote to settings file")