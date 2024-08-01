def f(x):
    print('f is called')
    result = x ** 2
    print(f'f is finished and is returning {result}')
    return result

def g(x):
    print('g is called')
    result = f(x - 1) + 1
    print(f'g is finished and is returning {result}')
    return result

def h(x):
    print('h is called')
    result = g(x - 3) + 2
    print(f'h is finished and is returning {result}')
    return result

x = h(6)


print('x value is', x)
