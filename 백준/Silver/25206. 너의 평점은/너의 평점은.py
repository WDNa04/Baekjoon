import sys

lista = [
    ["A+", 4.5],
    ["A0", 4.0],
    ["B+", 3.5],
    ["B0", 3.0],
    ["C+", 2.5],
    ["C0", 2.0],
    ["D+", 1.5],
    ["D0", 1.0],
    ["F", 0.0],
]
d = 0
e = 0
for i in range(20):
    name = sys.stdin.readline()
    a, b, c = map(str, name.split())
    b = float(b)
    if c == 'P':
        pass
    else:
        d += b
        for i in lista:
            if c == i[0]:
                e += i[1] * b
print(e/d)
