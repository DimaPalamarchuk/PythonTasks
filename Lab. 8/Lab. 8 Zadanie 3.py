def potęga():
    lista3=[]
    if len(lista1) != len(lista2):
        print('rozna długosc list')
        return lista3
    for i in range(lista1):
        lista3.append(lista1[i]**lista2[i])
    return lista3



lista1 = [2,4,5,3]
lista2 = [5,6,2,8]

x = potega(list1, list2)
print(x)
