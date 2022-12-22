amount = int(input())

x = []
y = []

for i in range(amount):
    e = input()
    x.append(int(e.split(',')[0]))
    y.append(int(e.split(',')[1]))

x.sort()
y.sort()
print(f'{x[0]-1},{y[0]-1}')
print(f'{x[-1]+1},{y[-1]+1}')