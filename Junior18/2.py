amount = int(input())

day1 = list(input())
day2 = list(input())

things = 0
for i in range(amount):
    if day1[i] == day2[i] == 'C':
        things += 1

print(things)