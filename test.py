import sys
input = sys.stdin.readline()
a,b = map(int,input.split())
input2 = sys.stdin.readline()
list = list(map(int,input2.split()))
line = ""
for i in list:
    if i < b:
        line += "{} ".format(i)
print(line)