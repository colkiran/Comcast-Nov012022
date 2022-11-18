
fruits = [
    ('apple', 285),
    ('orange', 65),
    ('grapes', 145),
    ('pineapple', 85),
    ('banana', 65),
    ('gauva', 110),
    ('kiwi', 175),
    ('strawberry', 350)
]

prices = ['fruit' for fruit in fruits]
print(prices)

print("-" * 40)

prices = [fruit for fruit in fruits]
print(f"prices :{prices}")

print("-" * 40)

prices = [fruit[0] for fruit in fruits]
print(prices)

print("-" * 40)

prices = [fruit[1] for fruit in fruits]
print(prices)

print("-" * 40)

prices = [fruit[1] * 0.9 for fruit in fruits]
print(prices)

print("-" * 40)

prices = [fruit[1] * 0.75 for fruit in fruits]
print(prices)

print("-" * 40)

expfrts  = [fruit[0] for fruit in fruits if fruit[1] >= 100]
print(expfrts)

print("-" * 40)

expfrts = [(fruit[0], fruit[1], fruit[1] * 0.9, fruit[1] * 0.75) for
           fruit in fruits if fruit[1] >= 100]
print(expfrts)

print("-" * 40)

sentence  = "the quick brown fox jumps over the lazy dog"
print(f"sentence :{sentence}")

print("-" * 40)

words = [word for word in sentence.split()]
print(words)

print("-" * 40)

words = [(word, len(word)) for word in sentence.split()]
print(words)

print("-" * 40)

words = [(word, len(word)) for word in sentence.split() if word != "the"]
print(words)

print("-" * 40)

squares = [x ** 2 for x in range(1, 11)]
print(squares)

print("-" * 40)

squares = [x ** 2 for x in range(1, 25) if x % 3 == 0]
print(squares)

