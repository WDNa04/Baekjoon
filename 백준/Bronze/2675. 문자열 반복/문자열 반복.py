import sys
count = int(sys.stdin.readline())
for i in range(count):
    input = sys.stdin.readline()
    a,b = input.split()
    line = ""
    for i in b:
        line+= (i*int(a))
    print(line)