import os

filepath = "./input"

with open(os.path.join(os.path.dirname(__file__), filepath)) as f:
    lines = f.readlines()


m = {"A": 0, "B": 1, "C": 2, "X": 0, "Y": 1, "Z": 2}

score_mat = [[4, 8, 3], [1, 5, 9], [7, 2, 6]]

total = 0
for line in lines:
    [f, s] = line.split()
    total += score_mat[m[f]][m[s]]

print(total)

out_mat = [[3, 4, 8], [1, 5, 9], [2, 6, 7]]

total = 0
for line in lines:
    [f, s] = line.split()
    total += out_mat[m[f]][m[s]]

print(total)
