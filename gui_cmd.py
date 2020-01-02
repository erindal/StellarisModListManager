# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!


from tkinter import filedialog
from tkinter import *
import util
import setup
import sys
import time

data = util.GameData()


def display_menu():
	print("------------------")
	print("1. Sort load order")
	print("2. View mod list")
	print("3. Add/remove a mod")
	print("4. Save mod list")
	print("5. Import/load mod list")
	print("6. Share your mod list")
	print("7. Apply changes to Stellaris")
	print("8. Instructions")
	print("9. Close SMLM")
	print("------------------")


def app_loop():
	is_saved = True
	is_applied = True

	while True:
		display_menu()

		user_in = input("> ")

		if user_in == "1":  # Sort
			print("Sorting mod list")
			data.sort_mod_order()
			is_saved = False
			is_applied = False
			print("Done")

		elif user_in == "2":  # Print mods
			data.display_ordered_active_mods()

		elif user_in == "3":  # Add/remove mods
			print("NYI")

		elif user_in == "4":  # Save
			if not is_saved:
				print("Enter a file name: ")
				file_title = input("> ")

				data.exportData(file_title)

				is_saved = True

			else:
				print("Already saved!")

		elif user_in == "5":  # Load
			root = Tk()
			root.filename = filedialog.askopenfilename(initialdir=setup.path_save_folder, title="Select mod list file",
													   filetypes=(("SMLM Files", "*.json_smlm"), ("all files", "*.*")))
			temp = root.filename
			root.destroy()

			data.import_data(temp)

			is_applied = False
			is_saved = False

			print("Mod list loaded")

		elif user_in == "6":  # Share
			print("NYI")

		elif user_in == "7":  # Apply
			data.write_all_data()

			is_applied = True

		elif user_in == "8":
			print("----")
			print("Enter a number to access an application function")
			print("Stellaris mod list manager stores all changes internally until you apply your changes to Stellaris")
			print("----")
			time.sleep(2)

		elif user_in == "9":
			if not is_saved:
				print("Your changes have not been saved to a file!")

			if not is_applied:
				print("Your changes have not been applied to Stellaris!")

			if is_saved and is_applied:
				sys.exit()
			else:
				print("If you don't care, simply close this window")
				time.sleep(2)

# appLoop()
