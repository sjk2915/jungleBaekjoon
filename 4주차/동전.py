import sys

T = int(sys.stdin.readline().strip())
testcases = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    coins = list(map(int, sys.stdin.readline().split()))
    M = int(sys.stdin.readline().strip())
    testcases.append([N, M, coins])

for testcase in testcases:
    N, M, coins = testcase
    dp = [0] * (M+1)
    dp[0] = 1
    for i in range(N):
        for j in range(1, M+1):
            if j - coins[i] >= 0:
                dp[j] += dp[j - coins[i]]
    print(dp[M])