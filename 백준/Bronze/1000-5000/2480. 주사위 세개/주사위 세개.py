def dice(number):
    a,b,c = [int(x) for x in number.split()]
    if a==b==c:
        return 10000+a*1000
    elif a==b:
        return 1000+a*100
    elif b==c:
        return 1000+b*100
    elif c==a:
        return 1000+c*100
    else:
        return max(a,b,c) * 100

number = input()
print(dice(number))