"""
class Method
    a. change the value of a class attribute
    b. to manage the arguments passed to the constructor
"""
class Player:

    team = "India"                  # class Attribute

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print("Player Ctor....")

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    @classmethod
    def changeTeam(cls, tm):
        cls.team = tm

    @classmethod
    def CreatePlayer(cls, name, dob):
        print("factory.....")
        from datetime import datetime
        import dateutils
        dt1 = datetime.strptime(dob, "%d/%m/%Y")
        age = int(round(dateutils.years(datetime.now(), dt1), 0))
        return cls(name, age)                   # calls the constructor



ply1 = Player("Virat", 34)
ply1.get_details()

print("-" * 40)
ply2 = Player.CreatePlayer("hello", "10/05/1983")
ply2.get_details()

"""
print("-" * 40)
print(f"Player :{Player.team}")
print(f"ply1 :{Player.team}")

print("-" * 40)
Player.changeTeam("RCB")
print(f"Player :{Player.team}")
print(f"ply1 :{Player.team}")
"""

