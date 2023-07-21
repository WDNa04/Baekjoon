import sys
lista = []
for i in range(3):
    number = int(sys.stdin.readline())
    lista.append(number)
if sum(lista) == 180:
    if len(set(lista)) == 2:
        print('Isosceles')
    elif len(set(lista)) == 1:
        print("Equilateral")
    else:
        print("Scalene")
else:
    print("Error")

