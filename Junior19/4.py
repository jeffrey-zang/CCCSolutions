flips = input()
flips = list(flips)

if flips.count('V') % 2 == 0 and flips.count('H') % 2 == 0 and flips.count('V') == flips.count('H'): 
    print('1 2\n3 4')

else: 
    row1 = ['1', '2']
    row2 = ['3', '4']

    for i in flips:
        if i == 'H':
            save = row1
            row1 = row2
            row2 = save
        if i == 'V':
            row1 = row1[::-1]
            row2 = row2[::-1]

    print(f'{row1[0]} {row1[1]}\n{row2[0]} {row2[1]}')
