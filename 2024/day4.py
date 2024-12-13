import re


pattern_mul = r'XMAS'




def load_file():
    with open('data/day4.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

#lines = ["XMAS", "AMAC", "AMAC", "XBCS"]
lines = load_file()
count = 0;

for line in lines:
    count += len(re.findall(pattern_mul, line))
    count += len(re.findall(pattern_mul, line[::-1]))
print(count)
rows = ['' for _ in range(len(lines[0]))]

for line in lines:
    for position in range(len(lines[0])):
        rows[position] += line[position]
        
for row in rows:
    count += len(re.findall(pattern_mul, row))
    count += len(re.findall(pattern_mul, row[::-1]))
    
print(count)

decending = ['' for _ in range(len(lines[0])*2-1)]
line_n = 0
for line in lines:
    for position in range(len(lines[0])*2-1):
        pick = line_n + position-len(lines[0])+1
        if pick >= 0 and pick < len(line):
            decending[position] += line[pick]
    line_n +=1 

for line in decending:
    count += len(re.findall(pattern_mul, line))
    count += len(re.findall(pattern_mul, line[::-1]))

print(count)
accending = ['' for _ in range(len(lines[0])*2-1)]
line_n = len(lines[0])
for line in lines:
    for position in range(len(lines[0])*2-1):
        pick = line_n + position-len(lines[0])
        if pick >= 0 and pick < len(line):
            accending[position] += line[pick]
    line_n -=1 
for line in accending:
    count += len(re.findall(pattern_mul, line))
    count += len(re.findall(pattern_mul, line[::-1]))

print(count)