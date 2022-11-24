

def outerFun(fnc):

    def helper():
        print("Logging in to the service")
        fnc()
        print("Logging out of the service")
        print("-" * 40)

    return helper

def basicFun():
    print("Call me basic function")

basicFun = outerFun(basicFun)
basicFun()              # calls the helper function

print("-" * 40)

@outerFun
def simpleFun():
    print("Call me Simple Function......")

simpleFun()