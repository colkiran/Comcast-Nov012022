
values = list(range(10, 40, 10))
print(f"values :{values}")

# unpack the list
a, b, c = values
print(a, b, c, sep=" : ")

print("-" * 40)
values = list(range(10, 101, 10))
print(f"values :{values}")

print("-" * 40)
a, b, *c = values
print(a, b, c, sep=" : ")

print("-" * 40)
a, *b, c = values
print(a, b, c, sep=" : ")

print("-" * 40)
*a, b, c = values
print(a, b, c, sep=" : ")

print("-" * 40)
lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

lst3 = [lst1, lst2]
print(f"lst3 :{lst3}")
print(len(lst3))

print("-" * 40)
lst4 = [*lst1, *lst2]           # unpack the list
print(f"lst4 :{lst4}")
print(len(lst4))
