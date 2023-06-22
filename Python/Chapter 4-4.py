example = ["A", 'B', 'C']
k = 0
for i in example:
    print("{} element is {}.".format(k,i))
    k+=1
for element in range(len(example)):
    print("{} element is {}.".format(element, example[element]))
for i, value in enumerate(example):
    print("{} element is {}.".format(i, value))
ex = {"A": 'a', "B":"b", "C":"c"}
print(ex.items())
for k,v in ex.items():
    print("{} value is {}".format(k,v))
array = ["A", "B", "C", "D"]
output = [i*2 for i in array if i!="B"]
print(output)
