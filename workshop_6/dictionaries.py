person = {
    # key: value
    'name': "Josh",
    'age': 43
}

# accessing elements by key
print(person['name'], person['age'])

# adding new key values pairs
person['pet'] = 'German Shepherd'
print(person['pet'])
print(person)

# change
person['name'] = 'Jane'

# remove last added key value pair
# person.popitem()

# person.pop('name')
# del person['age']
# Key error when trying to pop non existent key
# person.pop('father')

person['friends'] = [
    'Jimmy', 'Jane', 'Jake'
]
print(person)

for friend in person['friends']:
    print(friend)


print('>>> Keys <<<')
for key in person.keys():
    print(key)

print('>>> Keys (method2) <<<')
for key in person:
    print(key, person[key])

print('>>> Values <<<')
for value in person.values():
    print(value)

print('>>> Items <<<')
for key, value in person.items():
    # key, value = item
    # print(item[0], item[1])
    print(key, value)

# key error when you try to access undefiend key value pair
# person['car']

# unpack
a, b = 5, 7
print(person.items())