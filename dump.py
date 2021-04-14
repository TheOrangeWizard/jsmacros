# attempts to shift click all a given item into an open inventory

def dump(name):
    inv = player.openInventory()
    slots = inv.getMap()
    
    if "container" not in slots:
        chat.log("inventory not a container, cancelling")
        inv.close()
        return False

    time.sleep(250)
    for slot in slots["hotbar"]:
        item = inv.getSlot(slot)
        if item.getItemID() == name:
            inv.quick(slot)
            client.waitTick()
    for slot in slots["main"]:
        item = inv.getSlot(slot)
        if item.getItemID() == name:
            inv.quick(slot)
            client.waitTick()
    
    time.sleep(500)
    inv.close()
