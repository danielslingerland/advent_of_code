from tqdm import tqdm


def load_file():
    with open('data/day16_2.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def mapInt(value):
    if value == "######":
        return -10000
    return int(value)

results = [[mapInt(number) for number in line.split("|")[1:]] for line in load_file()]

MAX_Y = len(results)
MAX_X = len(results[0])

part_of_path = [[0 for i in range(MAX_X)] for j in range(MAX_Y)]

part_of_path[1][-2] = 1
print(results[1][-2])
print(part_of_path[1][-2])
for i in tqdm(range(115476, -1, -1)):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if  i == results[y][x] and part_of_path[y][x] == 1:
                for dx in [1, -1]:
                    diff = results[y][x] - results[y][x+dx]
                    if diff == 1 or diff == 1001:
                        part_of_path[y][x+dx] = 1
                for dy in [1, -1]:
                    diff = results[y][x] - results[y+dy][x]
                    if diff == 1 or diff == 1001:
                        part_of_path[y+dy][x] = 1
                for dx in [2, -2]:
                    if x + dx < 0 or x + dx >= MAX_X:  continue
                    if results[y][x+int(dx/2)] == -10000: continue
                    diff = results[y][x] - results[y][x+dx]
                    if diff == 2 or diff == 1002:
                        part_of_path[y][x+dx] = 1
                for dy in [2, -2]:
                    if y + dy < 0 or y + dy >= MAX_Y:  continue
                    if results[y+int(dy/2)][x] == -10000: continue
                    diff = results[y][x] - results[y+dy][x]
                    if diff == 2 or diff == 1002:
                        part_of_path[y+dy][x] = 1

total =0

for line in part_of_path:
    for number in line:
        total += number
print()
for line in part_of_path:
    sline = ""
    for number in line:
        if number == 1:
            sline += "0"
        else:
            sline += "."
        
    print(sline)

print(total, "manually remove false positives")
