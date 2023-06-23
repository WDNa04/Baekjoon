import sys
input1 = int(sys.stdin.readline())
input2 = sys.stdin.readline()
list = list(map(int,input2.split()))
number = int(sys.stdin.readline())
print(list[0:input1].count(number))