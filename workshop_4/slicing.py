tbilisi_temperature: list[float] = [
    25.5, 24.3, 27, 27.8, 29.5, 30.1, 31.2
]

# list[start:end:step]; Up to end


# first 5 values
print(tbilisi_temperature[0:5])
print(tbilisi_temperature[:5])

# middle 3 values
mid_point = (len(tbilisi_temperature) // 2) - 1
print(tbilisi_temperature[mid_point:mid_point + 3])

# last 5 values
print("Equivalent Slices:")
print(tbilisi_temperature[len(tbilisi_temperature) - 5:])
print(tbilisi_temperature[len(tbilisi_temperature) - 5:len(tbilisi_temperature)])
print(tbilisi_temperature[-5:])

# it will yield only 1 element because it's up to 1
print(tbilisi_temperature[:1])

# every second day's temperature
# print(tbilisi_temperature[1:len(tbilisi_temperature):2])
print(tbilisi_temperature[1::2])

print(tbilisi_temperature[::-2]) # -1; -3; -5
# print(tbilisi_temperature[len(tbilisi_temperature) - 2:0:-2])
print(tbilisi_temperature[:])
# print(tbilisi_temperature[::])
print(tbilisi_temperature[::-1])
