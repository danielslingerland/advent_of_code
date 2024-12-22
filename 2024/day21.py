
test = ["029A","980A","179A","456A","379A"]
real = ["540A","839A","682A","826A","974A"]

fromA = {'0':'<A', '1': '^<<A', '3':'^A', '4':'^^<<A', '5':'<^^A', '6':'^^A', '8':'<^^^A' ,'9':'^^^A'}
from0 = {'A':'>A','2':'^A'}
from1 = {'7':'^^A'}
from2 = {'A':'v>A', '6':'^>A', '9':'^^>A'}
from3 = {'7': '<<^^A', '9':'^^A'}
from4 = {'A':'>>vvA', '0':'>vvA','5': '>A'}
from5 = {'4':'<A','6': '>A'}
from6 = {'A': 'vvA', '8':'<^A'}
from7 = {'4':'vA', '9':'>>A'}
from8 = {'0':'vvvA', '2': 'vvA', '3':'vv>A'}
from9 = {'A': 'vvvA', '7':'<<A', '8': '<A'}

route = {'A':fromA,'0':from0, '1': from1, '2': from2, '3':from3, '4':from4, '5':from5, '6':from6, '7':from7, '8':from8, '9': from9} 

cache = [{} for i in range(25)]


fA = {"^":"<A", ">":"vA", "v":"<vA", "<":"v<<A", "A":"A"}
fU = {"A":">A", ">":"v>A", "v":"vA", "<":"<vA", "^":"A"}
fL = {"A":">>^A", ">":">>A", "v":">A", "^":">^A", "<":"A"}
fD = {"A":"^>A", ">":">A", "<":"<A", "^":"^A", "v":"A"}
fR = {"A":"^A", "v":"<A", "<":"<<A", "^":"<^A", ">":"A"}
f = {"A":fA, "^":fU, "<":fL,"v":fD, ">":fR}

for fr, value in f.items():
    for to, v in value.items():
        cache[0][fr+to] = len(v)

def get(fr, to, depth):
    if fr+to in cache[depth] : 
        return cache[depth][fr+to]
    t = 0
    path = f[fr][to]
    previous = "A"
    for l in range(len(path)):
        t += get(previous,path[l], depth-1)
        previous = path[l]
    cache[depth][fr+to] = t
    return t

def getCode(code, depth):
    total = 0
    previous = "A"
    for i in range(len(code)):
        total += get(previous, code[i], depth-1)
        previous = code[i]
    return total

total = 0
for code in real:
    previous = "A"
    robot1 = ""
    for letter in code:
        robot1+=route[previous][letter]
        previous = letter
    l = getCode(robot1, 25)
    total += l * int(code[:-1])
print(total)
