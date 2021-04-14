path = "F:/Minecraft/jsMacros/Macros/libs/"
execfile(path + "grab.py")
execfile(path + "dump.py")
execfile(path + "deposit.py")
execfile(path + "recipes.py")
execfile(path + "autoCraft.py")
execfile(path + "resetFocus.py")
execfile(path + "countItems.py")

# example crafting helper
# waits for the player to click on correct chests/crafting tables
# tendency to break if the wrong things are clicked

while countItems("minecraft:oak_log") < 512:
    chat.log("looking for {} logs...".format(512-countItems("minecraft:oak_log")))
    while hud.getOpenScreen() == None:
        client.waitTick()
    grab("minecraft:oak_log", number=512, onlyFullStacks=True, click=False)

chat.log("need crafting bench...")
while not hud.getOpenScreenName() == "Crafting Table":
    client.waitTick()

inv = player.openInventory()
slots = inv.getMap()

autoCraft(recipes["oak_planks"], inv, slots, 8)
autoCraft(recipes["oak_chest"], inv, slots, 4)

inv.close()
time.sleep(250)
resetFocus()

chat.log("need dropoff chest...")
while hud.getOpenScreen() == None:
    client.waitTick()

dump("minecraft:chest")
time.sleep(100)
chat.log("done!")
