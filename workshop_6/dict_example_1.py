person = {
    'name': "Josh",
    'last_name': "doe",
}

person['last_name'] = 'boe'
print(person)
person['last_name'] = person['last_name'].upper()
print(person)
person['last_name'] = person['last_name'].title()
print(person)

person['age'] = 45
print(person)

person['age'] += 1
print(person)

person.pop('last_name')
print(person)
