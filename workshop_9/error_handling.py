num1 = 1
num2 = 45

try:
    print(int(num2))
    print(num1 / num2)
except ZeroDivisionError as e:
    print('Nums must be non-zero')
except TypeError as e:
    print('Nums must be numbers')
except Exception as e:
    print('Uknown Error:', e, type(e))
finally:
    print('This will always run')
