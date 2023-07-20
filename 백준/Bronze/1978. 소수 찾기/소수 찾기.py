import sys

def prime(n):
    lista = []
    for i in range(1, n+1):
        if n % i == 0:
            lista.append(i)
    return len(lista)


count = int(sys.stdin.readline())
number = sys.stdin.readline()
listb = list(map(int, number.split()))
a = 0
for i in listb:
    if prime(i) == 2:
        a += 1
print(a)
