

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def log_details(fnc):
    lof_info = "Logging into the service"

    def innerFun(*args):
        print(lof_info)
        print(fnc(*args))
        print("-" * 40)

    return innerFun

sumLogger = log_details(add)
sumLogger(10, 20)

print("-" * 40)

diffLogger = log_details(sub)
diffLogger(30, 12)
