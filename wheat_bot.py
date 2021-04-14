path = "F:/Minecraft/jsMacros/Macros/libs/"
execfile(path + "pick.py")
execfile(path + "walkTo.py")
execfile(path + "deposit.py")
execfile(path + "farmLine.py")
execfile(path + "resetFocus.py")
execfile(path + "countItems.py")
execfile(path + "sleepAndWake.py")
execfile(path + "countInventorySpace.py")

# example wheat bot

tool = "minecraft:stick" # to be used when clicking crops
threshold = 8 # bot will perform a dropoff once it has this amount of inventory space left

#starting corner of the crop field
startx = 1234
startz = 1234

#opposite corner of the crop field
endx = 2345
endz = 2345

#item config
seeditem = "minecraft:wheat_seeds"
deposititem = "minecraft:wheat"
throwitem = "minecraft:wheat_seeds"

#coordinates for the player to walk to when depositing items
depositx = startx
depositz = startz

#yaw and pitch for the player to look at when depositing items
#note that 0 yaw is south, 90 is west, 180 is north, and 270 is east
deposityaw = 90
depositpitch = 0

#coordinates for the player to walk to when discarding items
throwx = startx
throwz = 2345

#yaw and pitch for the player to look at when discarding items
throwyaw = 270
throwpitch = -25

bedx = 3456
bedz = 3456
bedyaw = 90
bedpitch = 45

if startz < endz:
    hyaw = 0
    pyaw = 180
else:
    hyaw = 180
    pyaw = 0

def dropoff(tx, tz):
    walkTo(tx, tz)
    walkTo(depositx, depositz)
    player.getPlayer().lookAt(deposityaw, depositpitch)
    time.sleep(100)
    deposit(deposititem)
    resetFocus()
    time.sleep(250)
    walkTo(throwx, throwz)
    player.getPlayer().lookAt(throwyaw, throwpitch)
    while countItems(throwitem) > 0:
        pick(throwitem)
        time.sleep(250)
        player.getPlayer().getRaw().method_7290(True)
        time.sleep(250)
    walkTo(bedx, bedz)
    player.getPlayer().lookAt(bedyaw, bedpitch)
    sleepAndWake()
    resetFocus()
    walkTo(throwx, throwz)
    walkTo(startx, startz)

pos = player.getPlayer().getPos()

for rx in range(int(pos.x), endx + 1):
    chat.log("{} {}".format(countInventorySpace(), threshold))
    if countInventorySpace() < threshold:
        dropoff(rx, startz)
    walkTo(rx, startz)
    if tool is not None:
        pick(tool)
    time.sleep(250)
    farmLine(rx, endz, hyaw, item=tool, pause=1)
    time.sleep(250)
    farmLine(rx, startz, pyaw, item=seeditem, mouse="right")
    time.sleep(250)
    if globalvars.getBoolean("stopall") == True:
        chat.log("STOPALL")
        raise Exception

dropoff(pos.x, startz)
chat.log("done!")
