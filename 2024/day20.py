from tqdm import tqdm

with open('data/day20.txt') as f:
    lines = [line.rstrip('\n') for line in f]

MAX_Y = len(lines)
MAX_X = len(lines[0])
FROM_END = 0
FROM_START = 1

def mapLetter(letter):
    if letter == "#":
        return [-2, -2]
    return [-1, -1]

memory =[[mapLetter(letter) for letter in line] for line in lines]

neighbours = []
class P:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    
    def getNeighbours(self):
        neighbours = []
        for d in [1, -1]:
            if self.x + d >= 0 and self.x + d < MAX_X:
                neighbours.append(P(self.x + d, self.y))
            if self.y + d >= 0 and self.y + d < MAX_Y:
                neighbours.append(P(self.x, self.y + d))
        return neighbours
    
    def memory(self, start):
        return memory[self.y][self.x][start]
    
    def setMemory(self, value, start):
        memory[self.y][self.x][start] = value

def find(letter):
    for y in range(MAX_Y):
        for x in range(MAX_X):
            if lines[y][x] == letter:
                return P(x, y)


def runPathfinding(start, value):
    neighbours = [find(value)]
    neighbours[0].setMemory(0, start)
    while len(neighbours) > 0:
        last = neighbours.pop(-1)
        for neigh in last.getNeighbours():
            if neigh.memory(start) == -1 or neigh.memory(start) > last.memory(start) +1:
                neigh.setMemory(last.memory(start) +1, start)
                neighbours.append(neigh)

runPathfinding(FROM_END, "E")
runPathfinding(FROM_START, "S")

longDistance = find("S").memory(FROM_END)


def evaluate(m0, m2, distance):
    if m0 < 0 or m2 < 0: return 0
    if m0 + m2 + distance  <= longDistance - 100: 
        return 1
    return 0

total = 0
for x in tqdm(range(MAX_X)):
    for y in range(MAX_Y):
        for dx in range(-20, 21):
            for dy in range(-20, 21):
                distance = abs(dx) + abs(dy)
                if distance > 20: continue
                if x + dx >= MAX_X or y + dy >= MAX_Y: continue
                if x + dx < 0 or y + dy < 0: continue
                
                e1 = evaluate(memory[y][x][FROM_END], memory[y+dy][x+dx][FROM_START], distance)
                if e1 == 1:
                    total += 1

print()
print(total)

def printMap(start, fil):
    for line in memory:
        s = ""
        for pos in line:
            if pos[start] == -2:
                s += "|"+("#"*fil)
            elif pos[start] == -3:
                s += "|"+("-"*fil)
            elif pos == -1:
                s += "|"+str(pos[start]).zfill(fil)
            else:
                s += "|"+str(pos[start]).zfill(fil)
        print(s)


