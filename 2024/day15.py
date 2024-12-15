from tqdm import tqdm

def load_file():
    with open('data/day15.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

class Robot:
    def __init__(self, x,y):
        self.x = x
        self.y = y
    def move(self, direction):
        self.x += direction.x
        self.y += direction.y


class Direction:
    def __init__(self, s):
        self.y = 0
        self.x = 0
        if s == "^": self.y = -1
        if s == "v": self.y = 1
        if s == "<": self.x = -1
        if s == ">": self.x = 1
        
area = []
directions = []
robot = None

for line in load_file():
    if(line.startswith("#")):
        row = []
        for letter in line:
            if letter == "@":
                row += ["@", "."]
            elif letter == "O":
                row += ["[", "]"]
            else:
                row += [letter, letter]
        area.append(row)
        continue
    for letter in line:
        directions.append(Direction(letter))

MAX_Y = len(area)
MAX_X = len(area[0])

moved = [[False for i in range(MAX_X)] for j in range(MAX_Y)]

for y in range(MAX_Y):
    for x in range(MAX_X):
        if area[y][x] == "@":
            robot = Robot(x, y)
            area[y][x] = "."

def canMoveVertical(x, y, area, dy):
    look_y = y + dy
    if area[look_y][x] == "#": return False
    if area[look_y][x] == ".": return True
    if area[look_y][x] == "[":
        return canMoveVertical(x,look_y,area,dy) and canMoveVertical(x+1,look_y,area,dy)
    if area[look_y][x] == "]":
        return canMoveVertical(x,look_y,area,dy) and canMoveVertical(x-1,look_y,area,dy)

def moveVertical(x, y, area, dy):
    if moved[y][x]: return
    moved[y][x] = True
    look_y = y + dy
    
    if area[look_y][x] == ".":
        area[look_y][x] = area[y][x]
    elif area[look_y][x] == "[":
        moveVertical(x,look_y,area,dy) 
        moveVertical(x+1,look_y,area,dy)
        area[look_y][x] = area[y][x]
    elif area[look_y][x] == "]":
        moveVertical(x,look_y,area,dy) 
        moveVertical(x-1,look_y,area,dy)
        area[look_y][x] = area[y][x]
    
def removeSingles(area):
    for y in range(MAX_Y):
        for x in range(MAX_X-1):
            if area[y][x] == "[" and area[y][x+1] != "]":
                area[y][x] = "."
            if area[y][x] != "[" and area[y][x+1] == "]":
                area[y][x+1] = "."
                
def moveHorizontal(robot, area, dx):
    look_x = robot.x + dx
    while(True):
        if area[robot.y][look_x] == "#": return
        if area[robot.y][look_x] == ".": 
            while area[robot.y][look_x-dx] != ".":
                area[robot.y][look_x] = area[robot.y][look_x-dx]
                look_x -= dx
            robot.move(direction)
            area[robot.y][robot.x] = "."
            return
        look_x += dx
        
def printArea():
    for y in range(MAX_Y):
        row = ""
        for x in range(MAX_X):
            if robot.x == x and robot.y == y:
                row += "@"
            else:
                row += area[y][x]
        print(row)

    
for direction in tqdm(directions):
    if direction.y == 0:
        moveHorizontal(robot, area, direction.x)
    else:
        if canMoveVertical(robot.x, robot.y, area, direction.y):
            moved = [[False for i in range(MAX_X)] for j in range(MAX_Y)]
            moveVertical(robot.x, robot.y, area, direction.y)
            robot.move(direction)
            removeSingles(area)
   

total = 0

for y in range(MAX_Y):
    for x in range(MAX_X):
        if area[y][x] == "[":
            total += y * 100 + x
print()
printArea()
print(total)
