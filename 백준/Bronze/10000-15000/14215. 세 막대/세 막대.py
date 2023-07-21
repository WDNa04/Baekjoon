import sys

a, b, c = map(int, sys.stdin.readline().split())
if max(a, b, c) < a + b + c - max(a, b, c):
    print(a + b + c)
else:
    d = a + b + c - max(a, b, c)
    print(2 * d - 1)
