import sys

N = int(sys.stdin.readline().strip())
dp = [0] * (N+1)
for i in range(N+1):
    if i == 0:
        dp[i] = 0
    elif i == 1:
        dp[i] = 1
    elif i >= 2:
        dp[i] = dp[i-1] + dp[i-2]
print(dp[N])