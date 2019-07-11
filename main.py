#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!


import setup
import gui


def run():
	doRun = setup.confirmStellaris()
	if doRun:
		gui.start()
		
if __name__ == "__main__":
   # stuff only to run when not called via 'import' here
   run()