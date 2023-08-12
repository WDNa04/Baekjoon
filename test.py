import sys

count = int(sys.stdin.readline())
sum = 0
for i in range(1,count-1):
    sum += (i * (i+1) / 2)
print(int(sum))
print(3)