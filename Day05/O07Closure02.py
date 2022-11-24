
def outerFun(gname):            #HOF - Higher Order Function

    def innerFun():

        print(f"Greetings {gname}")

    return innerFun

infun = outerFun("Sachin")

print("-" * 40)

outerFun("Rahul")()             # calls the innerFun

print("-" * 40)

infun()

print("-" * 40)
print(outerFun.__name__)
print(outerFun("Rahul").__name__)
