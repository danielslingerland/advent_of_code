import numpy as np

def load_file():
    with open('data/day1.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

first = []
second= []

for line in load_file():
    split = line.split("   ")
    first.append(int(split[0]))
    second.append(int(split[1]))

np_second = np.array(second)
total = 0
for f in first:
    total += np.sum(np_second == f) * f

print(total)