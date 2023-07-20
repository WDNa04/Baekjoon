import sys

while True:
    number = sys.stdin.readline()
    a, b = map(int,number.split())
    if a == b == 0:
        break
    elif b % a == 0:
        print('factor')
    elif a % b == 0:
        print('multiple')
    else:
        print('neither')