import sys
lista = []
listb = []
for i in range(9):
    a = sys.stdin.readline()
    for k in a.split():
        lista.append(int(k))
    number = list(map(int,a.split()))
    listb.append(number)
b = max(lista)
print(b)
for i in range(len(listb)):
    if b in listb[i]:
        c = listb[i].index(b)
        print(str(i+1) + ' ' + str(c+1))
        break

