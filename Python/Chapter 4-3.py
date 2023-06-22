a = list(range(3,10,3))
print(a)

key_list = ["name", "hp", "mp", "level"]
value_list = ["peter", 200, 30, 5]
character = {}
for i in range(4):
    character[key_list[i]] = value_list[i]
print(character)

limit = 10000
i = 1
sum_value = 0
while i<limit:
    sum_value = sum_value + i
    i += 1
    if sum_value >10000:
        print("When you add {}, the sum exceeds {}, and the value at that point is {}.".format(i-1,limit,sum_value))
        break

max_value = 0
for i in range(1, 51):
    a = i
    b = 100 - i
    current = a*b
    if max_value < current:
        max_value = current
print("Max = {} * {} = {}".format(a, b, max_value))
