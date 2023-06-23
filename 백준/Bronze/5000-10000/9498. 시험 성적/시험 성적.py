def scorerange(score):
    if 90<=score<=100:
        return "A"
    elif score>=80:
        return "B"
    elif score>=70:
        return "C"
    elif score>=60:
        return "D"
    else:
        return "F"

print(scorerange(int(input())))