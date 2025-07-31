import sys

N = int(sys.stdin.readline().strip())
dp = [0] * (N+1)
for i in range(N+1):
    if i == 1:
        dp[i] = 1
    elif i == 2:
        dp[i] = 2
    elif i >= 3:
        dp[i] = (dp[i-1] + dp[i-2]) % 15746
print(dp[N])