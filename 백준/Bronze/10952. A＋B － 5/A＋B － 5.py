import sys
while True:
    input = str(sys.stdin.readline())
    output = list(map(int,input.split()))
    if output == [0,0]:
        break
    print(output[0]+output[1])
