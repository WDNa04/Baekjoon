import datetime
now = datetime.datetime.now()

sentence = str(input("Enter: "))
if sentence == 'Hello':
    print("Hello")
elif sentence == "what time is it?":
    print("it is {} right now.".format(now.hour))
else:
    print(sentence)

number = int(input())
if number % 2==0:
    print("{} is divisible by 2.".format(number))
elif number %3 ==0:
    print("%d is divisible by 3."%(number))
elif number %4 ==0:
    print("{} is divisible by 4.".format(number))
elif number %5 ==0:
    print("{} is divisible by 5.".format(number))
