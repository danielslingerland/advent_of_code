from tqdm import tqdm

def load_file():
    with open('data/day19.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

lines = load_file()
towels = lines[0].split(", ")


class Token:
    def __init__(self, pattern, start, end):
        self.pattern = pattern
        self.start = start
        self.end = end
        self.cache = -1
    
    def count(self, maximaal):
        if self.end == maximaal: return 1
        if self.cache != -1: return self.cache
        total = 0
        for token in tokens[self.end]:
            total += token.count(maximaal)
        self.cache = total
        return total
    
    def printToken(self):
        print("Token{pattern: "+self.pattern+", start: "+str(self.start)+", end: "+str(self.end)+"}")

total = 0
for pattern in tqdm(lines[2:]):
    tokens = [[] for i in pattern]
    
    for towel in towels:
        for i in range(len(pattern)):
            if(pattern[i:].startswith(towel)):
                tokens[i].append(Token(towel, i, i+len(towel)))

    
    for zeros in tokens[0]:
        total += zeros.count(len(pattern))
print()
print(total)
