person = {
    'name': 'Joe',
    'last_name': 'doe',
    'job': 'Janitor',
    'job': 'President' # last key is used!
}
print(person)
specialization = {
    'job': 'Software Engineer',
    'degree': 'PhD',
    'salary': 105_000,
}

# combine specialization with person

# for key, value in specialization.items():
#     print(key, value)
#     person[key] = value

person.update(specialization)
print(person)
