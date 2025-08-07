import sys
import math

N, M = list(map(int, sys.stdin.readline().split()))
small_rocks = set(int(sys.stdin.readline().strip()) for _ in range(M))

max_speed = int(math.sqrt(2 * N) + 1)
dp = [[float('inf')] * (max_speed+1) for _ in range(N+1)]
dp[1][0] = 0
for cur in range(1, N):
    if cur in small_rocks: continue
    for speed in range(max_speed+1):
        if dp[cur][speed] == float('inf'): continue

        # 감속 점프
        next = cur+speed-1
        if speed-1 > 0 and next <= N and next not in small_rocks:
            dp[next][speed-1] = min(dp[next][speed-1], dp[cur][speed] + 1)
        # 점프
        next = cur+speed
        if speed > 0 and next <= N and next not in small_rocks:
            dp[next][speed] = min(dp[next][speed], dp[cur][speed] + 1)
        # 가속 점프
        next = cur+speed+1
        if speed+1 > 0 and next <= N and next not in small_rocks:
            dp[next][speed+1] = min(dp[next][speed+1], dp[cur][speed] + 1)

result = min(dp[N])
print(result if result != float('inf') else -1)