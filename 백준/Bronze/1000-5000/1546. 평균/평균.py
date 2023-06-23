number = int(input())
series = str(input())
list = []
for i in range(number):
    list.append(int((series.split())[i]))
lista = []
for i in range(number):
    lista.append(list[i]/max(list)*100)
print(sum(lista)/number)
