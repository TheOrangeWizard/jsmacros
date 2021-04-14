def getHeldDura():
    inv = player.openInventory()
    slots = inv.getMap()
    
    slot = slots["hotbar"][inv.getSelectedHotbarSlotIndex()]
    item = inv.getSlot(slot)
    dura = item.getMaxDamage() - item.getDamage()

    inv.close()
    
    return dura