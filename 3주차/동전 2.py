import sys

N, K = list(map(int, sys.stdin.readline().split()))
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

dp = [float('inf')] * (K + 1)
dp[0] = 0

coins.sort() 
for i in range(1, K + 1):
    for coin in coins:
        if i - coin >= 0 and dp[i - coin] != float('inf'):
            dp[i] = min(dp[i], dp[i - coin] + 1)

print(dp[K] if dp[K] != float('inf') else -1)