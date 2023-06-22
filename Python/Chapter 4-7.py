lista = [1, 2, 3,4,1,2,3,1,4,1,2,3]
print("In this list, the number of numbers used is {}".format(len(set(lista))))
dicta = {}
for i in set(lista):
    dicta[i] = lista.count(i)
print(dicta)

dna = str(input())
liste = ['a', 't', 'c', 'g']
for i in liste:
    print("{} count: {}".format(i, dna.count(i)))

nucleus = str(input())
i = 0
listf = []
dictb = {}
while i < len(nucleus):
    listf.append(nucleus[i:i+3])
    dictb[nucleus[i:i+3]] = listf.count(nucleus[i:i+3])
    i +=3
print(dictb)

listc = [1, 2, [3, 4], 5, [6, 7], [8,9]]
listd = []
for i in listc:
    if type(i) == list:
        for k in range(len(i)):
            listd.append(i[k])
    else:
        listd.append(i)
print(listd)


