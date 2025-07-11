import sys  
n = (int)(sys.stdin.readline())
numsList = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for nums in numsList:
    print(nums[0]+nums[1])