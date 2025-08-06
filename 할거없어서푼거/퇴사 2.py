import sys

N = int(sys.stdin.readline().strip())
counsels = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [0] * (N+2)
max_pay = 0
for day, (time, pay) in enumerate(counsels, start=1):
    max_pay = max(max_pay, dp[day])
    if day+time <= N+1:
        dp[day+time] = max(dp[day+time], max_pay + pay)
print(max(dp))