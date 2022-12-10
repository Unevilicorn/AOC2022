import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.read().splitlines()


class Instruction:
    def execute(self, register):
        pass


class Add(Instruction):
    def __init__(self, value):
        self.cycle = 0
        self.value = value

    def execute(self, register):
        if self.cycle == 0:
            self.cycle += 1
            return False, register
        return True, register + self.value

    def __repr__(self):
        return "addx {}".format(self.value)


class NOOP(Instruction):
    def execute(self, register):
        return True, register

    def __repr__(self):
        return "noop"


instrs = []
for line in lines:
    s = line.split(" ")
    if s[0] == "addx":
        instrs.append(Add(int(s[1])))
    else:
        instrs.append(NOOP())

cycles = [20, 60, 100, 140, 180, 220]
reg = 1
sums = 0
queue = []

i = 0
screen = []
while i < 240:
    i += 1
    if i in cycles:
        sums += i * reg
    if i <= len(instrs):
        queue.append(instrs[i - 1])

    if abs(reg - (i - 1) % 40) <= 1:
        screen.append("#")
    else:
        screen.append(".")

    if queue:
        used, reg = queue[0].execute(reg)
        if used:
            queue.pop(0)

print(sums)
for i in range(0, len(screen), 40):
    print("".join(screen[i : i + 40]))
