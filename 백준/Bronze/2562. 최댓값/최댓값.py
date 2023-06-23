import sys
list = []
for i in range(9):
    number = int(sys.stdin.readline())
    list.append(number)
print(max(list))
print(list.index(max(list))+1)
