from tqdm import tqdm


class Point:
    def __init__(self, x, y, value):
        self.x = x
        self.y = y
        self.value = value

def load_file():
    with open('data/day8.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

lines = load_file()

antenas = [[0 for j in i] for i in lines]

MAX_X = len(antenas[0])
MAX_Y = len(antenas)

points = []
for y in range(len(lines)):
    for x in range(len(lines[0])):
        if lines[y][x]!="." :
            points.append(Point(x, y, lines[y][x]))

for point in tqdm(points):
    for other in points:
        if point.value == other.value and point != other:
            dif_x = point.x - other.x
            dif_y = point.y - other.y
            
            x = point.x
            y = point.y
            
            while x >= 0 and x < MAX_X and y >= 0 and y < MAX_Y:
                antenas[y][x] = 1
                x += dif_x
                y += dif_y
                

total = 0
for row in antenas:
    for number in row:
        total += number
print()
print(total)
        
