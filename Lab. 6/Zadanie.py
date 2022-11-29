numbers = input('Podaj 5 liczby: ')

for number in numbers:
    if int(number) % 2 == 0 or int(number) %3 == 0:
        print(number, end='')