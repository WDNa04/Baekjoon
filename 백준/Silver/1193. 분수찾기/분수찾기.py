import sys
number = int(sys.stdin.readline())

a = 0
s = 0
while s<number:
    a += 1
    s += a

c = number - s + a
b = a - c + 1
if a % 2 != 0:
    print("{}/{}".format(b, c))
elif a % 2 == 0:
    print("{}/{}".format(c, b))
