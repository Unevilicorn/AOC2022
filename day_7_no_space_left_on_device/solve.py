import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.read().splitlines()


class File:
    def __init__(self, name, size) -> None:
        self.name = name
        self.size = size


class Dirs:
    def __init__(self, name, parent=None) -> None:
        self.name = name
        self.parent = parent
        self.dirs = []
        self.files = []

    def cd_dir(self, dir):
        if dir == "..":
            return self.parent

        if dir not in self.dirs:
            self.dirs.append(Dirs(dir, self))

        return self.dirs[-1]

    def add_dir(self, dir):
        self.dirs.append(dir)

    def add_file(self, file):
        self.files.append(file)

    def total_size(self):
        total = 0
        for file in self.files:
            total += file.size
        for dir in self.dirs:
            total += dir.total_size()
        return total

    def get_all_dir_size_less_than_100000(self):
        dirs = []
        subtotal = 0
        for dir in self.dirs:
            dirs.extend(dir.get_all_dir_size_less_than_100000())
            subtotal += dir.total_size()

        subtotal += sum([file.size for file in self.files])
        if subtotal < 100000:
            dirs.append(subtotal)
        return dirs

    def get_all_dir_sizes(self):
        dirs = []
        for dir in self.dirs:
            dirs.extend(dir.get_all_dir_sizes())
        dirs.append(self.total_size())
        return dirs


system = Dirs("/")
current = system
for line in lines[1:]:
    split = line.split(" ")
    if split[0] == "$":
        if split[1] == "cd":
            current = current.cd_dir(split[2])
    elif split[0] == "dir":
        current.add_dir(Dirs(split[1]))
    else:
        size = int(split[0])
        name = split[1]
        current.add_file(File(name, size))

print(sum(system.get_all_dir_size_less_than_100000()))


total_size = system.total_size()
needed_to_free = 30000000 - (70000000 - total_size)
sorted_sizes = sorted(system.get_all_dir_sizes())

for size in sorted_sizes:
    if size > needed_to_free:
        print(size)
        break
