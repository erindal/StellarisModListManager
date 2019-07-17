# StellarisModListManager
A simple mod list manager for Stellaris. A full release is WIP.

Update 7/17:
The full release is approximately 50% done.

New features (planned):

-Profile system

-Directly edit settings file

-Full UI

Built on Python 3.7.2

User Guide (v0.1):

Your current mod list is stored in your documents by Stellaris. This program will store that file seperately and automate loading it when you want to change you mod list.

To make a modlist and save it:
1. Select your mods as you normally would in the Stellaris Launcher
2. Close the launcher (this is important)
3. Run the program, type save
4. Enter a name
5. You're done

The list is now stored in a folder under the same directory as your settings.

You can now open the launcher, change your mod list, close it, and save a new mod list.

To load a list again, type load, then enter the name you saved the list under (the program will give you a file list if you forget).

You can also type "read" to list what mods are currently enabled.

For v0.2+ Users:
Type 'gui' in the command prompt after running main.exe. This will launch a gui window that will allow you load and save your modlists.
You still must create the initial list in the Stellaris launcher, then close the launcher, before saving it.
Clicking the read button will output your modlist into the console window.
