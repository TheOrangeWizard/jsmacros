# logs nbt information inc. repair cost about the currently selected item to chat
# actual level cost equals repair cost+2 because minecraft

inv = player.openInventory()
slots = inv.getMap()

slot = slots["hotbar"][inv.getSelectedHotbarSlotIndex()]

item = inv.getSlot(slot)
dura = item.getMaxDamage() - item.getDamage()
nbt = item.getNBT()

chat.log("{} {} {}".format(item.getItemID(), dura, nbt))

inv.close()
