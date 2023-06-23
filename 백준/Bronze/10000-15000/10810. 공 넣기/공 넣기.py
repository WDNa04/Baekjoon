import sys

N, M = map(int, (sys.stdin.readline()).split())
dicta = {}
for i in range(M):
    a, b, c = map(int, (sys.stdin.readline()).split())
    for i in range(a, b + 1):
        dicta[i] = c
for i in range(1, N + 1):
    if i not in dicta.keys():
        dicta[i] = 0
        dicta = dict(sorted(dicta.items()))

line = ""
for i in range(1, N + 1):
    line += str(dicta[i]) + " "
print(line)
