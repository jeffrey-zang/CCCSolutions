a3 = int(input())
a2 = int(input())
a1 = int(input())

b3 = int(input())
b2 = int(input())
b1 = int(input())

apple = a3*3 + a2*2 + a1*1
ban = b3*3 + b2*2 + b1*1

if apple > ban: print('A')
if ban > apple: print('B')
if apple == ban: print('T')