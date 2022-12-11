import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.read()


class Monkey:
    def __init__(self, items, worry_fn, pred_fn, true_index, false_index):
        self.items = items
        self.worry_fn = worry_fn
        self.pred_fn = pred_fn
        self.true_index = true_index
        self.false_index = false_index

        self.inspec_count = 0

    def has_items(self):
        return len(self.items) > 0

    def inspect(self, div3=True):
        self.inspec_count += 1
        first = self.items.pop(0)
        first = self.worry_fn(first)

        if div3:
            first //= 3
        if self.pred_fn(first) == 0:
            return self.true_index, first
        return self.false_index, first


def parse_start_items(line):
    items = line.split(":")[-1].replace(" ", "").split(",")
    return list(map(int, items))


def parse_worry_fn(line):
    items = line.split("=")[-1].strip(" ")
    func = items.split(" ")

    if func[2] == "old":
        if func[1] == "+":
            return lambda x: x + x
        return lambda x: x * x

    num = int(func[2])

    if func[1] == "+":
        return lambda x: x + num
    return lambda x: x * num


def parse_pred_fn(line):
    item = line.split(" ")[-1]
    return lambda x: x % int(item), int(item)


def parse_true_index(line):
    item = line.split(" ")[-1]
    return int(item)


def parse_false_index(line):
    item = line.split(" ")[-1]
    return int(item)


monkeys = []
monkeys2 = []
all_mods = 1
for block in lines.split("\n\n"):
    minfo = block.split("\n")
    start_items = parse_start_items(minfo[1])
    worryinfo = parse_worry_fn(minfo[2])
    predinfo, pred_val = parse_pred_fn(minfo[3])
    true_index = parse_true_index(minfo[4])
    false_index = parse_false_index(minfo[5])
    monkeys.append(Monkey(start_items[:], worryinfo, predinfo, true_index, false_index))
    monkeys2.append(Monkey(start_items[:], worryinfo, predinfo, true_index, false_index))
    all_mods *= pred_val

for i in range(20):
    for monkey in monkeys:
        while monkey.has_items():
            index, item = monkey.inspect()
            monkeys[index].items.append(item)

counts = sorted([monkey.inspec_count for monkey in monkeys])
print(counts[-1] * counts[-2])

for i in range(10000):
    for monkey in monkeys2:
        while monkey.has_items():
            index, item = monkey.inspect(div3=False)
            monkeys2[index].items.append(item % all_mods)

counts = sorted([monkey.inspec_count for monkey in monkeys2])
print(counts[-1] * counts[-2])
