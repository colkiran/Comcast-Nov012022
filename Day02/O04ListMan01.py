
l1 = list()
print(f"l1 :{l1}")
print(type(l1))

print("-" * 40)
l2 = [1, 2, 3, 'four', 'five', 'six', 7.5, 8.3, 9.1, 10+3j, 11-2j, True, False]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l3 = list(range(1, 11))
print(f"l3 :{l3}")
print(type(l3))

print("-" * 40)
l4 = [1, 2, 3, 'four', 'five', 'six', 7.5, 8.3, 9.1, 10+3j, 11-2j, True, False]
print(f"l4 :{l4}")
# memory allocation
print(f"l4[0] : {l4[0]} : {id(l4[0])}")
print(f"l4[1] : {l4[1]} : {id(l4[1])}")
print(f"l4[2] : {l4[2]} : {id(l4[2])}")
print(f"l4[3] : {l4[3]} : {id(l4[3])}")

print("-" * 40)
lst = [1, 2, 3, 4, 5]
print(f"lst :{lst}")

# read values in the list
print(f"lst[0] :{lst[0]}")
print(f"lst[1] :{lst[1]}")
print(f"lst[4] :{lst[4]}")
# print(f"lst[5] :{lst[5]}")
print("-" * 40)

for i in lst:
    print(i, end=" ")
print()

# update
print("-" * 40)
print(f"lst :{lst}")
print(f"lst[2] :{lst[2]}")
lst[2] = 35
print(f"lst :{lst}")
# lst[5] = 6
# print(f"lst :{lst}")

# delete
print("-" * 40)
print(f"lst :{lst}")
del lst[3]
del lst[1]
print(f"lst :{lst}")

print("-" * 40)
print(dir(lst))
