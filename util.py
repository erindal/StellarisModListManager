# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

import urllib.error
import ctypes
import setup
import json
import requests
import os
import urllib.request as url_req


def message_box(title, text, style):
	return ctypes.windll.user32.MessageBoxW(0, text, title, style)
# See: https://stackoverflow.com/questions/34953438/how-can-i-get-the-value-of-the-pressed-button-inside-of-a-ctypes-messageboxa?noredirect=1&lq=1
# For info


class Mod:  # holds mod info
	def __init__(self, uid, name, path):
		self.name = name
		self.uid = uid
		self.path = path
		
		
class GameData:
	def __init__(self):
		self.load_order = get_load_order()
		self.active_mods = get_selected_mods()
		self.all_mods_list = get_mod_data()
		self.share_load_order = []

	def sort_mod_order(self):
		sort_order = []
	
		# Sort
		self.all_mods_list.sort(reverse=True, key=sort_mod_obj)
	
		# Write uid
		for mod in self.all_mods_list:
			sort_order.append(mod.uid)
		
		# Update data
		self.load_order = sort_order
		
	def remove_mod(self, uid):
		for mod in self.all_mods_list:
			if mod.uid == uid:
				temp = mod.path
				break
	
		self.active_mods.remove(temp)
		
	def add_mod(self, uid):
		for mod in self.all_mods_list:
			if mod.uid == uid:
				temp = mod.path
				break
				
		self.active_mods.append(temp)
		
	def display_ordered_active_mods(self):
		for uid in self.load_order:
			for mod in self.all_mods_list:
				if uid == mod.uid:
					if mod.path in self.active_mods:
						print(mod.name)
		
	def update_load_order(self):
		self.share_load_order = []
		
		for uid in self.load_order:
			for mod in self.all_mods_list:
				if uid == mod.uid:
					if mod.path in self.active_mods:
						self.share_load_order.append(mod.uid)

	def write_all_data(self):
		write_mod_order(self.load_order)
		write_mod_list(self.active_mods)
		
	def import_data(self, file_path):
		
		save_file = open(file_path, 'r')
		
		data_dict = json.load(save_file)
		
		self.load_order = data_dict['load_order']
		self.active_mods = data_dict['loaded_mods']
		
		save_file.close()
		
	def export_data(self, file_title):  # Warning! This will need adjustment for a different ui system!
	
		save_file_path = setup.path_save_folder + file_title + ".json_smlm"
		
		if os.path.exists(save_file_path):
			msg_box = message_box("Overwrite?", "This file already exists. Do you wish to overwrite it?", 4)
			
			if msg_box == 6:
				pass
			else:
				return False
		
		save_file = open(save_file_path, "w")
		
		data_dict = {'load_order': self.load_order, 'loaded_mods': self.active_mods}
		
		json.dump(data_dict, save_file)
		
		save_file.close()
		
		return True

	def create_paste(self):
		data_dict = {'load_order': self.load_order, 'loaded_mods': self.active_mods}

		paste_data = json.dumps(data_dict)

		paste_api_end = "https://pastebin.com/api/api_post.php"
		paste_api_key = "da4c9e0d5d5470ea2c8c20197eeb28f2"

		data = {'api_dev_key': paste_api_key, 'api_option': 'paste', 'api_paste_code': paste_data}

		r = requests.post(url=paste_api_end, data=data)
		paste_code = r.text

		return paste_code

	def read_paste(self, share_code):  # TODO HANDLE BAD CODES
		try:
			response = url_req.urlopen('https://pastebin.com/raw/'+share_code)
			data = response.read().decode('UTF-8')
			print(data)

			data_dict = json.loads(data)

			self.load_order = data_dict['load_order']
			self.active_mods = data_dict['loaded_mods']
		except urllib.error.HTTPError:
			print("Bad url!")
			print("Import failed!")
			print("Ensure you have the correct url or code")


def get_mod_data():  # Returns list of Mod objects of all installed mods
	all_mods_list = []
	
	# Extract data
	mod_data_file = open(setup.path_mod_data, 'r')
	mod_data = json.load(mod_data_file)
	mod_data_file.close()
	
	# Get needed mod data
	for mod in mod_data:
		name = mod_data[mod]["displayName"]
		try:
			path = mod_data[mod]["gameRegistryId"]
		except KeyError:  # Handle missing path
			print("")
			print("Missing game reg id!")
			print("This mod was not installed correctly!")
			print("You should unsubscribe and clear your .../Stellaris/mod/ folder to fix this")
			print("Back up the folder first, especially if you've ever made mods yourself")
			print(name)
			print("")
			
			path = None

		all_mods_list.append(Mod(mod, name, path))  # mod is the uid
		
	return all_mods_list


def get_load_order():  # Returns current load order in list form, using mod's uid
	mod_order = []
	
	# Extract data
	load_order_file = open(setup.path_load_order, 'r')
	load_order_data = json.load(load_order_file)
	load_order_file.close()
	
	mod_order = load_order_data["modsOrder"]
	
	return mod_order


def get_selected_mods():  # Returns current mod list in list form, using mod's path
	mod_list = []
	
	# Extract data
	mod_list_file = open(setup.path_mod_list, 'r')
	mod_list_data = json.load(mod_list_file)
	mod_list_file.close()
	
	mod_list = mod_list_data["enabled_mods"]  # WHY IS THIS INCONSISTENT ??? Come on paradox

	# if not mod_list:
	# 	print("No mods selected!")
	# 	print("Please close this, enable at least one mod in the Stellaris launcher, and restart SMLM")
	# 	input()
	# 	sys.exit()

	return mod_list


def write_mod_order(mod_order):
	# Open file
	load_order_file = open(setup.path_load_order, 'r+')
	load_order_data = json.load(load_order_file)
	load_order_data["modsOrder"] = mod_order
	load_order_file.seek(0)
	json.dump(load_order_data, load_order_file)
	load_order_file.truncate()  # Technically this shouldn't be necessary but just in case
	load_order_file.close()
	print("Wrote updated load order")

	
def write_mod_list(mod_list):
	# Open file
	mod_list_file = open(setup.path_mod_list, 'r+')
	mod_list_data = json.load(mod_list_file)
	mod_list_data["enabled_mods"] = mod_list
	mod_list_file.seek(0)
	json.dump(mod_list_data, mod_list_file)
	mod_list_file.truncate()
	mod_list_file.close()
	print("Wrote updated mod list")
	

def sort_mod_obj(val):  # use as a key
	return val.name


