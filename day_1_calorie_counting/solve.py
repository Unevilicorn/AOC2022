import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.readlines()


cals = []
total = 0
for line in lines:
    if line == "\n":
        cals.append(total)
        total = 0 
    else:
        total += int(line)

cals.append(total)

print(max(cals))

sorted_cals = sorted(cals, reverse=True)
print(sum(sorted_cals[:3]))