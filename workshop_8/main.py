# import function_examples.find_max as helpers
# from function_examples.find_max import *
# from function_examples.find_max import find_priciest_product as fpp
from function_examples.find_max import find_priciest_product

products = [
    {"name": "Iphone 15 pro", "price": 1100},
    {"name": "Iphone 15 Pro Max", "price": 1400},
    {"name": "Iphone 14 Pro", "price": 1000},
    {"name": "Iphone 14 Pro Max", "price": 1300},
    {"name": "Macbook Pro 2024 M3", "price": 2300},
]


def main():
    print(products)
    print(f"{find_priciest_product(products) = }")
    # print(f'{function_examples.find_max.find_priciest_product(products) = }')
    # print(f'{helpers.find_priciest_product(products) = }')
    # print(f'{fpp(products) = }')


if __name__ == "__main__":
    main()
