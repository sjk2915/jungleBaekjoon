import sys

N = int(sys.stdin.readline().strip())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[0] * N for _ in range(N)]
dp[0][0] = 1
for i in range(N):
    for j in range(N):
        if i == N - 1 and j == N - 1:
            continue
        cur_num = board[i][j]
        # 오른쪽
        if j+cur_num < N:
            dp[i][j+cur_num] += dp[i][j]
        # 아래쪽
        if i+cur_num < N:
            dp[i+cur_num][j] += dp[i][j]

print(dp[N-1][N-1])