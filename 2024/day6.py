
from tqdm import tqdm
        

def load_file():
    with open('data/day6.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines


rows = [list(line) for line in load_file()] 


REACHABLE = [[False for i in range(len(rows[0]))] for j in range(len(rows))]
BLOCKED = [[letter == "#" for letter in row] for row in rows]

def inRangeY(val):
    return val >= 0 and val < len(rows)
def inRangeX(val):
    return val >= 0 and val < len(rows[0])

class Guard:
    def __init__(self, x, y):
        self.start_x = int(x)
        self.start_y = int(y)
        self.reset()
    
    def turn_right(self):
        prev_dx = self.dx
        self.dx = self.dy * -1
        self.dy = prev_dx
    
    def move(self):
        if not inRangeY(self.y + self.dy) or not inRangeX(self.x + self.dx): 
            self.isInside = False
            return False
        if BLOCKED[self.y+self.dy][self.x+self.dx]:
            self.turn_right()
            return self.move()
        self.x += self.dx
        self.y += self.dy
        self.visited[self.y][self.x] += 1
        if self.visited[self.y][self.x] > 4:
            return False
        return True
    
    
    def reset(self):
        self.x = self.start_x
        self.y = self.start_y
        self.dx= 0
        self.dy=-1
        self.isInside = True
        self.visited = [[0 for i in range(len(rows[0]))] for j in range(len(rows))]
                

def starting_guard():
    y = 0
    for row in rows:
        x = 0
        for column in row:
            if column == "^":
                return Guard(x, y)
            x+=1
        y+=1
        
guard = starting_guard()

count = 0

while(guard.move()):
    REACHABLE[guard.y][guard.x] = True
guard.reset()
for block_y in tqdm(range(len(rows))):
    for block_x in range(len(rows[0])):
        if not REACHABLE[block_y][block_x]: continue
        BLOCKED[block_y][block_x] = True
        while(guard.move()):
            pass
        if guard.isInside:
            count +=1
        BLOCKED[block_y][block_x] = False
        guard.reset()

    
print()         
print(count)
