
letters = ['a', 'b', 'c', 'd', 'e']
print(f"letters :{letters}")

print("-" * 40)
for letter in letters:
    print(letter, end=" ")
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter)
print()

print("-" * 40)
for letter in enumerate(letters):
    print(letter[0],"\t", letter[1])

print("-" * 40)
for index, letter in enumerate(letters):
    print(index, "\t", letter)

print("-" * 40)
my_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(f"my_list :{my_list}")

print("-" * 40)

for lst in my_list:
    print(lst)

print("-" * 40)

for ind, lst in enumerate(my_list):
    print(f"{ind}\t{lst}")

print("-" * 40)

for ind, lst in enumerate(my_list):
    print(f"list({ind})")
    for idx, num in enumerate(lst):
        print(f"\t{idx}\t{num}")

print("-" * 40)

for lst in my_list:
    for num in lst:
        print(num, end=" ")
    print()

print("-" * 40)

lst1 = [1, 2, 3, 4, 5]
lst2 = [11, 22, 33, 44, 55]

for i in zip(lst1, lst2):
    print(i)

print("-" * 40)
lst3 = [10, 20, 30, 40, 50, 60]
from itertools import zip_longest
for i in zip_longest(lst1, lst3):
    print(i)

print("-" * 40)
for i in zip(lst1, lst3):
    print(i)
