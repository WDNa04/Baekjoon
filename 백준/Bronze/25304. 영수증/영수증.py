price = int(input())
type = int(input())
list = []
for i in range(type):
    price_num = input()
    ind,num = map(int,price_num.split())
    list.append([ind,num])
final = 0
for i in range(len(list)):
    final += (list[i][0]*list[i][1])
if final == price:
    print("Yes")
else:
    print("No")

