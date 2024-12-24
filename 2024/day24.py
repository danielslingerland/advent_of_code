with open('data/day24.txt') as f:
    lines = [line.rstrip('\n').split(": ") for line in f]

operations = []

class Operation:
    def __init__(self, a1, op, a2, rs):
        self.a1 = a1
        self.op = op
        self.a2 = a2
        self.rs = rs

for line in lines:
    if len(line) == 1 and line[0] != "":
        s1 = line[0].split(" -> ")
        s2 = s1[0].split(" ")
        operations.append(Operation(s2[0], s2[1], s2[2], s1[1]))

FALSE_POSITIVE_MAX_Z = "z45"
FALSE_POSITIVE_MIN_X = "x00"
FALSE_POSITIVE_MIN_Y = "y00"

suspicious = []

for op in operations:
    if op.op =="XOR" and not op.a1[0] in ['x', 'y'] and op.rs[0] != "z":
        suspicious.append(op.rs)

for op in operations:
    if op.rs[0] == "z" and op.op != "XOR" and op.rs != FALSE_POSITIVE_MAX_Z:
        suspicious.append(op.rs)

counts = {}

for op in operations:
    counts[op.a1] = {"AND":0, "XOR":0, "OR": 0, "AND_RESULT": 0, "XOR_RESULT":0, "OR_RESULT":0, "SOURCE":""}
    counts[op.a2] = {"AND":0, "XOR":0, "OR": 0, "AND_RESULT": 0, "XOR_RESULT":0, "OR_RESULT":0, "SOURCE":""}
    counts[op.rs] = {"AND":0, "XOR":0, "OR": 0, "AND_RESULT": 0, "XOR_RESULT":0, "OR_RESULT":0, "SOURCE":""}

for op in operations:
    counts[op.a1][op.op] += 1
    counts[op.a2][op.op] += 1
    counts[op.rs][op.op+"_RESULT"] += 1
    counts[op.rs]["SOURCE"] = op.a1+" "+op.op+" "+op.a2

for key, count in counts.items():
    if FALSE_POSITIVE_MIN_X in count["SOURCE"] and FALSE_POSITIVE_MIN_Y in count["SOURCE"]: continue
    if count["OR"] == 1 and count["AND_RESULT"] != 1:
        suspicious.append(key)
    if count["AND"] == 1 and count["XOR"] == 1 and count["AND_RESULT"] == 1:
        suspicious.append(key)

print(",".join(sorted(list(set(suspicious)))))