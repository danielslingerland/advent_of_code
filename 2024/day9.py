from tqdm import tqdm
file_id = 0

def load_file():
    with open('data/day9.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

class Gap:
    def __init__(self, size, position):
        self.size = size
        self.filled = 0
        self.memory = [-1 for i in range(size)]
        self.position = position
    
    def add(self,file):
        for filepart in range(file.size):
            self.memory[self.filled] = file.id
            self.filled += 1
            self.size -= 1
        
    
class File:
    def __init__(self, size, fid, position):
        self.size = size
        self.id = fid
        self.position = position

line = load_file()[0]

i = 0
gaps = []
files =[]
pos= 0 
for letter in tqdm(line):
    if i%2 == 0:
        files.append(File(int(letter), file_id, pos))
        file_id += 1
    else:
        gaps.append(Gap(int(letter), pos))
    pos += int(letter)
    i += 1
    
for position in tqdm(range(len(files)-1, 0, -1)):
    for gap in gaps:
        if gap.position > files[position].position :
            break 
        if gap.size >= files[position].size:
            gap.add(files.pop(position))
            break

total = 0

for gap in gaps:
    reletive_pos = 0
    for memor in gap.memory:
        if memor == -1:
            break
        total += (gap.position+reletive_pos)*memor
        
        reletive_pos += 1

for file in files:
    reletive_pos = 0
    for f in range(file.size):
        total += (file.position+reletive_pos)*file.id 
        reletive_pos += 1 
    
print()   
print(total)        
        
    