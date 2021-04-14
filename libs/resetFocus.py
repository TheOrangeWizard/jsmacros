# resets minecraft's window focus variable
# useful for when clicks stop being registered after using a menu while tabbed out

def resetFocus():
    focused = reflection.getDeclaredField(client.getMinecraft().getClass(), "field_1695")
    focused.setAccessible(True)
    focused.set(client.getMinecraft(), True)
    client.waitTick()
