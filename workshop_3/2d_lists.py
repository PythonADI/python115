# 2D list
people = [
    ["John", "Doe", 30, 1000, True],
    ["Jane", "Doe", 25, 1200, False],
    ["Pope", "Doe", 40, 15000, True]
]

print(people, type(people))

print(f"{people[0][0]}")
print(f"{people[2][0]}'s salary is {people[2][3]}")
# IndexError when you try to access an index that does not exist
# print(people[5])