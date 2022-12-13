def dodawanie(a,b):
    return a+b
def odejmowanie(a,b):
    return a-b
def mnożenie(a,b):
    return a*b
def dzielenie(a,b):
    if b!=0:
        return a/b

a = int(input("Podaj a: "))
b = int(input("Podaj b: "))
x = input()

słownik = {'+':dodawanie,'-': odejmowanie,'*':mnożenie,'/': dzielenie}
print(słownik[x](a,b))