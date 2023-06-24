import sys
input = sys.stdin.readline()
lista = input.strip().split()
for i in range(len(lista)):
    lista[i] = lista[i][::-1]
lista = list(map(int,lista))
print(max(lista))