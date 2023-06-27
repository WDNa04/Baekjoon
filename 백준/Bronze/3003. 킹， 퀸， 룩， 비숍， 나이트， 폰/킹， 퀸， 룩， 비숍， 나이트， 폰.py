import sys
count = sys.stdin.readline()
lista = list(map(int,count.split()))
dicta = {0:1, 1:1, 2:2, 3:2, 4:2, 5:8}
listb = []
for i in range(len(lista)):
    a = dicta[i] - lista[i]
    listb.append(a)
print(*listb)

