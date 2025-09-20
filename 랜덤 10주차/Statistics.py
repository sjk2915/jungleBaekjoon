import sys

N = int(sys.stdin.readline().strip())
nums = []
for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))

to_delete = 0
announced_num = nums[0]
for num in nums:
    if num > announced_num:
        to_delete += num - announced_num
    else:
        announced_num = num

print(to_delete)