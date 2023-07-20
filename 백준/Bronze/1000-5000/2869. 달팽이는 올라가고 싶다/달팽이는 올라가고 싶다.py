import sys
import math
number = sys.stdin.readline()
a,b,c = map(int,number.split())

"""
i = 0
s = 0
while s < c:
    s += a
    i += 1
    if s < c:
        s -= b
    else:
        print(i)
"""
"""
difference = a - b
if difference == 1:
    c = c - a
    result = c + 1
    print(result)
else:
    result = math.ceil(c / difference)
    print(result)
"""

result = math.ceil((c-b)/(a-b))
print(result)
