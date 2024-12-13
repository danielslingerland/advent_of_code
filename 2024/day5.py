import functools

def load_file(data):
    with open('data/'+data+'.txt') as f:
        lines = [line.rstrip('\n') for line in f]
    return lines



orders = [o.split("|") for o in load_file("day5_order")]
rows = [r.split(",") for r in load_file("day5_rows")]

def isOrderd(val1, row):
    positon_val1 = row.index(val1)
    for order in orders:
        if order[0]==val1 and order[1]!=val1:
            if order[1] in row and positon_val1-row.index(order[1])>0:
                return False
    return True

def rowIsOrdered(row):
    for number in row:
        if not isOrderd(number, row): return False
    return True

def order(val1, val2):
    for order in orders:
        if order[0] == val1 and order[1] == val2: return 1
        if order[1] ==  val1 and order[0] == val2: return -1
    return 0

total = 0

for row in rows:
    if not rowIsOrdered(row):
        sorted_row = sorted(row, key=functools.cmp_to_key(order))
        total += int(sorted_row[int((len(sorted_row)-1)/2)])
            
print(total)
        



