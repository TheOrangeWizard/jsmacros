path = "F:/Minecraft/jsMacros/Macros/libs/"
execfile(path + "pick.py")

# uses 16 emeralds which gives the player slightly over 30 levels worth of experience
# dependent on civclassics' plugin+config setup
# a small number of bottles are wasted

pick("minecraft:emerald")
time.sleep(200)
for i in range(16):
    keybind.key("key.mouse.right", True)
    keybind.key("key.mouse.right", False)
    time.sleep(200)