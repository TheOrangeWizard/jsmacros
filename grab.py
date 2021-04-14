# attempts to take a given number of a given item from a chest
# tries to open the chest the player is looking at
# shift-clicks stacks until number is reached
# name = "minecraft:itemname"
# number = minimum number of items to grab

def grab(name, number=1, timeout=500, onlyFullStacks=False, click=True):
    if click:
        keybind.key("key.mouse.right", True)
        keybind.key("key.mouse.right", False)
        
        t = 0
        while hud.getOpenScreenName() == None and t < timeout:
            t += 1
            client.waitTick()
        if not t < timeout:
            chat.log("failed to open inventory, cancelling")
            return False
        time.sleep(250)
    
    inv = player.openInventory()
    slots = inv.getMap()
    
    if "container" not in slots:
        chat.log("inventory not a container, cancelling")
        inv.close()
        return False

    time.sleep(250)
    count = 0
    for slot in slots["container"]:
        item = inv.getSlot(slot)
        num = item.getCount()
        if item.getItemID() == name and (num == 64 or not onlyFullStacks):
            count += num
            inv.quick(slot)
            client.waitTick()
            if count >= number:
                inv.close()
                return True
    
    time.sleep(500)
    
    inv.close()
    return False
