import sys
N, M = map(int, (sys.stdin.readline()).split())
lista = []
for i in range(1, N + 1):
    lista.append(i)
ball = 0
for i in range(M):
    a, b = map(int, (sys.stdin.readline()).split())
    ball = lista[a - 1]
    lista[a - 1] = lista[b - 1]
    lista[b - 1] = ball
line = ""
for i in range(N):
    line += (str(lista[i]) + " ")
print(line)
