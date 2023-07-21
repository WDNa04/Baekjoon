import sys
number = sys.stdin.readline()
x, y, w, h = map(int, number.split())
print(min(abs(w-x), abs(h-y), x, y))
