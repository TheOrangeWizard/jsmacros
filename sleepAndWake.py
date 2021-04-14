# helper function for using a bed

def sleepAndWake():
    time.sleep(100)
    keybind.key("key.mouse.right", True)
    keybind.key("key.mouse.right", False)
    time.sleep(2500)
    try:
        hud.getOpenScreen().close()
    except:
        pass
    time.sleep(2500)
    resetFocus()
    time.sleep(100)