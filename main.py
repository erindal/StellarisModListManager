# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!


import setup
import gui
import util


def run():
    doRun = setup.confirmStellaris()
    if doRun:
        gui.start()


if __name__ == "__main__":
    run()
