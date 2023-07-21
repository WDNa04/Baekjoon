i = 0
lista = []
listb = []
while i<3:
    a, b = map(int,input().split())
    lista.append(a)
    listb.append(b)
    i += 1
a = [x for x in lista if lista.count(x)==1]
b = [x for x in listb if listb.count(x)==1]
print(a[0], b[0])