playernum = int(input())
players = []
for i in range(playernum):
    in1 = int(input())
    in2 = int(input())
    players.append([in1, in2])
goldnum = 0
for j in players:
    j = j[0]*5 - j[1]*3
    if j > 40: goldnum += 1
if goldnum == playernum:
    goldnum = str(goldnum) + '+'
print(goldnum)