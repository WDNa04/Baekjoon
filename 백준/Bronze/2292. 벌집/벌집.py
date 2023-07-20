import sys

number = sys.stdin.readline()
number = int(number)

i = 0
a = 1
while a < number:
    a += 6*(i)
    i += 1

if number == 1:
    print(i+1)
else:
    print(i)