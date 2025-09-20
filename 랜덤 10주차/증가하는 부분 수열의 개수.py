import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
MOD_NUM = 998244353

dp = [1] * N
for i in range(1, N):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = (dp[i] + dp[j]) % MOD_NUM
print(*dp)