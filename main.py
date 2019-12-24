# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!


import setup
import gui_cmd

def run():
	doRun = setup.confirmStellaris()
	isRunning = setup.isStellarisRunning()
	if doRun and not isRunning:
		gui_cmd.appLoop()

if __name__ == "__main__":
	run()
