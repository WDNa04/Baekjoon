def mul(*values):
    multi=1
    for value in values:
        multi = multi*value
    return multi

print(mul(5, 7, 9, 10))

def factorial(n):
    output = 1
    for i in range(1, n+1):
        output = output * i
    return output
print(factorial(3))

def factorial(n):
    if n ==0:
        return 1
    else:
        return n*factorial(n-1)
print(factorial(3))

def fibonacci(n):
    if n ==1:
        return 1
    elif n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
print(fibonacci(4))

dictionary = {1:1, 2:1}
def fibonacci1(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci1(n-1) + fibonacci1(n-2)
        dictionary[n] = output
        return output
print(fibonacci1(50))