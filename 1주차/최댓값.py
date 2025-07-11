import sys
nums =[(int)(sys.stdin.readline()) for i in range(9)]

maxValue = max(nums)
idx = nums.index(maxValue)

print(maxValue)
print(idx+1)