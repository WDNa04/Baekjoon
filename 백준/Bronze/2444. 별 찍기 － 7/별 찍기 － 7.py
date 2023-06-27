import sys

count = sys.stdin.readline()
count = int(count)
i = 1
while i <= count:
    stars = " " * (count - i) + "*" * (2 * i - 1)
    print(stars)
    if count - i == 0:
        for k in reversed(range(1, count)):
            hi = " " * (count - k) + "*" * (2 * k - 1)
            print(hi)
    i += 1