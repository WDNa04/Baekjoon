pets = [
    {"name": "cloud", "age": 5},
    {"name": "coco", "age": 3},
    {"name": "arthur", "age": 1},
    {"name": "tiger", "age": 2},
        ]
print("# our pets")
for i in pets:
    print("{} {} years old".format(i["name"],i["age"]))

numbers = [1,2,6,8,4,3,2,1,9,5,4,9,7,2,1,3,5,4,8,9,7,2,3]
counter = {}
for number in numbers:
    if number not in counter:
        counter[number] = numbers.count(number)
print(counter)

character = {
    "name": "peter",
    "level":12,
    "items":{"sword":"sword of fire","armor": "diamond"},
    "skill":["cut","swish","kill"]
}
for key in character:
    if type(character[key]) is dict:
        for k in character[key]:
            print("{} : {}".format(k, character[key][k]))
    elif type(character[key]) is list:
        for i in character[key]:
            print("{} : {}".format(key,i))
    else:
        print("{} : {}".format(key,character[key]))
