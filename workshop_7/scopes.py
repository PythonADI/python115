# this is a global scope
def f(x):
    # every function has a local scope
    # x will be created and x shadows global x
    first_name = 'something'
    print('f', x, y, first_name)

def g(x):
    x = 17  # this will create a new local variable for g function
    print('g', x, y)

def modifies_global():
    global y
    y = 99
    print('Modified', y)


# first_name  # this is not defined
x = 7
y = 18
print(x)
x = 9
f(x + 1)
g(x - 1)
print(x)
modifies_global()
print('Global', y)

# Output:
# 7
# f 8
# g 6