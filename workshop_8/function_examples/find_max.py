import math
# wrtie a function which takes 2 numbers and returns biggest

def find_max(a, b):
    if a > b:
        return a
    return b

def find_max_in_list(numbers):
    m = -math.inf

    for num in numbers:
        m = find_max(num, m)

    return m

def find_max_in_many(*numbers):
    return find_max_in_list(numbers)


def find_priciest_product(products):
    priciest_product = products[0]

    for product in products[1:]:
        if product['price'] > priciest_product['price']:
            priciest_product = product

    return priciest_product



def main():
    numbers = [1, 3, 7, 99, -99, 100]
    print(f'{find_max(5, 7) = }')
    print(f'{find_max(8, 4) = }')
    print(f'{find_max(5, 5) = }')
    print(f'{find_max_in_list([-999999999999, -888888, -666, -555]) = }')
    print(f'{find_max_in_list([]) = }')
    print(f'{find_max_in_list(numbers) = }')
    print(f'{find_max_in_many(-999999999999, -888888, -666, -555) = }')
    print(f'{find_max_in_many(*numbers) = }')


if __name__ == '__main__':
    # guard clause
    main()






