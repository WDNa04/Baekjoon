import sys
while True:
    input = str(sys.stdin.readline())
    output1,output2 = map(int,input.split())
    if output1==output2==0:
        break
    print(output1+output2)
