import sys

def prime(n):
    lista = []
    for i in range(1, n+1):
        if n % i == 0:
            lista.append(i)
    return len(lista)

def divide(n):
    for i in range(1,n+1):
        if prime(i) == 2 and n % i == 0:
            print(i)
            a = n/i
            divide(a)

number = int(sys.stdin.readline())
divide(number)