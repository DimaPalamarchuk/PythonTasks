def sum_of_values(dict1):
    suma=0
    x=dict1.values()
    for v in x:
        suma+=v
    return suma

wynik=sum_of_values({'data1':15, 'data2':-7, 'data3':20})
print(wynik)