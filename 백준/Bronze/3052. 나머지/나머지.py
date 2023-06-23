import sys
set = set()
for i in range(10):
    input = (sys.stdin.readline()).strip()
    add = int(input)%42
    set.add(add)
print(len(set))