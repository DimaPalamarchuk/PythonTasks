def zadanie3(*argumenty):
    print(argumenty)
    for x in (argumenty):
        print(x)
    print()

# zadanie3(12, 123, 412, "asdasd", 123.45, [12, 56])
#
# zadanie3(56, "fdcdh")
#
# zadanie3()

def max(*argumenty):
    m=argumenty[0]
    for x in argumenty[1:]:
        if m<x:
            m=x
    return m
print(max(20, 999999, 200000, 90))

liczbamax = max(52, 74, 200, 22)
print(liczbamax)