import sys

while True:
    a, b, c = map(int, sys.stdin.readline().split())
    lista = [a,b,c]
    if a == b == c == 0:
        break
    if max(a, b, c) < a + b + c - max(a, b, c):
        if len(set(lista)) == 2:
            print("Isosceles")
        elif len(set(lista)) == 1:
            print("Equilateral")
        else:
            print("Scalene")
    else:
        print("Invalid")