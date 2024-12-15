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

def giveAreaDirectionsAndRobot():
    area = []
    directions = []
    robot = None
    y = 0
    for line in load_file():
        if(line.startswith("#")):
            x = 0
            row = []
            for letter in line:
                if letter == "@":
                    row += [".", "."]
                    robot = Robot(x, y)
                elif letter == "O":
                    row += ["[", "]"]
                else:
                    row += [letter, letter]
                x += 2
            area.append(row)
            y += 1
            continue
        for letter in line:
            directions.append(Direction(letter))
    return area, directions, robot

area, directions, robot = giveAreaDirectionsAndRobot()


MAX_Y = len(area)
MAX_X = len(area[0])

def siblingDx(value):
    if value == "[": return 1
    if value == "]": return -1
    return 0

def canMoveVertical(x, y, dy):
    look_y = y + dy
    if area[look_y][x] == "#": return False
    if area[look_y][x] == ".": return True
    dx = siblingDx(area[look_y][x])
    return canMoveVertical(x,look_y,dy) and canMoveVertical(x+dx,look_y,dy)



def moveVertical(x, y, dy, moved):
    if moved[y][x]: return
    moved[y][x] = True
    look_y = y + dy
    
    if area[look_y][x] == ".":
        area[look_y][x] = area[y][x]
        return
    moveVertical(x,look_y,dy,moved) 
    moveVertical(x+siblingDx(area[look_y][x]),look_y,dy,moved)
    area[look_y][x] = area[y][x]
    
    
def removeSingles():
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
        if canMoveVertical(robot.x, robot.y, direction.y):
            moved = [[False for i in range(MAX_X)] for j in range(MAX_Y)]
            moveVertical(robot.x, robot.y, direction.y, moved)
            robot.move(direction)
            removeSingles()
   

total = 0

for y in range(MAX_Y):
    for x in range(MAX_X):
        if area[y][x] == "[":
            total += y * 100 + x
print()
printArea()
print(total)
