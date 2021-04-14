# helper function which can be configured for (almost) any crop farm
# tx, tz: target coordinates, bot will exit cleanly when it arrives
# yaw, pitch: angle the bot will look at
# movekey: key to be pressed while moving. typically w, a, s, or d
# mouse: left or right mouse key to be pressed
# item: e.g. minecraft:diamond_axe for harvesting or minecraft:wheat_seeds etc. for replanting
# pause: tick delay between each mouse key press. may be useful to increase if the bot encounters anticheat issues
# error: whether or not the bot should abort if it is unable to pick the specified item

def farmLine(tx, tz, yaw, pitch=90, movekey="w", mouse="left", item=None, pause=1, dura=15, error=False):
    pos = player.getPlayer().getPos()
    player.getPlayer().lookAt(yaw, pitch)
    if item is not None:
        pick(item)
    client.waitTick(pause)
    keybind.key("key.mouse." + mouse, True)
    keybind.key("key.mouse." + mouse, False)
    client.waitTick(pause)
    keybind.key("key.keyboard." + movekey, True)
    while (int(pos.z)==tz or int(pos.x)==tx) and not (int(pos.z)==tz and int(pos.x)==tx):
        player.getPlayer().lookAt(yaw, pitch)
        if item is not None:
            if not pick(item, dmg=dura) and error:
                chat.say("/g sa-info failed to pick item, aborting")
                keybind.key("key.keyboard." + movekey, False)
                raise Exception
        client.waitTick(pause)
        keybind.key("key.mouse." + mouse, True)
        keybind.key("key.mouse." + mouse, False)
        pos = player.getPlayer().getPos()
    keybind.key("key.keyboard." + movekey, False)
    if (int(pos.z) == tz and int(pos.x) == tx):
        player.getPlayer().lookAt(yaw, pitch)
        if item is not None:
            if not pick(item, dmg=dura) and error:
                chat.say("/g sa-info failed to pick item, aborting")
                keybind.key("key.keyboard." + movekey, False)
                raise Exception
        client.waitTick(pause)
        keybind.key("key.mouse." + mouse, True)
        keybind.key("key.mouse." + mouse, False)
        client.waitTick(pause)
    else:
        chat.log("coordinate mismatch, aborting")
        raise Exception
