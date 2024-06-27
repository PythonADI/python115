first_name = "Melissa"  # hard coded value
last_name = "Apaza"
age = 32
# full_name = first_name + " " + last_name  # dynamic value
full_name = f"{first_name} {last_name}"  # f-string

full_name_title = full_name.title()

print(full_name_title)
print(full_name.upper())
print(full_name.lower())
print(full_name)

text = f"{full_name.title()} is {age} years old.\n\t\"In two years {full_name.title()} will be {age + 2} years old\""
text = f'{full_name.title()} is {age} years old.\n\t\'In two years {full_name.title()} will be {age + 2} years old\''
print(text)

# print("josh doe".title())
# print("john doe".upper())
# print("john doe".lower())
