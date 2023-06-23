import sys
input = int(sys.stdin.readline().strip())
for i in range(input):
    input2 = sys.stdin.readline().strip()
    a,b = map(int,input2.split())
    print(a+b)
