import sys

N = int(sys.stdin.readline().strip())
nums = []
for _ in range(N):
    nums.append(list(map(int, sys.stdin.readline().split())))

max_dp = [[0] * 3 for _ in range(N)]
min_dp = [[0] * 3 for _ in range(N)]
max_dp[0] = nums[0]
min_dp[0] = nums[0]
for i in range(1, N):
    max_dp[i][0] = nums[i][0] + max(max_dp[i-1][0], max_dp[i-1][1])
    max_dp[i][1] = nums[i][1] + max(max_dp[i-1][0], max_dp[i-1][1], max_dp[i-1][2])
    max_dp[i][2] = nums[i][2] + max(max_dp[i-1][1], max_dp[i-1][2])

    min_dp[i][0] = nums[i][0] + min(min_dp[i-1][0], min_dp[i-1][1])
    min_dp[i][1] = nums[i][1] + min(min_dp[i-1][0], min_dp[i-1][1], min_dp[i-1][2])
    min_dp[i][2] = nums[i][2] + min(min_dp[i-1][1], min_dp[i-1][2])

print(f'{max(max_dp[N-1])} {min(min_dp[N-1])}')