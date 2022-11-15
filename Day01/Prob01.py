
for i in range(6, 1, -1):
    for k in range(1, 7-i):
        print(" ", end="")
    for j in range(1, i):
        print(j, end=" ")
    print()

for i in range(2, 6):
    for k in range(1, 6-i):
        print(" ", end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
