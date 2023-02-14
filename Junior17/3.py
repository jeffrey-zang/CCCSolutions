coord1 = input().split(' ')
coord2 = input().split(' ')
t = int(input())

coord1 = [int(x) for x in coord1]
coord2 = [int(x) for x in coord2]

changey = abs(coord1[1] - coord2[1])
changex = abs(coord1[0] - coord2[0])

distance = changey+changex

if distance % 2 == t % 2 and distance <= t:
    print('Y')
else:
    print('N')