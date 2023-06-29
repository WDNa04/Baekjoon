import sys
count = sys.stdin.readline()
a, b = map(int,count.split())
listc = []
for i in range(2*a):
    number = sys.stdin.readline()
    lista = list(map(int,number.split()))
    listc.append(lista)
print(listc)
for i in range(a):
    listd = []
    for l in range(b):
        listd.append(listc[i][l]+listc[i+a][l])
    print(*listd)


