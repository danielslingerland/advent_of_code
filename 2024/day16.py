from tqdm import tqdm

def load_file():
    with open('data/day16.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

area = [[s for s in line] for line in load_file()]
MAX_Y = len(area)
MAX_X = len(area[0])

distance_area = []

for line in area:
    distance_area.append([])
    for letter in line:
        if letter == "S":
            distance_area[-1].append(0)
        elif letter == "." or letter == "E":
            distance_area[-1].append(-1)
        else:
            distance_area[-1].append(-2)

find = 0
while(distance_area[1][-2] == -1):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if distance_area[y][x] == find:
                for dx in [-1, 1]:
                    if distance_area[y][x+dx] == -1 or distance_area[y][x+dx] > find:
                        if distance_area[y][x-dx] == find-1 or distance_area[y][x-dx]  == find - 1001:
                            distance_area[y][x+dx] = find+1
                        elif distance_area[y][x+dx] > find + 1000 or distance_area[y][x+dx] == -1:
                            distance_area[y][x+dx] = find+1001
                for dy in [-1, 1]:
                    if distance_area[y + dy][x] == -1 or distance_area[y + dy][x] > find:
                        if distance_area[y - dy][x] == find-1 or distance_area[y - dy][x]  == find - 1001:
                            distance_area[y + dy][x] = find+1
                        elif distance_area[y + dy][x] > find + 1000 or distance_area[y + dy][x] == -1:
                            distance_area[y + dy][x] = find+1001
    if find%1000 == 0:
        print(find)
    find += 1

for line in distance_area:
    sline = ""
    for number in line:
        if number == -2:
            sline += "|"+("#"*6)
        else:
            sline += "|"+str(number).zfill(6)
        
    print(sline)


print(distance_area[1][-2])