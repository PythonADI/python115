import random

temps: list[int] = []

# populate a list with 100 random numbers (-5, 40)
for _ in range(100):
    temps.append(random.randint(-5, 40))

print(temps)

# calculate average
total: int = 0

for temp in temps:
    total += temp

print(f"average is: {total / len(temps)}")

print(f"max (function): {max(temps)}")
print(f"min (function): {min(temps)}")

m = temps[0]

for x in temps:
    if x < m:
        m = x

print(f"Minimum by our code: {m}")

m = temps[0]
for x in temps:
    if x > m:
        m = x
print(f"Maximum by our code: {m}")



