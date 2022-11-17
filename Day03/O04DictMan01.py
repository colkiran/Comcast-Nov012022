
d1 = dict()
print(f"d1 :{d1}")
print(type(d1))

print("-" * 40)
d2 = {'name': 'Sachin', 'runs': 105, 'oppn': "Aus", 'venue': 'Perth'}
print(f"d2 :{d2}")
print(type(d2))

print("-" * 40)
d3 = dict([('name', 'rahul'), ('runs', 85), ('oppn', 'SA'), ('venue', 'durban')])
print(f"d3 :{d3}")
print(type(d3))

print("-" * 40)
d4 = dict(name='sachin', runs=98, oppn='Newzealand', venue="auckland")
print(f"d4 :{d4}")
print(type(d4))

print("-" * 40)
player = {'name': 'sachin', 'runs': 97, 'oppn': 'srilanka', 'venue': 'gale'}
print(f"player :{player}")

# Read data
print("-" * 40)
print(f"Name  :{player['name']}")
print(f"Venue :{player['venue']}")

print("-" * 40)
for i in player:
    print(i, "=>", player[i])

# update
print("-" * 40)
player['year'] = 2004
player['name'] = "tendulkar"

print(f"player :{player}")

# delete
print("-" * 40)
del player['venue']
del player['runs']
print(f"player :{player}")

print("-" * 40)
print(dir(d1))
