def f(x, y=0):
    return (x * 2) + y

def g(x, *, y):
    return x * y

print(f(5, 1))
# keyword arguments
print(f(x=5, y=1))
print(f(y=1, x=5))
print(f(5, y=1))
print(f(5))
print(f(x=5))

print(g(6, y=1))
