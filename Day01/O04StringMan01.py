
s1 = str()
print(f"s1 :{s1}")
print(type(s1))

print("-" * 40)

s2 = "Hello World"
print(f"s2 :{s2}")
print(type(s2))

print("-" * 40)
print(f"s2[0]  {s2[0]}")        # strings are stored like list(arrays)
print(f"s2[6]  {s2[6]}")
print(f"s2[10]  {s2[10]}")

print("-" * 40)
# slicing - using indexes
print(f"s2 :{s2}")
print(f"s2[0:5]  :{s2[0:5]}")
print(f"s2[6:11] :{s2[6:11]}")
print(f"s2[0:11] :{s2[0:11]}")
print(f"s2[:11]  :{s2[:11]}")
print(f"s2[0:]   :{s2[0:]}")
print(F"s2[:]    :{s2[:]}")

print("-" * 40)
# reverse indexing
print(f"s2[-1]  :{s2[-1]}")
print(f"s2[-5]  :{s2[-5]}")
print(f"s2[-11] :{s2[-11]}")

print("-" * 40)
# reverse slicing
print(f"s2[-1:-6:-1]  :{s2[-1:-6:-1]}")
print(f"s2[-7:-12:-1] :{s2[-7:-12:-1]}")
print(f"s2[-1:-12:-1] :{s2[-1:-12:-1]}")
print(f"s2[-1::-1]    :{s2[-1::-1]}")
print(f"s2[:-12:-1]   :{s2[:-12:-1]}")
print(f"s2[::-1]      :{s2[::-1]} ")


s2 = "malayalam"
if s2[::] == s2[::-1]:
    print(f"{s2} is  a palindrome......")
else:
    print(f"{s2} is not a palindrome......")

print("-" * 40)
# strings are immutable
s2 = "Hello World"
# print(f"s2 :{s2}")
# s2[6] = "w"

# print(dir(s2))
s2 = "Hello World"
print(f"s2 :{s2}")
idx = s2.find("H")
print(f"index :{idx}")
print("-" * 40)

idx = s2.find("W")
print(f"index :{idx}")
print("-" * 40)

idx = s2.find("l")
print(f"index :{idx}")
print("-" * 40)

idx = s2.find("l", s2.find("l", s2.find("l") + 1) + 1)
print(f"index :{idx}")
print("-" * 40)

idx = s2.find("b")
print(f"index :{idx}")
print("-" * 40)
