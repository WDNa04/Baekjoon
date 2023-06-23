number = str(input())
if int(number.split()[0]) > int(number.split()[1]):
    print(">")
elif int(number.split()[0]) < int(number.split()[1]):
    print("<")
else:
    print("==")