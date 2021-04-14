# walks to the centre of the given x, z coordinate. assumes flat y level
# if x, z is ommitted then centres the player on the current block
# precise=True attemts to walk to the exact coordinate rather than the centre of the block

def walkTo(x=None, z=None, precise=False, timeout=None):
    pos = player.getPlayer().getPos()
    if x == None:
        x = pos.x
    if z == None:
        z = pos.z
    if precise:
        tx, tz = x, z
    else:
        if x < 0:
            tx = int(x)-0.5
        else:
            tx = int(x)+0.5
        if pos.z < 0:
            tz = int(z)-0.5
        else:
            tz = int(z)+0.5
    chat.log("walking to x {} z {}".format(tx, tz))
    keybind.key("key.keyboard.w", True)
    timer = 0
    while True:
        player.getPlayer().lookAt(tx, pos.y, tz)
        pos = player.getPlayer().getPos()
        if abs(pos.x - tx) < 0.5 and abs(pos.z - tz) < 0.5:
            keybind.key("key.keyboard.left.shift", True)
        if abs(pos.x - tx) < 0.075 and abs(pos.z - tz) < 0.075:
            break
        client.waitTick()
        timer += 1
        if timeout and timer > timeout:
            chat.log("walkTo timed out")
            keybind.key("key.keyboard.w", False)
            keybind.key("key.keyboard.left.shift", False)
            return False
    keybind.key("key.keyboard.w", False)
    keybind.key("key.keyboard.left.shift", False)
    client.waitTick(5)
    pos = player.getPlayer().getPos()
    player.getPlayer().getRaw().method_5814(tx,pos.y,tz)
    return True
