
# nested functions

def outerFun(gname):        # local var
    print(id(gname))

    def innerFun():         # convert it into a nonlocal var
        nonlocal gname      # only local var can be converted into nonlocal
        gname += " Tendulkar"
        print("Hello World")
        print(f"Greetings {gname}")
        print(id(gname))

    innerFun()
    print(f"After {gname}")
    print(id(gname))

outerFun("Sachin")
