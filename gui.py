#Author: Erindal
#Contact: erindalc@gmail.com
#This code is under the MIT License, however if you use it, some notification would be appreciated!


from appJar import gui
import util


#setup for gui
allMods = util.getAllMods()



def start():
	app = gui("Stellaris Mod List Manager", "800x600")
	
	#FILE MENU
	def menuPress(button):
		if button == "New":
			pass
		elif button == "Load":
			pass
		elif button == "Save":
			pass
		elif button == "Export to pastebin":
			pass
		elif button == "Exit":
			app.stop()
		
	
	fileMenus = ["New", "Load", "Save", "-", "Export to pastebin", "-", "Exit"]
	
	#TOP CENTER
	app.startFrame("CENTER_TOP", row=0, column=0, colspan=2)
	def comp():
		test = app.getAllCheckBoxes()
		print(test)
	
	app.addMenuList("File", fileMenus, menuPress)
	app.addButton("Go", comp)
	app.stopFrame()
	
	#LEFT FRAME
	app.startFrame("LEFT", row=1, column=0)
	
	
	app.startScrollPane("All Mods")
	
	for i in allMods:
		app.addCheckBox(i.name)
		
	app.stopScrollPane()
	
	app.stopFrame()
	
	#RIGHT FRAME
	app.startFrame("RIGHT", row=1, column=1)
	app.addLabel("right")
	app.stopFrame()
	
	#Keep at bottom, runs app
	app.go()