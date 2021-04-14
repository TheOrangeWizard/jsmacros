# helper function for tree farms
# breaktime is roughly calibrated for diamond e4 axe, should be higher for slower tools.
# yaw = direction of the tree to chop down relative to the player
# hasLowLeaves = if tree can grow leaves at player eye level. true for small oak, false for birch
# logBreakTime
# player should start 3 blocks away from the trunk (i.e. adjacent to the leaves but not under them)
# finishes under the trunk. should be combined with extra walkToward calls and replant saplings in a complete farm script

def chopTree(yaw, hasLowLeaves=True, logBreakTime=15, leafBreakTime=30, toolDmg=15,
             logTool="minecraft:diamond_axe", leafTool="minecraft:stick", toolslot=0):
    pos = player.getPlayer().getPos()
    sx, sz = int(pos.x), int(pos.z)
    if yaw == 0:
        tx, tz = int(pos.x), int(pos.z) - 3
        fx, fz = int(pos.x), int(pos.z) - 5
    elif yaw == 90:
        tx, tz = int(pos.x) - 3, int(pos.z)
        fx, fz = int(pos.x) - 5, int(pos.z)
    elif yaw == 180:
        tx, tz = int(pos.x), int(pos.z) + 3
        fx, fz = int(pos.x), int(pos.z) + 5
    elif yaw == 270:
        tx, tz = int(pos.x) + 3, int(pos.z)
        fx, fz = int(pos.x) + 5, int(pos.z)

    pick("minecraft:stick", hotbar=toolslot)
    player.getPlayer().lookAt(yaw, 15)
    keybind.key("key.mouse.right", True)
    time.sleep(750)
    keybind.key("key.mouse.right", False)
    time.sleep(250)

    while True:
        player.getPlayer().lookAt(yaw,0)
        if hasLowLeaves:
            pick(leafTool, toolslot)
            keybind.key("key.mouse.left", True)
            client.waitTick(leafBreakTime * 2)
            keybind.key("key.mouse.left", False)
            time.sleep(250)
        
        pick(logTool, hotbar=toolslot, dmg=toolDmg)
        player.getPlayer().lookAt(yaw, 12)
        keybind.key("key.mouse.left", True)
        client.waitTick(logBreakTime * 2)
        keybind.key("key.mouse.left", False)
        time.sleep(250)
    
        if walkTo(tx, tz, timeout=500):
            break
        else:
            walkTo(sx, sz)

    player.getPlayer().lookAt(yaw, -90)
    keybind.key("key.mouse.left", True)
    client.waitTick(logBreakTime * 5)
    keybind.key("key.mouse.left", False)
    time.sleep(250)
    
    while True:
        player.getPlayer().lookAt(yaw,0)
        if hasLowLeaves:
            pick(leafTool, toolslot)
            keybind.key("key.mouse.left", True)
            client.waitTick(leafBreakTime * 2)
            keybind.key("key.mouse.left", False)
            time.sleep(250)
        
        if walkTo(fx, fz, timeout=500):
            break
        else:
            walkTo(tx, tz)
    
    

