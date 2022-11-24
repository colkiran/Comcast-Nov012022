
# diff function should always return a positive value

def returnPostive(fnc):

    def helper(a, b):
        if b > a:
            a, b = b, a
        return(fnc(a, b))

    return helper

@returnPostive
def diff(x, y):
    return x - y

print(diff(30, 10))
print(diff(10, 35))
print(diff(25, 60))
