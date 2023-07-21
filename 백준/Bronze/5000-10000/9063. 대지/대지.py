import sys

count = int(sys.stdin.readline())
lista = []
listb = []
for i in range(count):
    a, b = map(int, sys.stdin.readline().split())
    lista.append(a)
    listb.append(b)
print((max(lista) - min(lista))*(max(listb) - min(listb)))
