import sys

N, M = list(map(int, sys.stdin.readline().split()))
mars = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[float('-inf')] * M for _ in range(N)]
dp[0][0] = mars[0][0]
for i in range(N):
    if i == 0:
        # 왼쪽에서 오는 루프
        for j in range(M):
            if 0 <= j-1 < M:
                dp[i][j] = dp[i][j-1] + mars[i][j]
    else:
        # 위에서 오는 경우를 tmp_dp에 저장
        tmp_dp = [dp[i-1][j] + mars[i][j] for j in range(M)]

        # 왼쪽에서 오는 루프
        tmp_left_dp = tmp_dp[:]
        for j in range(M):
            if 0 <= j-1 < M:
                tmp_left_dp[j] = max(tmp_left_dp[j], tmp_left_dp[j-1] + mars[i][j])
        # 오른쪽에서 오는 루프
        tmp_right_dp = tmp_dp[:]
        for j in range(M-1, -1, -1):
            if 0 <= j+1 < M:
                tmp_right_dp[j] = max(tmp_right_dp[j], tmp_right_dp[j+1] + mars[i][j])

        for j in range(M):
            dp[i][j] = max(tmp_left_dp[j], tmp_right_dp[j])
        
print(dp[N-1][M-1])