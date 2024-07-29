"""
Data Structre: Tuple
- Immutable
- Ordered
"""

nums: list[int] = [1, 2, 3, 4, 5]
screen_size: tuple[int, int] = (1920, 1080)
print(screen_size, type(screen_size))

for pixels in screen_size:
    print(pixels)


# screen_size[0] = 1024
# assignment operator
screen_size = (3840, 2160)
for i, pixels in enumerate(screen_size):
    print(i, pixels)

print(len(screen_size))
