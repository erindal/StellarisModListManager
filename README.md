# StellarisModListManager
Update 8/6/19:
I'm trying to make the profile system work with the gui as well as possible before I release it.
No ETA, but I think I can release a beta by the end of August.
If I can't do that, I will release a limited version that will not have the ability to edit the modlist, 
but still manage your lists you make in the Stellaris launcher using the profile system.

New features (planned):

- Profile system

- Directly edit settings file

- Full UI
________________________________________________

A simple mod list manager for Stellaris. A full release is WIP.

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
