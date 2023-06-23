import sys
while True:
    try:
        input = sys.stdin.readline()
        a,b = map(int,input.split())
        print(a+b)
    except:
        break

    