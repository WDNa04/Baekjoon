import sys
number = int(sys.stdin.readline())
for i in range(number):
    input = (sys.stdin.readline()).strip()
    print("{}{}".format(input[0],input[-1]))
