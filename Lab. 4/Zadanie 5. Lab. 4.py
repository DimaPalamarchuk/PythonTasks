import random
punkty = []

y = 0
while y < 15:
    x = random.uniform(0, 50)
    x = round(x, 2)
    punkty.append(x)
    y += 1
print(punkty)

