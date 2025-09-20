import sys

N = int(sys.stdin.readline().strip())
triangle = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = triangle[0][0]
for i in range(1, N):
    for j in range(i+1):
        left = 0
        right = 0
        if j-1 >= 0: left = dp[i-1][j-1]
        if j <= i-1: right = dp[i-1][j]
        dp[i][j] = triangle[i][j] + max(left, right)
print(max(dp[N-1]))