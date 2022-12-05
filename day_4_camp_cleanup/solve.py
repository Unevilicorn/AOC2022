import os
import string

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.readlines()

total1 = 0
total2 = 0
for line in lines:
    p1, p2 = line.split(",")
    p1s, p1e = p1.split("-")
    p2s, p2e = p2.split("-")

    p1r = set(range(int(p1s), int(p1e) + 1))
    p2r = set(range(int(p2s), int(p2e) + 1))

    if p1r.issubset(p2r) or p2r.issubset(p1r):
        total1 += 1

    if p1r & p2r:
        total2 += 1

print(total1)
print(total2)
