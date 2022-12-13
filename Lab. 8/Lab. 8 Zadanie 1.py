def find(lista, liczba):
    lista2=[]
    index = 0
    for i in lista:
        if liczba ==i:
            lista2.append(index)
        index+=1
    return lista2

L1 = find([3,2,5,-2,4,10], 100)
print(L1)

