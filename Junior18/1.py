nums = []

for i in range(4):
    nums.append(int(input()))

if nums[0] in [8, 9] and nums[3] in [8, 9] and nums[1] == nums[2]:
    print('ignore')
else:
    print('answer')