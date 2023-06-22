list1 = []
for i in range(5):
    name = input("Name: ")
    if name != 'Done':
        list1.append(name)
    elif name == "Done":
        break
for i in range(len(list1)):
    print(list1[i])
