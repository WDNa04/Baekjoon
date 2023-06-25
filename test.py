import sys
"""
lista = []
while True:
    input1 = sys.stdin.readline()
    input1 = input1.strip()
    if input1 == '':
        break
    else:
        lista.append(input1)
print('\n'.join(lista))

"""
with open('text.txt','w') as f:
    while True:
        input1 = sys.stdin.readline()
        input1 = input1.strip()
        if input1 == "":
            break
        else:
            f.write(input1+'\n')
with open('text.txt','r') as f:
    data = f.readlines()
    a = ''.join(data)
    print(a.strip())
