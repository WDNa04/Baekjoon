def alarm(number):
    output = list(map(int,number.split(" ")))
    H = output[0]
    M = output[1]
    time = H*60+M
    final_time = time-45
    final_time_hour = final_time//60
    final_time_minute = final_time%60
    if final_time_hour<0:
        final_time_hour += 24
    return str(final_time_hour)+" "+str(final_time_minute)

print(alarm(input()))
