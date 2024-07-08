tbilisi_temperature: list[float] = [
    25.5, 24.3, 27, 27.8, 29.5, 30.1, 31.2
]
print(sum(tbilisi_temperature) / len(tbilisi_temperature))

total_temperature: float = 0
# loop with list
for temperature in tbilisi_temperature:
    total_temperature += temperature

print(f"Average Temperature: {total_temperature / len(tbilisi_temperature)}")

for temperature in tbilisi_temperature: # this is called for loop
    # this is indented code that is called code block
    # every step of loop is called iteration
    # every entrance into the block is called iteration
    print(temperature)
    if temperature > 26:
        print("it is hot today")
    else:
        print("it is normal temperature")

# Range based loops
print(">>> 0 to 7 <<<")
for i in range(7):
    print(i)

print(">>> 3 to 7 <<<")
for i in range(3, 7):
    print(i)

print(">>> 0 to 10 | 2 steps <<<")
for i in range(0, 10, 2):
    print(i)


print("Daily report:")
# day 1; temperature is 25.5
for i in range(len(tbilisi_temperature)):
    # print(tbilisi_temperature[i])
    print(f"Day {i + 1} - Temperature is {tbilisi_temperature[i]}")

print("Daily report (enumerate function):")

# enumerate() function
for i, temperature in enumerate(tbilisi_temperature):
    print(f"Day {i + 1} - Temperature is {temperature}")
