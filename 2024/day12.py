from tqdm import tqdm

def load_file():
    with open('data/day12.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

class Coordinate:
    def __init__(self, x, y):
        self.x = x
        self.y = y



area = load_file()

MAX_Y = len(area)
MAX_X = len(area[0])

color = [[0 for i in range(MAX_X)] for j in range(MAX_Y)]

def giveNeighbours(coord):
    neighs = []
    letter = area[coord.y][coord.x]
    for dx in [1, -1]:
        x = coord.x + dx
        if(x >= 0 and x < MAX_X and color[coord.y][x] == 0 and area[coord.y][x] == letter):
            neighs.append(Coordinate(x, coord.y))
    for dy in [1, -1]:
        y = coord.y + dy
        if(y >= 0  and y < MAX_Y and color[y][coord.x] == 0 and area[y][coord.x] == letter):
            neighs.append(Coordinate(coord.x, y))
    return neighs

paint = 0

for y in tqdm(range(MAX_Y)):
    for x in range(MAX_X):
        if color[y][x] != 0: continue
        paint += 1
        neighbours = [Coordinate(x, y)]
        color[y][x] = paint
        while len(neighbours) > 0:
            neighs = giveNeighbours(neighbours.pop(-1))
            for neigh in neighs:
                color[neigh.y][neigh.x] = paint
                neighbours.append(neigh)

paint_sizes = [0]

for p in range(1, paint+1):
    paint_sizes.append(sum(row.count(p) for row in color))

total = 0

def fenceLengthHorizontal(inside, outside):
    inside_color = color[inside.y][inside.x]
    length = 1
    for direction in [1, -1]:
        outside_cursor_x = outside.x + direction
        outside_cursor_y = outside.y
        inside_cursor_x = inside.x + direction
        inside_cursor_y = inside.y
        while(inside_cursor_y >= 0 and inside_cursor_y < MAX_Y and inside_cursor_x >= 0 and inside_cursor_x < MAX_X and color[inside_cursor_y][inside_cursor_x] == inside_color and (outside_cursor_y < 0 or outside_cursor_y >= MAX_Y or outside_cursor_x < 0 or outside_cursor_x >= MAX_X or color[outside_cursor_y][outside_cursor_x] != inside_color)):
            outside_cursor_x += direction
            inside_cursor_x += direction
            length += 1
    return length

def fenceLengthVertical(inside, outside):
    inside_color = color[inside.y][inside.x]
    length = 1
    for direction in [1, -1]:
        outside_cursor_x = outside.x 
        outside_cursor_y = outside.y + direction
        inside_cursor_x = inside.x 
        inside_cursor_y = inside.y + direction
        while(inside_cursor_x >= 0 and inside_cursor_x < MAX_X and inside_cursor_y >= 0 and inside_cursor_y < MAX_Y and color[inside_cursor_y][inside_cursor_x] == inside_color and (outside_cursor_y < 0 or outside_cursor_y >= MAX_Y or outside_cursor_x < 0 or outside_cursor_x >= MAX_X or color[outside_cursor_y][outside_cursor_x] != inside_color)):
            outside_cursor_y += direction
            inside_cursor_y += direction
            length += 1   
    return length

for y in tqdm(range(MAX_Y)):
    for x in range(MAX_X):
        fences = 0.0
        for dx in [1, -1]:
            rx = x + dx 
            if(rx < 0 or rx >= MAX_X or area[y][rx] != area[y][x]):
                fl = fenceLengthVertical(Coordinate(x, y), Coordinate(rx, y))
                fences += 1.0/fl
        for dy in [1, -1]:
            ry = y + dy
            if(ry < 0 or ry >= MAX_Y or area[ry][x] != area[y][x]):
                fl = fenceLengthHorizontal(Coordinate(x, y), Coordinate(x, ry))
                fences += 1.0/fl
        total += fences * paint_sizes[color[y][x]]
print()
print(round(total))