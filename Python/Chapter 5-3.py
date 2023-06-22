numbers = [1,2,3,4,5,6]
print("::".join(map(str,numbers)))


number = list(range(1, 10+1))
print(list(filter(lambda x: x%2!=0,number)))
print(list(filter(lambda x: 3<=x<7, number)))
print(list(filter(lambda x: x**2 <50, number)))


