first_name = "John"
last_name = "Doe"
age = 30
salary = 1000
is_married = True

first_name_2 = "Jane"
last_name_2 = "Doe"
age_2 = 25
salary_2 = 1200
is_married_2 = False


print(first_name, last_name, age, salary, is_married)
print(first_name_2, last_name_2, age_2, salary_2, is_married_2)

# List
first_names = ["John", "Jane", "Jack"] # list of strings
# everything in list are called elements
# elements are numbered starting from 0 and called index

print(first_names[0]) # Accessing elements in list
print(first_names[1])
print(first_names[2])

# List of integers
ages = [30, 25, 40]
print(ages[0])
print(ages[1])
print(ages[2])

# List of booleans
is_married = [True, False, True]

print(is_married[0])
print(is_married[1])
print(is_married[2])

print(f"{first_names[0]} is {ages[0]} years old and is married: {is_married[0]}")


# List of mixed data types
person = ["John", "Doe", 30, 1000, True]

print(person)
print(f"{person[0]} {person[1]} is {person[2]} years old and earns {person[3]} and is married: {person[4]}")

print(f'There are {len(person)} elements in list')
print(f'{len(person) = }')
# print(f'{5 + 6 = }')
