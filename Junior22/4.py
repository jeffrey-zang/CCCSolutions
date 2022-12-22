together = []
apart = []
groups = []

x = int(input())
for i in range(x):
    together.append(input())

y = int(input())
for i in range(y):
    apart.append(input())
    
g = int(input())
for i in range(g):
    groups.append(input())

for i in range(len(groups)):
    groups[i] = groups[i].split(' ')

for i in groups:
    for j in together:
        if j[0] in i and j[1] not in i:
            