# Recursion Practice

def sum_digits(x):
    if x < 10:
        return x
    else:
        return (x % 10) + sum_digits(x//10)

print(sum_digits(123))

def factorial(x):
    if x == 1:
        return 1
    else:
        return x * factorial(x - 1)

print(factorial(5))

def cascade(x):
    print(x)
    if x < 10:
        return
    else:
        cascade(x//10)
        print(x)
        
cascade(2013)
