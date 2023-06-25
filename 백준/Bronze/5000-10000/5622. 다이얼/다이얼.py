import string
import sys
dicta = {}
lista = list(string.ascii_uppercase)
lista = [x for x in lista if x not in ('W','X', 'Y', 'Z')]
i = 2
while i<=6:
    listb = []
    for k in lista[3*(i-1)-3:3*(i-1)]:
        listb.append(k)
    dicta[i] = listb
    i+=1
listc = ['P', 'Q', 'R', 'S']
dicta[7] = listc
liste = ['T', 'U', 'V']
dicta[8] = liste
listd = ['W','X', 'Y', 'Z']
dicta[9] = listd
input = sys.stdin.readline()
input = input.strip()
liste = list(input)
s = 0
i = 0
while i < len(liste):
    for k,v in dicta.items():
        if liste[i] in v:
            s+=int(k+1)
    i+=1
    
print(s)
