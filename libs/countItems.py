def countItems(name, location=None):
    count = 0
    inv = player.openInventory()
    slots = inv.getMap()
    for section in slots:
        for slot in slots[section]:
            item = inv.getSlot(slot)
            if item.getItemID() == name and (location==None or location==inv.getLocation(slot)):
                count += item.getCount()
    return count
