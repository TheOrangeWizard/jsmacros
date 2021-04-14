# toggles automatically right clicking every tick.
# may trigger anticheat esp. if used while sending chat messages

if globalvars.getString("using") == "on":
    globalvars.remove("using")
    chat.log("auto use OFF")
else:
    globalvars.putString("using", "on")
    chat.log("auto use ON")

while globalvars.getString("using") == "on":
    keybind.key("key.mouse.right", True)
    keybind.key("key.mouse.right", False)
    client.waitTick()
