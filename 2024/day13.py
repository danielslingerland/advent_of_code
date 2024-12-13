import math


def load_file():
    with open('data/day13.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines

def extract(line, splitter):
    ls = line.split(splitter)
    x = int(ls[1].split(",")[0])
    y = int(ls[2])
    return Vector(x, y)

class Slotmachine:
    def __init__(self, a, b, prize):
        self.a = a
        self.b = b
        self.prize = Vector(prize.x + 10000000000000, prize.y + 10000000000000)
    
    def toString(self):
        return "Slot{a="+self.a.toString()+", b="+self.b.toString()+", prize="+self.prize.toString()+"}"
    
    def test(self, ma, mb):
        x = (self.a.x * ma) + (self.b.x *mb)
        y = (self.a.y * ma) + (self.b.y *mb)
        return x == self.prize.x and y == self.prize.y

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.magnitude = math.sqrt(x ** 2 + y ** 2)
    
    def dot(self, v2):
        return self.x * v2.x + self.y * v2.y
    
    def toString(self):
        return "("+str(self.x)+", "+str(self.y)+")"
        
def loadSlotmachines():
    lines = load_file()
    slots = []
    for i in range(0, len(lines), 4):
        a = extract(lines[i], "+")
        b = extract(lines[i+1], "+")
        prize = extract(lines[i+2], "=")
        slots.append(Slotmachine(a, b, prize))
    return slots
      

def angleBetweenVectors(vector1, vector2):
    return math.acos(vector1.dot(vector2) / (vector1.magnitude * vector2.magnitude))


def runSlot(slot):
    angle_a = angleBetweenVectors(slot.a, slot.prize)
    angle_b = angleBetweenVectors(slot.b, slot.prize)
    angle_ab = angleBetweenVectors(slot.a, slot.b)
    
    a_div_sin_A = slot.prize.magnitude / math.sin(angle_ab)
    c = round((a_div_sin_A * math.sin(angle_b))/slot.a.magnitude)
    b = round((a_div_sin_A * math.sin(angle_a))/slot.b.magnitude)
    
    if (slot.test(c, b)):
        return c * 3 + b
    return 0    

total = 0

for slot in loadSlotmachines():
    total += runSlot(slot)
                
        
print(total)     

            