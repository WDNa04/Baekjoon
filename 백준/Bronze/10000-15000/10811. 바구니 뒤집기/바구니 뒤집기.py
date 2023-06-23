import sys
list = []
input = sys.stdin.readline()
N,M = map(int,input.split())
for i in range(1,N+1):
    list.append(i)
for i in range(M):
    a,b = map(int,(sys.stdin.readline()).split())
    lista = list[a-1:b]
    lista.reverse()
    for i in range(a-1,b):
        list[i] = lista[i-a+1]
print(*list)

