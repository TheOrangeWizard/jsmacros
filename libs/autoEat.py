# the player will eat food in its inventory until full or runs out of food
# prioritises the foods highest in the list, can be reordered as needed

path = "F:/Minecraft/jsMacros/Macros/libs/"
execfile(path + "pick.py")


def autoEat(pslot = 8, timeout = 10):
    foods = ["minecraft:beetroot",
             "minecraft:cookie",
             "minecraft:melon_slice",
             "minecraft:apple",
             "minecraft:chorus_fruit",
             "minecraft:carrot",
             "minecraft:baked_potato",
             "minecraft:bread",
             "minecraft:pumpkin_pie",
             "minecraft:cooked_chicken",
             "minecraft:cooked_mutton",
             "minecraft:cooked_porkchop",
             "minecraft:cooked_beef"]
    t = 0
    hf = False
    if player.getPlayer().getFoodLevel() == 20:
        chat.log("not hungry, not eating")
        return True
    while player.getPlayer().getFoodLevel() < 20 and t < timeout:
        for food in foods:
            if pick(food, hotbar=pslot):
                hf = True
                chat.log(food)
                break
        if not hf:
            chat.log("cannot find food")
            return False
        else:
            keybind.key("key.mouse.right", True)
            time.sleep(2500)
            keybind.key("key.mouse.right", False)
            t = t + 1
    if player.getPlayer().getFoodLevel() == 20:
        chat.log("finished eating")
        return True
    else:
        chat.log("eating timed out")
        return False
