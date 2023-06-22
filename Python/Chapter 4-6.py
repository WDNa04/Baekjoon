output = [x for x in range(1,101) if ("{:b}".format(x)).count('0')==1]
for i in output:
    print("{} : {}".format(i, "{:b}".format(i)))
print("Sum:", sum(output))