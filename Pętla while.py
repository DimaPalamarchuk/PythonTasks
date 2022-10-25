a = int(input('Podaj liczbe a: '))
b = int(input('Podaj liczbe b: '))

if b<a:
    a,b=b,a

while b>=a:
    print(a, end='')
    a=a+1