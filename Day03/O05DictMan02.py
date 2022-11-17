
player = {'name': 'Rahul', 'runs': 140, 'oppn': 'srilanka', 'venue': 'Srilanka', 'year': 2013}
print(f"player :{player}")

print("-" * 40)
print(player.get('age', "Invalid key Please enter a valid one"))
print(player.get('name', "Invalid key Please enter a valid one"))


print("-" * 40)
# fromkeys  -> used to convert a list into a dictionary
#           -> values of the list is converted to keys of dictionary

cities  = ['blr', 'che', 'mum', 'del', 'kol', 'hyd', 'pun']
print(f"cities :{cities}")

temp = dict.fromkeys(cities, 25)
print(f"temp :{temp}")

# setdefault - add new key value pairs into the dictionary
print("-" * 40)
player = {'name': 'Rahul', 'runs': 140, 'oppn': 'srilanka', 'venue': 'Srilanka'}

player.setdefault('year', 2015)
player.setdefault('name', 'Dravid')
player.setdefault('runs', 200)
player.setdefault('age', 35)

print(f"player :{player}")

print("-" * 40)
player = {'name': 'Rahul', 'runs': 140, 'oppn': 'srilanka', 'venue': 'Srilanka', 'year': 2015, 'age': 35}
print(f"player :{player}")

# keys
ky = player.keys()
print(f"ky :{ky}")

print("-" * 40)
for k in player.keys():
    print(k + " => " + str(player[k]))

# values
print("-" * 40)

player = {'name': 'Rahul', 'runs': 140, 'oppn': 'srilanka', 'venue': 'Srilanka', 'year': 2015, 'age': 35}
print(f"player :{player}")

print("-" * 40)
vl = player.values()
print(f"values :{vl}")

# pop and popitem
player = {'name': 'Rahul', 'runs': 140, 'oppn': 'srilanka', 'venue': 'Gale', 'year': 2015, 'age': 35}
print(f"player :{player}")

print("-" * 40)
res = player.pop('oppn')
print(f"res :{res}")
# print(f"player :{player}")

res = player.pop('year')
print(f"res :{res}")
print(f"player :{player}")

print("-" * 40)
player = {'name': 'Rahul', 'runs': 140, 'oppn': 'srilanka', 'venue': 'Gale', 'year': 2015, 'age': 35}
print(f"player :{player}")

res1 = player.popitem()
res2 = player.popitem()
print(f"res1 :{res1}")

print(f"player :{player}")
