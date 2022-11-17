
d1 = {'name': 'Sachin', 'runs': 145, 'oppn': 'SA', 'venue': 'chepauk' }
print(f"d1 :{d1}")
d2 = d1             # shallow copy   (address is shared to d2)
print(f"d2 before :{d2}")

print("-" * 40)
d2['year'] = 2021
print(f"d2 after :{d2}")
print(f"d1 after :{d1}")

print("=" * 40)
print("=" * 40)
d3 = {'name': 'Rahul', 'runs': 85, 'oppn': 'Srilanka', 'venue': 'Chinaswamy' }
print(f"d3 before :{d3}")
d4 = d3.copy()              # deep copy (only data is copied)
print(f'd4 before :{d4}')

print("-" * 40)
d4['year'] = 2022
print(f"d4 after :{d4}")
print(f"d3 after :{d3}")

print("=" * 40)
print("=" * 40)

d5 = {'name': 'Sachin', 'runs': {'chepauk':85, 'chinnaswamy': 134, 'wankhede': 98}, 'oppn': 'Aus'}
print(f"d5  before :{d5}")
d6 = d5.copy()
print(f"d6 before :{d6}")

print("-" * 40)
d6['runs']['mohali'] = 45
print(f"d6 afrer :{d6}")
print(F"d5 after :{d5}")

print("=" * 40)
print("=" * 40)
d7 = {'name': 'Sachin', 'runs': {'chepauk':85, 'chinnaswamy': 134, 'wankhede': 98}, 'oppn': 'Aus'}
from copy import deepcopy
d8 = deepcopy(d7)
print(f"d8 before :{d8}")

print("-" * 40)
d8['runs']['mohali'] = 45
print(f"d8 after :{d8}")
print(f"d7 after :{d7}")
