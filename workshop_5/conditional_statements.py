age: int = int(input("Enter your age: "))

if age < 18:
    # code block
    print("You are a minor.")
else:
    print("You are an adult.")


if age == 30:
    print("Wow, you are 30 years old.")


# if statement
if 0 <= age < 13:
    # if 0 <= age and age < 13:
    print("You are a minor.")
elif 13 <= age < 20:
    # elif 13 <= age and age < 20:
    print("You are a teenager.")
elif 20 <= age < 30:
    # elif 20 <= age and age < 30:
    print("You are young adult.")
else:
    print("You are an adult.")



