#Zadanie 6 (6.py): Zastosuj instrukcje continue w programie z zad. 5 tak, aby po podaniu liczby punktów spoza
#przedziału 0 – 100 pomijać dalsze wykonywanie pętli. Sprawdź działanie programu. Następnie zmień pętlę na
#nieskończoną, czyli taką której warunek zawsze jest prawdziwy. Zakończ działanie pętli przy użyciu instrukcji
#break.
n=int(input('Studentów = '))
x=1
suma=0
while x<=n:
    punkty=int(input(''))
    x=x+1
    suma+=punkty
print(suma/n)