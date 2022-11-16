
print("count".center(40, "-"))
l1 = [1, 2, 2, 3, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2,1, 1,1,1 ,1, 2, 2,2, 2,1, 2, 3]

print(f"1 :{l1.count(1)}")
print(f"2 :{l1.count(2)}")
print(f"3 :{l1.count(3)}")
print(f"4 :{l1.count(4)}")

print("index".center(40, "-"))

l1 = [1, 2, 2, 3, 1, 1, 1, 1, 2, 2, 3, 2, 2, 2, 2,1, 1,1,1 ,1, 2, 2,2, 2,1, 2, 3]

print(f"3 :{l1.index(3)}")
print(f"3 :{l1.index(3, l1.index(3)+1)}")
print(f"3 :{l1.index(3, l1.index(3, l1.index(3)+1)+1)}")
print(len(l1))

print("copy".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 before :{l1}")
l2 = l1                 # shallow copy - sharing the address with data
print(f"l2 before:{l2}")

print("-" * 40)
l2.extend([6, 7, 8, 9])
print(f"l2 after :{l2}")
print(f"l1 after :{l1}")

print("-" * 40)
l3 = [10, 20, 30, 40, 50]
print(f"l3 :{l3}")
l4 = l3.copy()              # Deep copy which copies only the value not                                 the addresses
print(f"l4 before :{l4}")

print("-" * 40)
l4.extend([60, 70, 80])
print(F"l4 After :{l4}")
print(f"l3 :{l3}")

print("-" * 40)
l5 = [1, 2, 3, [11, 22, 33, 44, 55], 4, 5]
print(f"l5 :{l5}")
l6 = l5.copy()
print(f"l6 before:{l6}")

print("-" * 40)
print(l6[3].extend([66, 77, 88, 99]))
print(f"l6 After :{l6}")
print(f"l5 After :{l6}")

print("-" * 40)
l7 = [2, 4, 6, 8, [1, 2, 3, 4, 5], 10]
print(f"l7 :{l7}")
from copy import deepcopy
l8 = deepcopy(l7)
print(f"l8 before :{l8}")

print("-" * 40)
l8[4].append(6)
l8[4].append(7)
l8[4].append(8)
l8[4].append(9)

print(f"l8 After :{l8}")
print(f"l7 :{l7}")