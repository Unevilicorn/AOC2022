import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.read().splitlines()

# consumable list
ilines = iter(lines)

size = len(lines)

# take all the stacks
raw_stacks = []
for line in ilines:
    if line == "":
        break

    raw_stacks.append([])
    # remove square brackets in the line
    for i in range(1, len(line), 4):
        raw_stacks[-1].append(line[i])


# we've hit a new line, start parsing the stacks
stacks = [[] for _ in range(len(raw_stacks[-1]))]
for vals in reversed(raw_stacks[:-1]):
    for i, val in enumerate(vals):
        if val == " ":
            continue
        stacks[i].append(val)

instructions = []
for line in ilines:
    sl = line.split()
    instructions.append((int(sl[1]), int(sl[3]) - 1, int(sl[5]) - 1))

part_1_stacks = [stack[:] for stack in stacks]
for mc, f, t in instructions:
    for i in range(mc):
        part_1_stacks[t].append(part_1_stacks[f].pop())

print("".join([stack[-1] for stack in part_1_stacks]))

part_2_stacks = [stack[:] for stack in stacks]
for mc, f, t in instructions:
    ls = []
    for i in range(mc):
        ls.append(part_2_stacks[f].pop())
    part_2_stacks[t].extend(reversed(ls))

print("".join([stack[-1] for stack in part_2_stacks]))
