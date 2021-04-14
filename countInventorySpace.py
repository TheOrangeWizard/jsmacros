def countInventorySpace():
    count = 0
    inv = player.openInventory()
    slots = inv.getMap()
    for slot in slots["hotbar"]:
        item = inv.getSlot(slot)
        if item.getItemID() == "minecraft:air":
            count += 1
    for slot in slots["main"]:
        item = inv.getSlot(slot)
        if item.getItemID() == "minecraft:air":
            count += 1
    return count