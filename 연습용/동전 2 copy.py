import sys
from collections import defaultdict

N, K = list(map(int, sys.stdin.readline().split()))
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

# dfs = 시간초과 걍 얌전히 dp나 쓰기
dp = defaultdict(lambda: float('inf'))
coins.sort(reverse=True)
def dfs(value, idx):
    if dp[(value, idx)] != float('inf'):
        return dp[(value, idx)]
    for i in range(value // coins[idx], -1, -1):
        remain = value - (i * coins[idx])
        if remain == 0:
            dp[(value, idx)] = min(dp[(value, idx)], i)
        else:
            # 더이상 작은 코인이 없으면
            if idx == len(coins)-1:
                continue
            else:
                remain_used_coins = dfs(remain, idx+1)
                if remain_used_coins == float('inf'):
                    continue
                else:
                    dp[(value, idx)] = min(dp[(value, idx)], i + remain_used_coins)
    
    return dp[(value, idx)]

min_coins = dfs(K, 0)
print(min_coins if min_coins != float('inf') else -1)