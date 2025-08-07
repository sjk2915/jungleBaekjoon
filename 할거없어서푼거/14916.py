import sys

N = int(sys.stdin.readline().strip())
coins = [2, 5]

dp = [float('inf')] * (N + 1)
dp[0] = 0

coins.sort() 
for i in range(1, N + 1):
    for coin in coins:
        if i - coin >= 0 and dp[i - coin] != float('inf'):
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[N] if dp[N] != float('inf') else -1)