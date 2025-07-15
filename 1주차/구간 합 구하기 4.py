import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))

prefix_sum = [0] * (n + 1)
current_sum = 0
for i in range(n):
    current_sum += nums[i]
    prefix_sum[i+1] = current_sum

cases = []
for _ in range(m):
    cases.append(list(map(int, sys.stdin.readline().split())))

for case in cases:
    answer = prefix_sum[case[1]] - prefix_sum[case[0] - 1]
    print(answer)