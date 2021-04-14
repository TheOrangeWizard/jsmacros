path = "F:/Minecraft/jsMacros/Macros/libs/"
execfile(path + "getItemSlot.py")

# when called with a recipe from recipes.py will attempt to place the relevant
# items into an open crafting window and shift click the output

def autoCraft(recipe, inv, slots, amount=1):
    for i in range(amount):
        for n in recipe.keys():
            slot = getItemSlot(recipe[n], inv, slots)
            inv.swap(slot, n)
            time.sleep(100)
        inv.quick(0)
        time.sleep(1000)
