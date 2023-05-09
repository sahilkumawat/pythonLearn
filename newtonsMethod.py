def newtonsmethod(func, funcderiv, x, n):
    def f(x):
        f = eval(func)
        return f

    def df(x):
        df = eval(funcderiv)
        return df

    for i in range (1,n):
        i = x - (f(x)/df(x))
        x = i

    print("Root: ", x)

newtonsmethod("x**2 - 4", "2*x", 2, 10)
newtonsmethod("x**2 - 4", "2*x", -2, 10)
