def flatten(data):
    output = []
    for item in data:
        if type(item)==list:
            output += flatten(item)
        else:
            output.append(item)
    return output

print(flatten([[1,2,3],[4,[5,6]],7,[8,9]]))

min = 2
max = 10
total = 100
memo = {}

def question(remain, sitted):
    key = str([remain, sitted])
    if key in memo:
        return memo[key]
    if remain <0:
        return 0
    if remain == 0:
        return 1
    count = 0
    for i in range(sitted, max +1):
        count+=question(remain-i, i)
    memo[key] = count
    return count

print(question(total, min))