rows = int(input())
columns = int(input())

coords = {}

for i in range(rows):
    row = str(input()).split(' ')
    coords[row[0]] = list(row[1::])

positions = []
for i in coords:
    for j in coords[i]:
        positions.append([int(i), int(j)])

print(positions)