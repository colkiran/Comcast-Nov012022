
def greet():
    print("Greetings Mr.Sachin, Welcome to the event......")

def greetGst(gname):
    print(f"Greetings Mr.{gname}, Welcome to the event.......")

# city is a default argument and gname is non default argument
def greetGstCty(gname, city="Mumbai"):
    print(f"Greetings Mr.{gname} from {city}, Welcome to the event.........")

greet()

print("-" * 40)
greetGst("Sachin")

print("-" * 40)
greetGstCty("Sachin")
greetGstCty("Sunil")
greetGstCty("Rahul", "Bangalore")

print("-" * 40)
print("-" * 40)

def admsn(cname, dob, qlf, gender, conno, addr, city, mar_sts):
    print(f"Name           :{cname}")
    print(f"DOB            :{dob}")
    print(f"Qualification  :{qlf}")
    print(f"Gender         :{gender}")
    print(f"Contact No.    :{conno}")
    print(f"Address        :{addr}")
    print(f"City           :{city}")
    print(f"Marital Status :{mar_sts}")

# two way to pass arguments -> *arg - like a list
#                              **kwa    rgs - like a dictionary

# *args
admsn('Richards', '24/10/1982', 'B.tech', 'Male', '323423423', 'MG Road, 8th Main', 'Mumbai',
      'Bachelor')

print("-" * 40)
print("-" * 40)

# **kwargs
admsn(gender="Female", city='Bangalore', qlf='MBA', dob='12/05/1983', cname='Grace', addr='MG Road, 3rd Cross', mar_sts='Spinster', conno='56756753')

print("-" * 40)

# varaible length arguments
def multiply_Me(*numbers):
    print(numbers)
    print(*numbers)
    prod = 1
    for number in numbers:
        prod *= number
    return prod

res = multiply_Me(1, 2, 3, 4, 5)
print(f"res :{res}")

print("-" * 40)

def extract_Details(**player):
    print(player)
    for k in player:
        print(k, "=>", player[k])

extract_Details(name='sachin', runs=136, oppn='Pak', venue='chinnaswamy')

print("-" * 40)
print("-" * 40)

def add_Me(x, y):
    return x + y

print("The sum of %d and %d is :%d" % (25, 86, add_Me(25, 86)))

# using recursive calls find the factorial of a number and generate fibanocci series

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)

x = 5
print(f"fact of {x} is :{fact(x)}")

print("-" * 40)

def fibo(n):
    if n <= 1:
        return n
    else:
        return fibo(n-1) + fibo(n-2)

iter = int(input("Enter the no of iterations :"))

for i in range(iter):
    print(fibo(i), end=" ")
print()

print("-" * 40)
def arithmetic_Calc(x, y):
    sum = x + y
    diff = x - y
    prod = x * y
    quot = x / y
    return sum, diff, prod, quot

res = arithmetic_Calc(20, 8)

print(f"res :{res}")

print("-" * 40)
# doc Strings

def fun():
    # this is a comment
    "this is a doc string"
    print('hello world')

fun()
print(fun.__doc__)

print("-" * 40)
print("-" * 40)

def fun1(x, y):
    """
    res = fun1 (x, y)
    -----------------

    function fun1 takes two arguments x and y
        a. if x and y are integers then the result will be sum of the two numbers
        b. if x abd y are strings then the result will be a concatenation of x and y
        c. if x and y are of different data types then throws an error
    """
    return x + y

res1 = fun1(33, 80)
print(f"res1 :{res1}")

res2 = fun1("hello ", "world")
print(f"res2 :{res2}")

print("-" * 40)
help(fun1)          # call __doc__
