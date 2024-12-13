from tqdm import tqdm

def load_file():
    with open('data/day11.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines[0]

NUM_CALCULATED = 1000

ITTERATIONS = 75

calcs = [[] for i in range(NUM_CALCULATED)]




class Stone:
    def __init__(self, number):
        self.number = number
        self.has_split = False
        self.child1 = None
        self.child2 = None
        self.c = 1

    
    def applyRules(self, left):
        if self.c != 1:
            return
        if left <= len(calcs[-1]) and left > 0 and (self.number < 10 or self.number >= 100) and self.number < NUM_CALCULATED:
            self.c = calcs[self.number][left-1]
            return
        if self.has_split:
            self.child1.applyRules(left)
            self.child2.applyRules(left)
            return
        if self.number == 0:
            self.number = 1
            return
        str_number = str(self.number)
        len_number = len(str_number)
        if len_number%2 == 0:
            middle = len_number // 2
            self.child1 = Stone(int(str_number[:middle]))
            self.child2 = Stone(int(str_number[middle:]))
            self.has_split = True
            return
        self.number *= 2024

    
    def toString(self):
        if not self.has_split:
            return str(self.number) + ' '
        return self.child1.toString() + self.child2.toString()
    
    def count(self):
        if not self.has_split:
            return self.c
        return self.child1.count() + self.child2.count()


for ii in tqdm(range(ITTERATIONS)):
    stones = [Stone(number) for number in range(NUM_CALCULATED)]
    for i in range(ii+1):
        for j in range(NUM_CALCULATED):
            stone = stones[j]
            k = ii + 1 - i
            stone.applyRules(k)
    for number in range(NUM_CALCULATED):
        calcs[number].append(stones[number].count()) 
print()
stones = [Stone(int(number)) for number in load_file().split(" ")]

total = 0
for stone in stones:
    for i in range(ITTERATIONS):
        j = ITTERATIONS - i
        stone.applyRules(j)
    count = stone.count()
    total += count
        
print(total)
    