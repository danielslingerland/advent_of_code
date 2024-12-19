from tqdm import tqdm

with open('data/day19.txt') as f:
    lines = [line.rstrip('\n') for line in f]
towels = lines[0].split(", ")

class Token:
    def __init__(self, start, end):
        self.start = start
        self.end = end
        self.cache = -1
    
    def count(self, maximaal):
        if self.end == maximaal: return 1
        if self.cache == -1:
            self.cache = 0
            for token in tokens[self.end]:
                self.cache += token.count(maximaal)
        return self.cache

total = 0
for pattern in tqdm(lines[2:]):
    tokens = [[] for i in pattern]
    for towel in towels:
        for i in range(len(pattern)):
            if(pattern[i:].startswith(towel)):
                tokens[i].append(Token(i, i+len(towel)))    
    for zeros in tokens[0]:
        total += zeros.count(len(pattern))
print()
print(total)
