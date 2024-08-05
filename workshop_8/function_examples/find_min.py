import math

def find_min(a, b):
    if a < b:
        return a
    return b


def find_min_in_list(numbers):
    m = math.inf

    for num in numbers:
        m = find_min(num, m)
    
    return m

def find_min_in_many(*numbers):
    return find_min_in_list(numbers)



numbers = [-99, -100, 10, 100, 12, -112]
print(f'{find_min(5, 9) = }')
print(f'{find_min(-5, -9) = }')
print(f'{find_min_in_list([99999, -999, -99, 100, 0, 10]) = }')
print(f'{find_min_in_list(numbers) = }')
print(f'{find_min_in_many(*numbers) = }')




