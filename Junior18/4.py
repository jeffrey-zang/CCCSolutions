numthings = int(input())

lines = []

for i in range(numthings):
    o = input().split(' ')
    o = [int(x) for x in o]
    lines.append(o)
    

def checkGood(lines):
    currentBiggest = 0
    for line in lines:

        sortedline = sorted(line)
        if sortedline != line:
            return 'bad'

        # if line[-1] > currentBiggest:
        #     currentBiggest = line[-1]
        # else:
        #     return 'bad'

    return 'good'

print()
for i in range(4):
    good = checkGood(lines)

    if good:
        

    if i == 0:
        newlines = []
        for j in range(len(lines)): 
            thingy = []
            for k in range(len(lines)):
                thingy.append(lines[k][j])
            newlines.append(thingy)
        lines = newlines
        
        for j in lines:
            e = ''
            for k in j:
                e += f'{k} '
            print(e)