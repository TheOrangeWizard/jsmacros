# TheOrangeWizard/jsmacros

collection of scripts+library functions intended for use with the jsmacros mod on /r/civclassics

## mods

not presently compatible with jsmacros 1.4+, latest confirmed working is 1.2.9 and jython plugin 1.0.8

requires
https://www.curseforge.com/minecraft/mc-mods/jsmacros

and the jython plugin
https://www.curseforge.com/minecraft/mc-mods/jsmacros-jython

installed as regular fabric mods in .minecraft/mods/

## libs

scripts with library dependencies require the local path variable to be set to the absolute path to the libs folder

(or you could just copy the code into the same file if you're lazy)

## general usage notes

unlike macromod or advancedmacros, jsmacros does not support binding code to a key directly or running a script from the editor.

all scripts are run by binding a file to a hotkey or event

K by default opens the mod menu - this is configurable in the normal keybindings menu if you have cothconfig installed
