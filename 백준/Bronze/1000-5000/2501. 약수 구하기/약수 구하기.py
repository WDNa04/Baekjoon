import sys
number = sys.stdin.readline()
a, b = map(int,number.split())
lista = []
for i in range(1, a+1):
    if a % i == 0:
        lista.append(i)

if b > len(lista):
    print(0)
else:
    print(lista[b-1])