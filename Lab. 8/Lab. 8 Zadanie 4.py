def znaki(nazwa):
    D = {}
    for x in nazwa:
        if x in D:
            D[x] = D[x] + 1
        else:
            D[x] = 1
    return D

D2 = znaki('napisaip')
l = sorted(D2.keys())
for k in l:
    print(k, D2[k])