with open('data/day25.txt') as f:
    lines = [line.rstrip('\n') for line in f]
    
locks = []
keys = []

i = 0
while(i < len(lines)):
    numbers = [0 for i in range(5)]
    for j in range(7):
        for l in range(5):
            if lines[i+j][l] == "#":
                numbers[l] += 1
    if lines[i][0] == "#":
        locks.append(numbers)
    else:
        keys.append(numbers)
    i += 8    

def fits(key, lock):
    for i in range(5):
        if key[i] + lock[i] > 7:
            return 0
    return 1

total = 0

for key in keys:
    for lock in locks:
        total += fits(key, lock)

print(total)
    
    
    