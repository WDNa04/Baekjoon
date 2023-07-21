import sys

count = int(sys.stdin.readline())
lista = []
listb = []
for i in range(count):
    a, b = map(int, input().split())
    lista.append(a)
    listb.append(b)
c = max(lista) - min(lista)
d = max(listb) - min(listb)
print(c * d)
