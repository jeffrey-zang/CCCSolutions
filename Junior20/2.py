target = int(input())
total = int(input())
perday = int(input())

days = 0
caninfectsomeone = total

while target >= total:
    # print(total, caninfectsomeone)
    old = total
    total += caninfectsomeone*perday
    caninfectsomeone = total - old
    days += 1
print(days)