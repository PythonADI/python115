first_name: str = input("Enter your first name: ")
# type casting
age: int = int(input("Enter your age: "))

print(f"{type(first_name) = }, {type(age) = }")
print(f"Hello {first_name}, you are {age} years old.")