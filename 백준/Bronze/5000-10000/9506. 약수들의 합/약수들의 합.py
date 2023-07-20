import sys

while True:
    number = int(sys.stdin.readline())
    if number == -1:
        break
    lista = []
    for i in range(1,number):
        if number % i == 0:
            lista.append(i)
    if sum(lista) == number:
        line = ' + '.join(str(i) for i in lista)
        print("{} = {}".format(number, line))
    else:
        print("{} is NOT perfect.".format(number))
    