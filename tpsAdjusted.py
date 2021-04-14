def tpsAdjusted(time):
    tps = world.getServer1MAverageTPS()
    mod = tps/20
    return int(time/mod)
