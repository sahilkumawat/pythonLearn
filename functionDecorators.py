#f(g(x))
def g(func):
    def square(x):
        x = func(x)
        return x * x
    return square

@g
def f(x):
    return x + 1

print(f(12))
