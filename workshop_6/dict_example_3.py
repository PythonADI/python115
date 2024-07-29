person = {
    'name': 'josh',
    'last_name': 'doe',
    'firends': [
        {
            'name': 'Eka',
            'age': 32,
        },
        {
            'name': 'James',
            'age': 38
        },
        {
            'name': "George",
            'age': 41
        }
    ]
}

# persons' friends average age
print(person['firends'])
total_age = 0
for friend in person['firends']:
    total_age += friend['age']

print('AVG', total_age / len(person['firends']))
