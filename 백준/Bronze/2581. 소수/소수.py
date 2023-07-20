import sys

def prime(n):
    lista = []
    for i in range(1, n+1):
        if n % i == 0:
            lista.append(i)
    return len(lista)


number1 = int(sys.stdin.readline())
number2 = int(sys.stdin.readline())
listb = []
for i in range(number1, number2+1):
    if prime(i) == 2:
        listb.append(i)
if len(listb) != 0:
    print(sum(listb))
    print(min(listb))
else:
    print('-1')

