def num(year):
    if year%4==0:
        if year%100!=0 or year%400==0:
            return 1
        else:
            return 0
    else:
        return 0

print(num(int(input())))