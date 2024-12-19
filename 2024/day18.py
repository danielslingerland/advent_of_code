from tqdm import tqdm

def load_file():
    with open('data/day18.txt') as f:
        lines = [P.parse(line.rstrip('\n')) for line in f]
    return lines

MAX= 70

class P:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    @classmethod    
    def parse(cls, line):
        x = int(line.split(",")[0])
        y = int(line.split(",")[1])
        return cls(x, y)
    
    def getNeighbours(self):
        neighbours = []
        for d in [1, -1]:
            if self.x + d >= 0 and self.x + d <= MAX:
                neighbours.append(P(self.x + d, self.y))
            if self.y + d >= 0 and self.y + d <= MAX:
                neighbours.append(P(self.x, self.y + d))
        return neighbours
    
    def memory(self):
        return memory[self.y][self.x]
    
    def setMemory(self, value):
        memory[self.y][self.x] = value

data = load_file()        

memory =[[-1 for x in range(MAX+1)] for y in range(MAX+1)]

print(len(data))
LOAD = 2906


#MAX_LOAD = 3450
# 1024 = positive
# 2000 = positive
# 2500 = positive
# 2750 = positive
# 2800 = positive
# 2900 = positive
# 2903 = positive
# 2905 = positive
# 2906 = negative
# 2912 = negative
# 2925 = negative
# 2950 = negative
# 3000 = negative

l = 0
for corrupt in data:
    l += 1
    memory[corrupt.y][corrupt.x] = -2
    if l == LOAD: break

neighbours = [P(0, 0)]
memory[0][0] = 0

while len(neighbours) > 0:
    last = neighbours.pop(-1)
    for neigh in last.getNeighbours():
        if neigh.memory() == -1 or neigh.memory() > last.memory() +1:
            neigh.setMemory(last.memory() +1)
            neighbours.append(neigh)

    
for line in memory:
    s = ""
    for pos in line:
        if pos == -2:
            s += "|"+("#"*3)
        elif pos == -1:
            s += "|"+str(pos).zfill(3)
        else:
            s += "|"+str(pos).zfill(3)
    print(s)

print(str(data[2906-1].x)+","+str(data[2906-1].y))