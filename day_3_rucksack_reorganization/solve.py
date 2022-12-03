import os
import string

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.readlines()


v = "\n" + string.ascii_lowercase + string.ascii_uppercase
m = {v[i]: i for i in range(len(v))}

total = 0
for line in lines:
    mid = len(line) // 2
    l1, l2 = line[:mid], line[mid:]
    inter = set.intersection(set(l1), set(l2))
    for c in inter:
        total += m[c]

print(total)

total = 0

for i in range(0, len(lines), 3):
    l1, l2, l3 = lines[i], lines[i + 1], lines[i + 2]
    inter = set.intersection(set(l1), set(l2), set(l3))
    for c in inter:
        total += m[c]

print(total)
