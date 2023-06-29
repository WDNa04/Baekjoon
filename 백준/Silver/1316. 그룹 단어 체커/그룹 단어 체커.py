import sys

a = 0
def group(name):
    global a
    name2 = name
    for i in range(len(name)-1):
        if name[i+1] == name[i]:
            b = name[i]*2
            name2 = name2.replace(b,name[i])
        else:
            pass
    if len(name2) == len(set(name)):
        a += 1
    return a

number = int(sys.stdin.readline())
for i in range(number):
    name = sys.stdin.readline()
    name = name.strip()
    group(name)
print(a)
    