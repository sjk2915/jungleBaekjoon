import sys
import math

N, M = list(map(int, sys.stdin.readline().split()))
small_rocks = set(int(sys.stdin.readline().strip()) for _ in range(M))

max_speed = int(math.sqrt(2 * N) + 1)
dp = [[float('inf')] * (max_speed+1) for _ in range(N+1)]
dp[1][0] = 0
for i in range(1, N+1):
    if i in small_rocks: continue
    for j in range(max_speed+1):
        if dp[i][j] == float('inf'): continue

        # 감속 점프
        next = i+j-1
        if j-1 > 0 and next <= N and next not in small_rocks:
            dp[next][j-1] = min(dp[next][j-1], dp[i][j] + 1)
        # 점프
        next = i+j
        if j > 0 and next <= N and next not in small_rocks:
            dp[next][j] = min(dp[next][j], dp[i][j] + 1)
        # 가속 점프
        next = i+j+1
        if j+1 > 0 and next <= N and next not in small_rocks:
            dp[next][j+1] = min(dp[next][j+1], dp[i][j] + 1)

result = min(dp[N])
print(result if result != float('inf') else -1)