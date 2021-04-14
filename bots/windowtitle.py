# example script to set the window title to something custom
# unfortunately resets when you open or close a menu ingame

path = "F:/Minecraft/jsMacros/Macros/libs/"
execfile(path + "setWindowTitle.py")

username = player.getPlayer().getName()
address = world.getCurrentServerAddress()

setWindowTitle("{} playing on {}".format(username, address))
