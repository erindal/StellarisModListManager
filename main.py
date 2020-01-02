# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!


import setup
import gui_cmd


def run():
	do_run = setup.confirm_stellaris()
	is_running = setup.is_stellaris_running()
	if do_run and not is_running:
		gui_cmd.app_loop()


if __name__ == "__main__":
	run()
