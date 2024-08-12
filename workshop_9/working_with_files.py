# Read / Write / Append to a file

from pathlib import Path

# Read a file
BASE_DIR = Path(__file__).parent.resolve()
print('Base Directory:', BASE_DIR)
# quit()
f = open(BASE_DIR / 'data.txt', 'r', encoding='utf-8')

content = f.read()
print(content)
# f.seek(0)
# print(f.read())

f.close()


# Write to a file
f = open(BASE_DIR / 'data.txt', 'w', encoding='utf-8')

for _ in range(10):
    f.write('Hello World\n')


f.close()

# Append to a file
# f = open(BASE_DIR / 'data.txt', 'a', encoding='utf-8')

with open(BASE_DIR / 'data.txt', 'a', encoding='utf-8') as f:
    f.write('Hello World\n')

# f.close()