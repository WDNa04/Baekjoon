import sys
input = int(sys.stdin.readline())
for i in range(input):
    number = str(sys.stdin.readline())
    input = list(map(int,number.split()))
    print("Case #{}: {} + {} = {}".format(i+1,input[0],input[1],sum(input)))
