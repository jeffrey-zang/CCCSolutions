distances = input().split(' ')

for i in range(5):

    line = ''

    for j in range(5):
        
        if j == i: 
            line += '0 '
        else:
            thingy = []
            sum = 0

            if j < i:
                thingy = distances[j:i]
            elif j > i:
                thingy = distances[i:j]

            for k in thingy:
                sum += int(k)
            line += f'{sum} '

    print(line)