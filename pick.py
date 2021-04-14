# puts a given item on your hotbar if it is in your inventory.
# similar to macromod PICK()
# name = "minecraft:itemname"
# hotbar = preferred hotbar slot (may not be used)
# dmg = minimum damage value, intended for use with tools to prevent breakages

def pick(name, hotbar=None, dmg=-1):
    inv = player.openInventory()
    slots = inv.getMap()
    
    if hotbar == None:
        hotbar = inv.getSelectedHotbarSlotIndex()

    slot = slots["hotbar"][inv.getSelectedHotbarSlotIndex()]
    item = inv.getSlot(slot)
    dura = item.getMaxDamage() - item.getDamage()
    if item.getItemID() == name and (dmg==-1 or dura>dmg):
        inv.close()
        return True
    
    for i in range(9):
        slot = slots["hotbar"][i]
        item = inv.getSlot(slot)
        dura = item.getMaxDamage() - item.getDamage()
        if item.getItemID() == name and (dmg==-1 or dura>dmg):
            inv.setSelectedHotbarSlotIndex(i)
            inv.close()
            return True
  
    for slot in slots["main"]:
        item = inv.getSlot(slot)
        dura = item.getMaxDamage() - item.getDamage()
        if item.getItemID() == name and (dmg==-1 or dura>dmg):
            inv.swap(slot, slots["hotbar"][hotbar])
            time.sleep(250)
            inv.setSelectedHotbarSlotIndex(hotbar)
            inv.close()
            return True
    
    inv.close()
    return False
