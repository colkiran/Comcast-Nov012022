
class Player:

    team = "India"                  # class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")


ply1 = Player("Virat", 34)
print(ply1.get_details())

ply2 = Player("Rohit", 33)
print(ply2.get_details())

print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1   :{ply1. team}")
print(f"ply2   :{ply2.team}")

print("-" * 40)
Player.team = "MI"
print(f"Player :{Player.team}")
print(f"ply1 :{ply1.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
ply1.team = "RCB"
print(f'ply1 :{ply1.team}')
print(f"Player :{Player.team}")
print(f"ply2 :{ply2.team}")

print("-" * 40)
print(ply1.__dict__)

