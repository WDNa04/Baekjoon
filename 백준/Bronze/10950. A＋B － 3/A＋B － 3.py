rangenum = int(input())
dict = {}
for i in range(rangenum):
    number = input()
    k,v = map(int,number.split())
    dict[k] = v
    print(k+v)

