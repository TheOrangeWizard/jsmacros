# same as dump i think

def deposit(name, timeout=500):
    keybind.key("key.mouse.right", True)
    keybind.key("key.mouse.right", False)
    
    t = 0
    while hud.getOpenScreenName() == None and t < timeout:
        t += 1
        client.waitTick()

    if not t < timeout:
        chat.log("failed to open inventory, cancelling")
        return False
    
    inv = player.openInventory()
    slots = inv.getMap()
    
    if "container" not in slots:
        chat.log("inventory not a container, cancelling")
        inv.close()

    for slot in slots["main"]:
        item = inv.getSlot(slot)
        num = item.getCount()
        if item.getItemID() == name:
            inv.quick(slot)
            client.waitTick()

    for slot in slots["hotbar"]:
        item = inv.getSlot(slot)
        num = item.getCount()
        if item.getItemID() == name:
            inv.quick(slot)
            client.waitTick()
    
    time.sleep(500)
    
    inv.close()
