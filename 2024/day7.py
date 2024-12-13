from tqdm import tqdm
import itertools
def load_file():
    with open('data/day7.txt') as f:
        lines = [Equation(line.rstrip('\n')) for line in f]
    return lines


class Equation:
    def __init__(self, line):
        self.result = int(line.split(": ")[0])
        self.values = [int(v) for v in line.split(": ")[1].split(" ")]
    
    def evaluate(self):
        for opperations in list(itertools.product([0, 1,2], repeat=len(self.values)-1)):
            test_result = self.values[0]
            i = 0
            for operation in opperations:
                i += 1
                
                if operation == 1:
                    test_result += self.values[i]
                if operation == 0:
                    test_result *= self.values[i]
                if operation == 2:
                    test_result = int(str(test_result)+str(self.values[i]))
            if test_result == self.result:
                return True
        return False

lines = load_file()
result = 0
for equation in tqdm(lines):
    if equation.evaluate():
        result += equation.result

print()
print(result)