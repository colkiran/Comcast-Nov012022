
for i in range(1, 11, 1):
    if i % 2 == 1:
        print(i,end=" ")
print()

print("-" * 40)

for i in range(1, 11, 2):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(10, 0, -1):
    print(i, end=" ")
print()

print("-" * 40)

for i in range(1, 16):
    # if i > 10:
    #     break               # break the loop iteration
    if i % 2 == 1:
        continue            # skip the iteration
    print(i, end=" ")
else:
    print("\niteration completed......")

