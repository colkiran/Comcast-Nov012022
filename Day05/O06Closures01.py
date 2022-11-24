
def outerFun(gname):

    def innerFun():

        print("Hello World")
        print(f"Greetings {gname}")

    innerFun()

outerFun("Sachin")


