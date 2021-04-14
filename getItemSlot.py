# search function that returns the slot that holds a given item

def getItemSlot(item, inv, slots):
    for slot in slots["hotbar"]:
        if inv.getSlot(slot).getItemID() == item:
            return slot
    for slot in slots["main"]:
        if inv.getSlot(slot).getItemID() == item:
            return slot
    return False