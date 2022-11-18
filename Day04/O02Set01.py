
s1 = set()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)
s2 = {0, 1, 2, 3, 4, 5.3, 6.5, 7.8, 'nine', 'ten', 'eleven', True, False, 11+2j, 11-2j }
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
s3 = {1, 2, 3}
print(f"s3 :{s3} ")

# add values
s3.add(2)
s3.add(1)
s3.add(3)
s3.add(4)
s3.add(2)
s3.add(5)
s3.add(2)
s3.add(6)

print(f"s3 :{s3}")

print(s3.update([1, 2, 3]))
print(s3.update([6, 7, 8]))
print(s3.update([4, 5, 6]))
print(s3.update([8, 9, 10]))

print(f"s3 :{s3}")

# Delete - pop, remove, discard
print("-" * 40)
print(f"s3 :{s3}")

res = s3.pop()
print(f"res :{res}")

res = s3.pop()
print(f"res :{res}")

print(f"s3 :{s3}")

print("-" * 40)
# remove

s3.remove(8)
s3.remove(7)
# s3.remove(1)
print(f"s3 :{s3}")

print("-" * 40)
print(f"s3 :{s3}")

s3.discard(4)
s3.discard(10)
s3.discard(1)

print(f"s3 :{s3}")

print("-" * 40)
A = {1, 2, 3, 4, 5, 6}
B = {5, 6, 7, 8, 9, 10}

print(f"A :{A}")
print(f"B :{B}")

print("-" * 40)
# union
print(f"a union b : A|B" )
print(f"b union a : {B.intersection(A)}")

print("-" * 40)
# intersection
print(f"a intersection B :{A & B}")
print(f"B intersection A :{B.intersection(A)}")

print("-" * 40)
# difference
print(f"A difference B :{A - B}")
print(f'B difference A :{B.difference(A)}')

print("-" * 40)
# systemmetric difference
print(f"A symmetric_difference B :{A ^ B}")
print(f"B symmetric_difference A :{B.symmetric_difference(A)}")

print("-" * 40)
fs = frozenset({1, 2, 3, 4, 5})
print(f"fs :{fs}")
print(type(fs))

# frozensets are immutable
