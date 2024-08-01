def f(x):
    # x is a positional parameter
    print(x ** 2)

def g(x, y):
    print(x - y)

# 5 is an argument
f(5)
# positions matter!
g(5, 7)
g(7, 5)
g(8, 9)

