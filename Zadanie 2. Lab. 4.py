#Utwórz listę zestaw_1 zawierającą liczby losowe z przedziału [1, 10]. Liczbę elementów listy podaje
#użytkownik. Wyświetl listę.

#• Utwórz drugą listę zestaw_2 zawierającą liczby losowe z przedziału [5, 15]. Liczbę elementów listy
#podaje użytkownik. Wyświetl listę.

#• Pobierz od użytkownika liczbę. Napisz instrukcję warunkową, która na podstawie wartości
#zapisanych w listach wyświetli jeden z poniższych komunikatów: „Liczba z zestawu 1”, „Liczba z
#zestawu 2” albo „Nie ma takiej liczby w obu zestawach”.

#• Utwórz listę zestaw_1_2 będącą złączeniem wartości z list zestaw_1 oraz zestaw_2. Posortuj i wyświetl
#listę.

import random

zestaw_1 = []

generowane_liczby = int(input('Podaj licbę: '))

x = random.randint(1, 10)

for y in range(generowane_liczby):
    x = random.randint(1, 10)
    zestaw_1.append(x)

print(zestaw_1)

generowane_liczby_2 = int(input('Podaj licbę 2: '))
zestaw_2 = [random.randint(5, 15) for y in range(generowane_liczby_2)]

print(zestaw_2)

y = int(input('Podaj licz: '))

if y in zestaw_1:
    print('Number of first list: ')
elif y in zestaw_2:
    print('Number of second list ')
else: print('Number not exitst pf both lists')

zestaw_1_2 = zestaw_1 + zestaw_2
print(zestaw_1_2)

zestaw_1_2.sort()
print(zestaw_1_2)