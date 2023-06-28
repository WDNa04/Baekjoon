import sys
lista = [['c=', 'č'], ['c-','ć'],['dz=','dž'], ['d-', 'đ'], ['lj','lj'],['nj','nj'],['s=','š'], ['z=','ž']]
name = sys.stdin.readline()
name = name.strip()
name2 = ''
listb = []
a = 0
i = 0
while i < len(name):
    name2 += name[i]
    for k in lista:
        if k[0] in name2:
            listb.append(k[0])
            name2 = name2.replace(k[0],'')
            a += len(name2)
            name2 = ''
        else:
            pass
    i+=1
    if i == len(name):
        a+=len(name2)

a += len(listb)
print(a)



