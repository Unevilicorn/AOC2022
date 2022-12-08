import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.read().splitlines()


w = len(lines[0])
h = len(lines)

grid = []

for line in lines:
    grid.append(list(map(int, line)))

coords = set()

for i in range(h):
    cur = -1
    for j in range(w):
        if grid[i][j] > cur:
            cur = grid[i][j]
            coords.add((i, j))
            continue
    cur = -1
    for j in range(w - 1, -1, -1):
        if grid[i][j] > cur:
            cur = grid[i][j]
            coords.add((i, j))
            continue


for j in range(w):
    cur = -1
    for i in range(h):
        if grid[i][j] > cur:
            cur = grid[i][j]
            coords.add((i, j))
            continue
    cur = -1
    for i in range(h - 1, -1, -1):
        if grid[i][j] > cur:
            cur = grid[i][j]
            coords.add((i, j))
            continue

print(len(coords))


def score(r, c):
    dists = [0, 0, 0, 0]
    for i in range(r - 1, -1, -1):
        dists[0] += 1
        if grid[i][c] >= grid[r][c]:
            break

    for i in range(r + 1, h):
        dists[1] += 1
        if grid[i][c] >= grid[r][c]:
            break

    for j in range(c - 1, -1, -1):
        dists[2] += 1
        if grid[r][j] >= grid[r][c]:
            break

    for j in range(c + 1, w):
        dists[3] += 1
        if grid[r][j] >= grid[r][c]:
            break

    return dists[0] * dists[1] * dists[2] * dists[3]


m = -1
for i in range(h):
    for j in range(w):
        m = max(m, score(i, j))
print(m)
