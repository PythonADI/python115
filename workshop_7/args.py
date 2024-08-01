print(1, 2, 2, 3, 4, 4, 5, 6)

def greet(*people, language='EN'):
    print(type(people), people)

    if language == 'GE':
        # * is an unpack operator
        # that means everything in peoples' list or tuple (iterbale)
        # will be spread / unpacked in print function
        print('გამარჯობა', *people)
    else:
        print('Hello', *people)
        

# people = ['Josh', 'Jane', 'Mary']
# greet(*people, language='GE')

# to pass language paramter a value we should use? - keyword argument
greet('Josh', 'Jane', 'Mary', language='GE')