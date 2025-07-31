import sys

N = int(sys.stdin.readline())
p = []
for _ in range(N):
    r, c = map(int, sys.stdin.readline().split())
    if not p:
        p.append(r)
    p.append(c)

dp = [[float('inf')] * (N+1) for _ in range(N+1)]
for i in range(1, N + 1):
    dp[i][i] = 0

for length in range(2, N+1):
    for i in range(1, N - length + 2):
        j = i + length - 1
        for mid in range(i, j):
            dp[i][j] = min(dp[i][j], dp[i][mid] + dp[mid+1][j] + p[i-1] * p[mid] * p[j])

print(dp[1][N])