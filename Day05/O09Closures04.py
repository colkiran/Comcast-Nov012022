
def outerFun(greet):

    def innerFun(sep):

        def innerMost(gname):
            from emojis import emojis
            emojized = emojis.encode(greet + " :" + sep + ": " + gname)
            print(emojized)

        return innerMost

    return innerFun

kanGrt = outerFun("Namaskara")
kanTgr = kanGrt("tiger")
kanTgr("Prabhakar")


"""
engGrt = outerFun("Welcome")
hndGrt = outerFun("Namaskar")

engSngArw = engGrt("----->")
hndDblArw = hndGrt("======>>")

engSngArw("Sachin")
hndDblArw("Virat")
"""