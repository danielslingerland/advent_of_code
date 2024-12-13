
class Lijst:
    def __init__(self, lijst):
        self.lijst = [int(x) for x in lijst]
    
    def isCorrectOplopendTweedeKans(self):
        for i in range(len(self.lijst)-1):
            dif = self.lijst[i+1]-self.lijst[i]
            if dif < 1 or dif > 3:
                zonder1 = [x for x in self.lijst]
                zonder2 = [y for y in self.lijst]
                zonder1.pop(i)
                zonder2.pop(i+1)
                return self.isCorrectOplopend(zonder1) or self.isCorrectOplopend(zonder2)
        return True
    
    def isCorrectOplopend(self, sublijst):
        for i in range(len(sublijst)-1):
            dif = sublijst[i+1]-sublijst[i]
            if dif < 1 or dif > 3:
                return False
        return True
    
    def isCorrectAflopendTweedeKans(self):
        for i in range(len(self.lijst)-1):
            dif = self.lijst[i]-self.lijst[i+1]
            if dif < 1 or dif > 3:
                zonder1 = [x for x in self.lijst]
                zonder2 = [y for y in self.lijst]
                zonder1.pop(i)
                zonder2.pop(i+1)
                return self.isCorrectAflopend(zonder1) or self.isCorrectAflopend(zonder2)
        return True
    
    def isCorrectAflopend(self, sublijst):
        for i in range(len(sublijst)-1):
            dif = sublijst[i]-sublijst[i+1]
            if dif < 1 or dif > 3:
                return False
        return True

def load_file():
    with open('data/day2.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def create_lists():
    lines = load_file()
    return [Lijst(line.split(" ")) for line in lines]
            
        


def main():
    lists = create_lists()
    safe = 0
    for lijst in lists:
        if(lijst.isCorrectAflopendTweedeKans() or lijst.isCorrectOplopendTweedeKans()):
            safe += 1
    print(safe)
main()