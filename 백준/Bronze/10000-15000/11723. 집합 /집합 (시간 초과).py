import sys
count = int(sys.stdin.readline())
seta = set()
def add(x):
    return seta.add(x)
def remove(x):
    return seta.remove(x)
def check(x):
    if x in seta:
        return 1
    else:
        return 0
def toggle(x):
    if x in seta:
        return seta.remove(x)
    else:
        return seta.add(x)
def all():
    seta = set([x for x in range(1,21)])
    return seta
def empty():
    seta = set()
    return seta

for i in range(count):
    try:
        input = sys.stdin.readline()
        lista = list(input.split())
        a = lista[0]
        b = lista[1]
        b = int(b)
        if a == 'add':
            add(b)
        elif a =='check':
            print(check(b))
        elif a == 'remove':
            remove(b)
        elif a== 'toggle':
            toggle(b)
    except:
        if a=='all':
            seta = all()
        elif a == 'empty':
            seta = empty()
    