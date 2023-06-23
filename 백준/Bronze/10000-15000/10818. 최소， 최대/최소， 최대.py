import sys
number = sys.stdin.readline()
series = sys.stdin.readline()
list = list(map(int, series.split()))
print("{} {}".format(min(list), max(list)))
