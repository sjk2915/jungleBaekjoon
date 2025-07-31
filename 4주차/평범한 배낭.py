import sys

N, K = list(map(int, sys.stdin.readline().split()))
goods = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [[0] * (K+1) for _ in range(N+1)]
for i in range(1, N+1):
    W, V = goods[i-1]
    for j in range(1, K+1):
        # 못넣는 경우
        if j < W:
            dp[i][j] = dp[i-1][j]
        # 안넣는 경우 : dp[i-1][j]
        # 다른걸 빼던가 해서 넣는 경우 : V + dp[i-1][j-W]
        else:
            dp[i][j] = max(dp[i-1][j], V + dp[i-1][j-W])

print(dp[N][K])