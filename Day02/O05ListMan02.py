
print("{:-^40}".format("append"))
# add one element at a time into the list, will be appended to the end of the list
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")
l1.append(6)
l1.append(7)
print(f"l1 :{l1}")

l1.append([8, 9, 10, 11, 12])
print(f"l1 :{l1}")
print(f"l1[7][1:4] :{l1[7][1:4]}")

print("extend".center(40, "-"))
l2 = [11, 22, 33, 44, 55]
print(f"l2 :{l2}")
print(type(l2))

print("-" * 40)
l2.extend([66, 77, 88, 99])
print(f"l2 :{l2}")

print("insert".center(40, "-"))
l1 = [1, 2, 3, 4, 5]
print(f"l1 :{l1}")

l1.insert(1, 1.5)
l1.insert(3, 2.5)
l1.insert(5, 3.5)
l1.insert(7, 4.5)

print(f"l1 :{l1}")

# pop, remove and clear
print("pop".center(40, "-"))
l3 = list(range(1, 16))
print(f"l3 :{l3}")
res1 = l3.pop(7)
res2 = l3.pop(11)
print(f"res1, res2 :{res1}\t{res2}")
print(f"l3 :{l3}")

print("-" * 40)
res3 = l3.pop()
print(f"res3 :{res3}")
res4 = l3.pop()
print(f"res4 :{res4}")
print(f"l3 :{l3}")

print("remove".center(40, "-"))
l1 = [1, 2, 1, 2, 3, 1, 1, 2, 1, 2, 1, 1, 1, 1, 2, 2, 2, 1, 2, 3, 2, 2, 2, 2, 2, 1, 2, 3]
print(f"l1 :{l1}")

l1.remove(3)
l1.remove(3)
l1.remove(3)
print(f"l1 :{l1}")
# l1.remove(3)

print("-" * 40)

l1 = [1, 1, 1, 1, 2, 3, 1, 1, 1, 2, 2, 2 ,2, 2, 2, 3, 1, 1, 1, 1, 1 ,1 ,1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2]

print(f"l1 :{l1}")

while l1.count(1):
    l1.remove(1)

print(f"l1 :{l1}")

print("clear".center(40, "-"))
lst= list(range(1, 6))
print(f"lst: {lst}")

lst.clear()
print(f"lst: {lst}")
