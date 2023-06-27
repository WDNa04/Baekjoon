import sys
name = sys.stdin.readline()
name = name.strip().lower()
lista = []
for i in name:
    if i not in lista:
        lista.append(i)
dicta = {}
listb = []
dictb = {}
for i in lista:
    dicta[i] = name.count(i)
for k,v in dicta.items():
    if v == max(dicta.values()):
        dictb[k] = v
if len(dictb) != 1:
    print('?')
else:
    listb = list(dictb)
    a = listb[0]
    print(a.upper())