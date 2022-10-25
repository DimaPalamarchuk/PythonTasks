a = int(input("podaj liczbę a: "))
b = int(input("podaj liczbę b: "))

if b<a:
    a,b=b,a

while a<=b:
    if a%2 == 1:
        if a % 2 == 0:
            a = a + 1
            continue
    print(a,end=' ')
    a = a + 1