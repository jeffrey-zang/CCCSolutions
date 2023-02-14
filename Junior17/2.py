n = int(input())
k = int(input())

sum = n

for i in range(k):
    n *= 10
    sum += n
print(sum)