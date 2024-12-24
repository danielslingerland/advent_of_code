with open('data/day24.txt') as f:
    lines = [line.rstrip('\n').split(": ") for line in f]

memory = {}

operations = []


def AND(a1, a2):
    return a1 & a2

def OR(a1, a2):
    return a1 | a2

def XOR(a1, a2):
    return a1 ^ a2



class Opperation:
    def __init__(self, a1, op, a2, rs):
        self.a1 = a1
        self.op = op
        self.a2 = a2
        self.rs = rs
        self.executed = False
        self.printed = False
    
    def execute(self):
        if self.executed == True or not self.a1 in memory or not self.a2 in memory: return False
        if self.op == 'AND':
            memory[self.rs] = AND(memory[self.a1], memory[self.a2])
        elif self.op == 'OR':
            memory[self.rs] = OR(memory[self.a1], memory[self.a2])
        elif self.op == 'XOR':
            memory[self.rs] = XOR(memory[self.a1], memory[self.a2])
        self.executed = True
        return True
        

for line in lines:
    if len(line) > 1:
        memory[line[0]] = int(line[1])
    elif line[0] != "":
        s1 = line[0].split(" -> ")
        s2 = s1[0].split(" ")
        operations.append(Opperation(s2[0], s2[1], s2[2], s1[1]))

class Counts:
    def __init__(self):
        self.AND = 0
        self.XOR = 0
        self.OR = 0
        self.AND_RESULT = 0
        self.XOR_RESULT = 0
        self.OR_RESULT = 0
        self.SOURCE = ""




print("getting a feeling for how it works...")
second = []
for i in range(90):
    stats = {"AND":0, "OR":0, "XOR":0}
    s = []
    for op in operations:
        if op.printed: continue
        if (op.a1[0] in ['x', 'y'] or op.a1 in second) and (op.a2[0] in ['x', 'y'] or op.a2 in second):
            stats[op.op] += 1
            s.append(op.rs)
            op.printed = True
    second += s
        
    print(stats)


print("see the pattern...")

for op in operations:
    if op.op =="XOR" and not op.a1[0] in ['x', 'y']:
        print(op.rs)

print("identify the outliers...")
for op in operations:
    if op.op =="XOR" and not op.a1[0] in ['x', 'y'] and op.rs[0] != "z":
        print(op.rs)

print("found 6, 2 to go...")
print("print csv format for further analysis...")
counts = {}

for op in operations:
    counts[op.a1] = Counts()
    counts[op.a2] = Counts()
    counts[op.rs] = Counts()

for op in operations:
    if op.op == 'AND':
        counts[op.a1].AND += 1
        counts[op.a2].AND += 1
        counts[op.rs].AND_RESULT += 1
        counts[op.rs].SOURCE = op.a1+" "+op.op+" "+op.a2
    elif op.op == 'OR':
        counts[op.a1].OR += 1
        counts[op.a2].OR += 1
        counts[op.rs].OR_RESULT += 1
        counts[op.rs].SOURCE = op.a1+" "+op.op+" "+op.a2
    elif op.op == 'XOR':
        counts[op.a1].XOR += 1
        counts[op.a2].XOR += 1
        counts[op.rs].XOR_RESULT += 1
        counts[op.rs].SOURCE = op.a1+" "+op.op+" "+op.a2

for key, count in counts.items():
    print(key+";"+str(count.AND)+";"+str(count.XOR)+";"+str(count.OR)+";"+str(count.AND_RESULT)+";"+str(count.XOR_RESULT)+";"+str(count.OR_RESULT)+";"+str(count.SOURCE))

