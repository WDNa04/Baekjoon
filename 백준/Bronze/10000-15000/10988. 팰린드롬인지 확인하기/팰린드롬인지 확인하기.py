import sys
name = sys.stdin.readline()
name = name.strip()
line = ''
for i in reversed(range(len(name))):
    line += name[i]
if line == name:
    print('1')
else:
    print('0')