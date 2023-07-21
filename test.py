import sys

number = int(sys.stdin.readline())
v = 1
while True:
    list = []
    for i in range(1, v + 1):
        if v % i == 0:
            list.append(i)
    if number % v == 0 and len(list) == 2:
        number = int(number / v)
        print(v)
        if number == 1:
            break
    else:
        v += 1