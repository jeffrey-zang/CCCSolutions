hour = 12
minute1 = 0
minute2 = 0
count = 0

times = int(input())
days = times // 3600
minsleft = times % 3600

if times < 3600:
    minsleft = times
count += 155 * days

for i in range(minsleft):

    minute2 += 1
    if minute2 == 10:
        minute1 += 1
        minute2 = 0
    if minute1 == 6:
        minute1 = 0
        minute2 = 0
        hour += 1
        if hour == 13:
            hour = 1

    if hour > 9:
        newhour = list(str(hour))
        newhour = [int(x) for x in newhour]
        diff1 = newhour[0] - newhour[1]
        diff2 = newhour[1] - minute1
        diff3 = minute1 - minute2
        if diff1 == diff2 == diff3:
            count += 1

    else:
        diff1 = hour-minute1
        diff2 = minute1-minute2
        if diff1 == diff2:
            count += 1

print(count)