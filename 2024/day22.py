from tqdm import tqdm

with open('data/day22.txt') as f:
    lines = [int(line.rstrip('\n')) for line in f]

memory = [[[[[-1 for i in range(19)] for j in range(19)] for k in range(19)] for l in range(19)] for line in lines]

PRUNE_VALUE = 16777216

def cycle(secret_number):
    return step3(step2(step1(secret_number)))

def step1(secret_number):
    secret_number ^= secret_number * 64
    secret_number %= PRUNE_VALUE
    return secret_number

def step2(secret_number):
    secret_number ^= secret_number // 32
    secret_number %= PRUNE_VALUE
    return secret_number

def step3(secret_number):
    secret_number ^= secret_number * 2048
    secret_number %= PRUNE_VALUE
    return secret_number


for l in tqdm(range(len(lines))):
    q = []
    secret_number = lines[l]
    for i in range(2000):
        secret_number = cycle(secret_number)
        q.append(secret_number%10)
        if i > 3:
            
            d0 = q[i-3] - q[i-4] +9
            d1 = q[i-2] - q[i-3] +9
            d2 = q[i-1] - q[i-2] +9
            d3 = q[i  ] - q[i-1] +9
            if memory[l][d0][d1][d2][d3] == -1:
                
                memory[l][d0][d1][d2][d3] = secret_number%10

maximum = 0
for i in tqdm(range(19)):
    for j in range(19):
        for k in range(19):
            for l in range(19):
                t = 0
                for ll in range(len(lines)):
                    if(memory[ll][i][j][k][l] != -1):
                        t += memory[ll][i][j][k][l]
                maximum = max(t, maximum)
print()
print(maximum)