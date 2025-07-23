import sys

T = int(sys.stdin.readline().strip())
max_n = 0
max_k = 0
testcases = []
for _ in range(T):
    n = int(sys.stdin.readline().strip())
    k = int(sys.stdin.readline().strip())
    max_n = max(max_n, n)
    max_k = max(max_k, k)
    testcases.append([n, k])

dp = [[0 for _ in range(max_k+1)] for _ in range(max_n+1)]
for i in range(max_k+1):
    dp[0][i] = i

for i in range(1, max_n+1):
    for j in range(1, max_k+1):
        dp[i][j] = sum(dp[i-1][:j+1])

for testcase in testcases:
    n, k = testcase
    print(dp[n][k])