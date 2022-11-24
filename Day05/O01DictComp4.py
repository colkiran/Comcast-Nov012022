
players = {
    'sachin': [280, 345, 250, 410, 300],
    'sourav': [185, 260, 325, 290, 210],
    'sehwag': [415, 335, 380, 420, 150],
    'rahul': [360, 185, 150, 310, 375],
    'laxman':[215, 150, 340, 280, 195],
}
print(f"players :{players}")

print("-" * 40)

print(f"sachin :{players['sachin']}")

print("-" * 40)

print(f"sachin :{sum(players['sachin'])}")

print("-" * 40)

scores = {k : sum(v) for k, v in players.items() }
print(f"scores :{scores}")

print("-" * 40)

scores = {k: (lambda score: sum(score) / len(score))(v)
          for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)

def avgScr(score):
    return sum(score) / len(score)

scores = {k: avgScr(v) for k, v in players.items()}
print(f"scores :{scores}")

print("-" * 40)

scores = [score for score in players.values()]
print(scores)

print("-" * 40)
# convert it into a single dimension array and filter runs >= 200

scores = [scr for score in players.values() for scr in score]
print(scores)

print("-" * 40)
scores = [scr for score in players.values() for scr in score if scr >= 200]
print(scores)

print("-" * 40)
scores = {name: [scr for scr in score if scr >= 200]
          for name, score in players.items()}
print(scores)
