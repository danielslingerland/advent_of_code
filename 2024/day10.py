

def load_file():
    with open('data/day10.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines



lines = load_file()

MAX_Y = len(lines)
MAX_X = len(lines[0])

reached = [[1 if letter == '0' else 0 for letter in line] for line in lines]

def countNeighbours(x, y, level):
    str_level = str(level)
    total = 0
    for dy in [-1, 1] :
        neigh_x = x
        neigh_y = y + dy
        if neigh_x >= 0 and neigh_x < MAX_X and neigh_y >= 0 and neigh_y < MAX_Y:
            if lines[neigh_y][neigh_x] == str_level:
                total += reached[neigh_y][neigh_x]
    for dx in [-1, 1] :
        neigh_x = x + dx
        neigh_y = y
        if neigh_x >= 0 and neigh_x < MAX_X and neigh_y >= 0 and neigh_y < MAX_Y:
            if lines[neigh_y][neigh_x] == str_level:
                total += reached[neigh_y][neigh_x]
   
           
                   
    return total

for i in range(1, 10):
    str_i = str(i)
    for x in range(MAX_X):
        for y in range(MAX_Y):
            if lines[y][x] == str_i:
                reached[y][x] = countNeighbours(x, y, i-1)

total = 0
for x in range(MAX_X):
    for y in range(MAX_Y):
        if lines[y][x] == '9':
            total += reached[y][x]

print(total)
        