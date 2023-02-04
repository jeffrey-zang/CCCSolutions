numlines = int(input())

final = ''
for i in range(numlines):
    line = input()
    line = list(line)
    
    chars = []
    for i in line:
        if i not in chars:
            chars.append(i)
    
    linefinal = ''
    for j in chars:
        numchars = line.count(j)
        linefinal += f'{numchars} {j} '
    final += linefinal + '\n'

    
print(final)