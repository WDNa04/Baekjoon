import sys
input = int(sys.stdin.readline())
for i in range(input):
    number = str(sys.stdin.readline())
    input = map(int,number.split())
    print("Case #{}: {}".format(i+1,sum(input)))
