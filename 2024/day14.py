
MAX_X = 101
MAX_Y = 103

def load_file():
    with open('data/day14.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines


class Robot:
    def __init__(self, line):
        sline = line.split(" ")
        p = sline[0].split("=")[1].split(",")
        v = sline[1].split("=")[1].split(",")
        self.x = int(p[0])
        self.y = int(p[1])
        self.dx= int(v[0])
        self.dy= int(v[1])
    
    def move(self):
        self.x = (self.x + self.dx)%MAX_X
        self.y = (self.y + self.dy)%MAX_Y

def not_mirror(picture):
    not_morrored = 0
    for line in picture:
        for x in range(round((MAX_X)/2)):
            if line[x] != line[-(x+1)]: 
                not_morrored +=1
    return not_morrored

robots = [Robot(line) for line in load_file()]

seconds = 0
while(True):
    seconds += 1
    for robot in robots:
        robot.move()
        
    picture = [[0 for x in range(MAX_X)] for y in range(MAX_Y)]
    for robot in robots:
        picture[robot.y][robot.x] += 1
    if(not_mirror(picture) < 380):
        print("-"*MAX_X)
        for line in picture:
            print("".join(map(str, line)).replace("0", ".").replace("1", "X"))
        print("-"*MAX_X)
        print(seconds)
        break
