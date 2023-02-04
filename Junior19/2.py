numlines = int(input())

final = ''
for i in range(numlines):
    thing = input()
    thing = thing.split(' ')
    final += f'{int(thing[0])*thing[1]}\n'
print(final)