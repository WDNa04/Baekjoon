number = int(input())
if number % 2 ==0:
    print(
        "The number entered is {}.\n"
        "{} is even.".format(number, number))
else:
    print((
        "The number entered is {}.\n"
        "{} is odd."
    ).format(number, number))

a = int(input("a: "))
if a % 2 ==0:
    print("\n".join(["The number entered is {}.","{} is even."]).format(a,a))
else:
    print("\n".join(["The number entered is {}.","{} is odd."]).format(a, a))