import sys
import string
word = (sys.stdin.readline()).strip()
alphabet = list(string.ascii_lowercase)
list = []
for i in alphabet:
    if i in word:
        list.append(word.index(i))
    if i not in word:
        list.append('-1')
print(*list)
