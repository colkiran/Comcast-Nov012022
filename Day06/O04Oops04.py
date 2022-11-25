
"""
self - have the name of the object that called the method


"""

class Player:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_details(self):
        print(f"Name is {self.name}\nAge is {self.age}")

    # def __del__(self):
    #     print("-" * 40)
    #     print(f"Detroying {self.name}....")

ply1 = Player("Sachin", 34)
ply1.get_details()

print("-" * 40)

ply2 = Player("Sourav", 33)
ply2.get_details()

print("-" * 40)
print(ply1.__dict__)

print("-" * 40)
print(ply2.__dict__)

print("-" * 40)
ply2.runs = 150
print(ply2.__dict__)

print("-" * 40)
print(ply1.__dict__)

"""
print("-" * 40)
del ply1

print("-" * 40)
print("Hello World \n" * 5)
"""
