peoples = int(input())
people = []
for i in range(peoples*2):
    put = input()
    print(put)
    if not put.isnumeric():
        people.append([put])
    if put.isnumeric():
        people[-1].append(put)
print(people)