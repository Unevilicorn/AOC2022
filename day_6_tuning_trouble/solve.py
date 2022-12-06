import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.read().splitlines()


for line in lines:
    for i in range(len(line) - 4):
        r = line[i : i + 4]
        if len(set(r)) == 4:
            print("Part 1:", i + 4)
            break


for line in lines:
    for i in range(len(line) - 14):
        r = line[i : i + 14]
        if len(set(r)) == 14:
            print("Part 2:", i + 14)
            break
