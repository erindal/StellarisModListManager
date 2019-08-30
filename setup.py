# Author: Erindal
# Contact: erindalc@gmail.com
# This code is under the MIT License, however if you use it, some notification would be appreciated!

import getpass
import os

currentUser = getpass.getuser()
pathSettings = "C:/Users/" + currentUser + "/Documents/Paradox Interactive/Stellaris/settings.txt"
pathModFolder = "C:/Users/" + currentUser + "/Documents/Paradox Interactive/Stellaris/mod/"
pathSaveFolder = "C:/Users/" + currentUser + "/Documents/Paradox Interactive/Stellaris/SMLM/"
pathStellarisFolder = "C:/Users/" + currentUser + "/Documents/Paradox Interactive/Stellaris/"


def confirmStellaris():  # returns false if no stellaris dir exists or if cannot create modlist dir

    # Ensure settings file exists
    if not os.path.exists(pathSettings):
        print("You must run Stellaris at least once before using this program. Exiting...")
        return False

    else:
        print("Stellaris folder detected.")

        # Create saved folder directory
        if not os.path.exists(pathSaveFolder):
            path = pathSaveFolder
            try:
                os.mkdir(path)
            except:
                print("Failed to create mod list directory. Check permissions!")
                print(path)
                return False
            else:
                print("Mod list directory created.")

        else:
            print("Mod list directory found.")

        return True
