program = [2,4,1,5,7,5,1,6,4,1,5,5,0,3,3,0]

def runProgram(a, b, c, itteration):
    ia = a
    b = a % 8
    b = b ^ 5
    c = a // 2 ** b
    b = b ^ 6 
    b = b ^ c
    out = b % 8
    a = a // 2 ** 3
    if itteration == 0 and out == program[itteration]:
        print(ia)
        return 
    if out != program[itteration]:
        return
    for i in range(8):
        runProgram(ia * 8 + i, b, c, itteration-1)
runProgram(3, 0, 0, len(program)-1)  