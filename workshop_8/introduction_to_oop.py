class Product:
    # class definition
    def __init__(self, name, price):
        # initialization
        self.name = name.title()
        if price < 0:
            raise ValueError('Price should be non-negative number')
        self.price = price

    def describe(self):
        print(self.name, self.price)

    def set_price(self, price):
        if price < 0:
            raise ValueError('Price should be non-negative number')
        self.price = price

# instance / object
product = Product('Iphone 15 pro', 1300)
product2 = Product('Iphone 15 pro max', 1400)
# product.price = -1000
product.set_price(1000)

# print(product.name, product.price, type(product))
# print(product2.name, product2.price)
product.describe()
product2.describe()

