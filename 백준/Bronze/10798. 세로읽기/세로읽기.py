import sys
lista = []
for i in range(5):
    line = sys.stdin.readline()
    lista.append(line.strip())
listb = list(reversed(sorted(lista, key = lambda x: len(x))))
for i in range(5):
    lista[i] = lista[i] + (len(listb[0])-len(lista[i]))*' '
line = ''
for k in range(len(listb[0])):
    for i in range(5):
        line += lista[i][k]
print(line.replace(' ', ''))