import math
import sys
count = sys.stdin.readline()
count = int(count)
for i in range(count):
    number = int(sys.stdin.readline())
    lista = []
    listb = [25, 10, 5, 1]
    for i in listb:
        a = int(number//i)
        number -= a*i
        lista.append(a)
    print(*lista)