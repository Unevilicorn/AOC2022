import os
import math

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.read().splitlines()


instrs = []
for line in lines:
    s = line.split()
    instrs.extend(s[0] * int(s[1]))

hp = (0, 0)
tp = (0, 0)
visited = set()

for instr in instrs:
    prev = hp
    if instr == "U":
        hp = (hp[0], hp[1] + 1)
    elif instr == "D":
        hp = (hp[0], hp[1] - 1)
    elif instr == "L":
        hp = (hp[0] - 1, hp[1])
    elif instr == "R":
        hp = (hp[0] + 1, hp[1])

    if max(abs(hp[0] - tp[0]), abs(hp[1] - tp[1])) > 1:
        tp = prev

    visited.add(tp)

print(len(visited))

file = open("output.txt", "w")

poses = [(0, 0) for _ in range(10)]
visited2 = set()
pi = ""
for ic, instr in enumerate(instrs):
    hp = poses[0]
    d = (0, 0)
    if instr == "U":
        d = (0, 1)
    elif instr == "D":
        d = (0, -1)
    elif instr == "L":
        d = (-1, 0)
    elif instr == "R":
        d = (1, 0)

    poses[0] = (hp[0] + d[0], hp[1] + d[1])

    for i in range(1, len(poses)):
        a, b = poses[i - 1], poses[i]
        dc, dr = a[0] - b[0], a[1] - b[1]
        if max(abs(dc), abs(dr)) > 1:
            dr = int(math.copysign(max(min(abs(dr), 1), 0), dr))
            dc = int(math.copysign(max(min(abs(dc), 1), 0), dc))
            poses[i] = (b[0] + dc, b[1] + dr)

    visited2.add((poses[-1]))

print(len(visited2))
