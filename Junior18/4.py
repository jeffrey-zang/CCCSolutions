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
            print('bad')
            return

        if line[-1] > currentBiggest:
            currentBiggest = line[-1]
        else:
            print('bad')
            return

    print('good')

def rotate(lines):

    if numthings % 2 == 0:
        pass

    else:
        newlist = []
        for i in range(len(lines)):
            newlist += [[0]*numthings]

        newlist[int(numthings/2)][int(numthings/2)] = lines[int(numthings/2)][int(numthings/2)]

        for line in range(len(lines)):
            
            for character in lines[line]:
                break
        print(newlist)

rotate(lines)