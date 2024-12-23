with open('data/day23.txt') as f:
    lines = [line.rstrip('\n').split("-") for line in f]

groups= [{} for i in range(len(lines))]

class Node:
    def __init__(self, name):
        self.name = name
        self.neigbours = []
        
    def addNeigbour(self, neighbour):
        self.neigbours.append(neighbour)
    
    def group(self):
        for selfN in self.neigbours:
            for otherN in selfN.neigbours:
                if self in otherN.neigbours:
                    groups[3]["".join(sorted([selfN.name, otherN.name, self.name]))] = [selfN, otherN, self]

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.name == other.name
        return False
    
    def __hash__(self):
        return hash((self.name))

repo = {}

for line in lines:
    repo[line[0]] = Node(line[0])
    repo[line[1]] = Node(line[1])

for line in lines:
    n0 = repo[line[0]]
    n1 = repo[line[1]]
    n0.addNeigbour(n1)
    n1.addNeigbour(n0)

for k, node in repo.items():
    node.group()

for g in range(3, len(lines)):
    if len(groups[g]) > 0:
        print(str(len(groups[g])) + " party of size " + str(g))
    for group, nodes in groups[g].items():
        overlap = set(nodes[0].neigbours) & set(nodes[1].neigbours)
        for i in range(2, len(nodes)):
            overlap = overlap & set(nodes[i].neigbours)
        for lap in overlap:
            new = nodes + [lap]
            groups[g+1][",".join(sorted([node.name for node in new]))] = new

for g in range(3, len(lines)):
    total = 0
    for group, nodes in groups[g].items():
        total += 1
    if total == 1:
        print(next(iter(groups[g])))

