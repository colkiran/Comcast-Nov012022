
def add(x, y):
    return x + y

a = add
res = a(35, 95)
print(f"res :{res}")

print("-" * 40)

b = lambda x, y: x + y
res = b(29, 49)
print(f"res :{res}")

# lambda's are best used with functions like MAP, REDUCE, FILTER

print("-" * 40)
# MAP - allow the lambda expression to execute on every element of the list
# MAP is used for conversion like currency from INR to Dollars, Pounds
l = list(range(1, 11))
print(f"l :{l}")

squares = list(map(lambda x: x ** 2, l))

print(f"squares :{squares}")

print("-" * 40)
# Filter
l2 = list(range(1, 25))
print(f"l :{l}")

res = list(filter(lambda x : x % 3 == 0, l))
print(f"res :{res}")

print("-" * 40)
# reduce
from functools import reduce
l = [8, 3, 1, 4, 7, 5, 9, 2, 10, 6]

res = reduce(lambda x, y: x if x > y else y, l)
print(f"res :{res}")

res = reduce(lambda x, y: x + y, l)
print(f"res :{res}")

print("-" * 40)

months = ['dec', 'aug', 'apr', 'nov', 'feb', 'oct', 'jan', 'mar', 'may', 'jul', 'jun', 'sep']
print(f"months :{months}")

from calendar import month_name

res_asc = sorted(months, key=list(map(lambda mth: mth[0:3].lower(), list(month_name))).index)
print(f"Ascending :{res_asc}")

