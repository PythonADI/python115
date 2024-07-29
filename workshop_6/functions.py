def greet():
    # definition
    print("Hello")

# positional parameters
def f(x, y):
    result = x ** 2 - (y * 3)
    print(result)
    return result # this will be returned where function is call

for _ in range(10):
    greet() # call

s = 0
for i in range(7):
    # i and 7 are called arguments
    s += f(i, 7)

print(s)