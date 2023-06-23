def oven(number,y):
    H,M = [int(x) for x in number.split()]
    time = H*60+M
    final_time = time+y
    final_time_hour = final_time//60
    final_time_minute = final_time%60
    if final_time_hour>=24:
        final_time_hour-=24
    return str(final_time_hour)+" "+str(final_time_minute)

number = input()
y = int(input())
print(oven(number,y))
