class Player:
    def __init__(self):             # constructor
        print("Player Initialized......")

    def get_runs(self):
        print("runs scored.............")

ply1 = Player()             # calls the constructor
ply1.get_runs()
print("-" * 40)

ply2 = Player()
ply2.get_runs()

print("-" * 40)
ply1.__init__()

print("-" * 40)
print(type(ply1))