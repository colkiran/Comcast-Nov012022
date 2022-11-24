a
def outerFun(greet):

    def innerFun(gname):

        print(greet, gname)

    return innerFun
# Simple Curry
outerFun("Welcome") ("Sachin")

print("-" * 40)

infun = outerFun('Welcome')
infun("Rahul")

print("-" * 40)

# simple curry
engGrt = outerFun("Welcome")
hndGrt= outerFun("Namaskar")

engGrt("Sachin")
engGrt("Rohit")
engGrt("Virat")
engGrt("Kapil Dev")

print("-" * 40)
print("-" * 40)
hndGrt("Jadeja")
hndGrt("Axar Patel")
hndGrt("piyush chawla")
hndGrt("Jadeja")
