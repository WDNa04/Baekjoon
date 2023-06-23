import sys
list = []
for i in range(28):
    input = (sys.stdin.readline()).strip()
    list.append(input)
for i in range(1,31):
    if str(i) not in list:
        print(i)

    
