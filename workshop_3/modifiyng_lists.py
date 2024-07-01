numbers = [1, 3, -7, 5, 100, 5, -1, 9]

print(numbers)
print(numbers[0])
print(numbers[len(numbers) - 1]) # last element
print(numbers[len(numbers) // 2])

# Change the value of an element
print("Change the first element to 100:")
numbers[0] = 100
print(numbers)


# Add an element to the end of the list
print("Append 200 to the list:")
numbers.append(200)
print(numbers)

# Remove the last element
print("Remove the last element:")
numbers.pop()
print(numbers)
