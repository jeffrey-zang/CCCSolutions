ori = list(input())
final = []
numbers = []
lastcharacter = 'e'
ori.append('e')
bruh = 0

for i in ori:

    if i.isalpha() and lastcharacter.isnumeric():
        #print(f'did this 4 for {i}')

        # if ori.index(i)+1 == len(ori):
        #     numbers.append(i) 
            
        final.append(''.join(numbers))
        thing = ''
        if final[1] == '+': thing = 'tighten'
        if final[1] == '-': thing = 'loosen'
        
        print(f'{final[0]} {thing} {final[2]}')
        bruh += 1
        final = []
        numbers = []

    if i.isalpha():
        #print(f'did this for {i}')
        final.append(i)
    
    if i in ['+', '-']:
        #print(f'did this 2 for {i}')
        final = [''.join(final)]
        final.append(i)
    
    if i.isnumeric():
        #print(f'did this 3 for {i}')
        numbers.append(i)

    lastcharacter = i

    
# e = ['1', '2', '3']
# #print(''.join(e[0:-1]))
# token = ''.join(token[0:-1])  