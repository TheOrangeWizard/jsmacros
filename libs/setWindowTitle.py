def setWindowTitle(title):
    mc = client.getMinecraft()
    getWindow = reflection.getDeclaredMethod(mc.getClass(), "method_22683")
    window = getWindow.invoke(mc)
    window.method_24286(title)
