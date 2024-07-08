# Data Structure
num: int = 5 # single value
# assignment operator
num += 7 #  num = num + 7

nums: list[int] = [1, 2, 3]
nums2: list[int] = [4, 5, 6, 7]

# list represents daily average temperature in Tbilisi
tbilisi_temperature: list[float] = [
    25.5, 24.3, 27, 27.8, 29.5, 30.1, 31.2
]

tbilisi_temperature_2: list[float] = [
   19.5, 20.3, 21, 22.8, 23.5, 24.1, 25.2
]

print(tbilisi_temperature[0])
print(tbilisi_temperature[-1])
print(tbilisi_temperature)
# quit()
# insert an element at a specific index
tbilisi_temperature.insert(0, 22.5)
tbilisi_temperature.insert(2, 25.5)
tbilisi_temperature.insert(-1, 29.5)

print(tbilisi_temperature)

# remove an element by value
tbilisi_temperature.remove(25.5)
print(f"After removing by value of 25.5: {tbilisi_temperature}")
# remove an element by index
tbilisi_temperature.pop(2)
print(f"After removing index 2: {tbilisi_temperature}")
# extend the list
tbilisi_temperature.extend(tbilisi_temperature_2)
print(f"After extending the list: {tbilisi_temperature}")

# remove all elements
tbilisi_temperature.clear()

print(f"After clearing the list: {tbilisi_temperature}")

