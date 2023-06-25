import sys
lista = []
while True:
    input1 = sys.stdin.readline()
    input1 = input1.strip()
    if input1 == '':
        break
    else:
        lista.append(input1)
print('\n'.join(lista))