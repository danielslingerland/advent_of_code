from tqdm import tqdm

with open('data/day20.txt') as f:
    lines = [line.rstrip('\n') for line in f]

MAX_Y, MAX_X = len(lines), len(lines[0])
FROM_END, FROM_START = 0, 1

def mapLetter(letter):
    if letter == "#": return [-2, -2]
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

def runPathfinding(start, p):
    neighbours = [p]
    neighbours[0].setMemory(0, start)
    while len(neighbours) > 0:
        last = neighbours.pop()
        for neigh in last.getNeighbours():
            if neigh.memory(start) == -1 or neigh.memory(start) > last.memory(start) +1:
                neigh.setMemory(last.memory(start) +1, start)
                neighbours.append(neigh)

runPathfinding(FROM_END, find("E"))
runPathfinding(FROM_START, find("S"))

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
            if x + dx >= MAX_X or x + dx < 0: continue
            for dy in range(-(20-abs(dx)), (21-abs(dx))):
                if y + dy >= MAX_Y or y + dy < 0: continue
                distance = abs(dx) + abs(dy)
                total += evaluate(memory[y][x][FROM_END], memory[y+dy][x+dx][FROM_START], distance)

print()
print(total)