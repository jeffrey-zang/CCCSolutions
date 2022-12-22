thing = input()
string = input()

shifts = [list(string)]

for i in range(len(list(string))):
    string = list(string)
    string.append(string[0])
    string.pop(0)
    shifts.append(string)
    string = ''.join((string))
shifts.pop(-1)

isin = False
for i in range(len(list(thing))):
    for j in shifts:
        if j == list(thing[i:i+len(shifts)]):
            isin = True
print('yes' if isin else 'no')
            