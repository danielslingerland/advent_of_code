import re

def load_file():
    with open('data/day3.txt') as f:
        lines = f.read()
    return lines

text = load_file()

pattern_mul = r'mul\([0-9]+,[0-9]+\)'

dos = text.split("do()")
donts_removed = [do.split("don't()")[0] for do in dos]

total = 0
for do in donts_removed:
    muls = re.findall(pattern_mul, do)
    for mul in muls:
        zmul = mul[4:-1].split(",")
        total += int(zmul[0]) * int(zmul[1])

print(total)