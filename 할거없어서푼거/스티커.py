import sys

T = int(sys.stdin.readline().strip())
testcases = []
for i in range(T):
    N = int(sys.stdin.readline().strip())
    sticker = [list(map(int, sys.stdin.readline().split())) for _ in range(2)]
    testcases.append((N, sticker))

for testcase in testcases:
    N, sticker = testcase

    dp = [[0] * 3 for _ in range(N)]
    # dp[i][0] = 안뗀경우
    dp[0][0] = 0
    # dp[i][1] = 위를 뗀 경우
    dp[0][1] = sticker[0][0]
    # dp[i][2] = 아래를 뗀 경우
    dp[0][2] = sticker[1][0]

    for i in range(1, N):
        dp[i][0] = max(dp[i-1][0], dp[i-1][1], dp[i-1][2])
        dp[i][1] = sticker[0][i] + max(dp[i-1][0], dp[i-1][2])
        dp[i][2] = sticker[1][i] + max(dp[i-1][0], dp[i-1][1])

    print(max(dp[N-1]))