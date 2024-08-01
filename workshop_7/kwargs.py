# kwargs - keyword arguments
def f(**kwargs):
    print(type(kwargs), kwargs)


def g(*args):
    print(type(args), args)


f(name="luka", last_name="tavkhelidze")
g(1, 2, 3, 4, 5, 6, 7)
