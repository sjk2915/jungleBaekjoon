import sys
from collections import defaultdict, deque

N, K = list(map(int, sys.stdin.readline().split()))
coins = []
for _ in range(N):
    coins.append(int(sys.stdin.readline().strip()))

def solve_using_dp():
    dp = [float('inf')] * (K + 1)
    dp[0] = 0

    coins.sort() 
    for i in range(1, K + 1):
        for coin in coins:
            if i - coin >= 0 and dp[i - coin] != float('inf'):
                dp[i] = min(dp[i], dp[i - coin] + 1)
    return dp[K] if dp[K] != float('inf') else -1

# dfs = 시간초과 이걸로는 못푸는듯
def solve_using_dfs():
    dp = defaultdict(lambda: float('inf'))
    coins.sort(reverse=True)
    def _dfs(value, idx):
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
                    remain_used_coins = _dfs(remain, idx+1)
                    if remain_used_coins == float('inf'):
                        continue
                    else:
                        dp[(value, idx)] = min(dp[(value, idx)], i + remain_used_coins)
        
        return dp[(value, idx)]
    
    min_coins = _dfs(K, 0)
    return min_coins if min_coins != float('inf') else -1

def solve_using_bfs():
    counted = [False] * (K+1)
    def _bfs():
        queue = deque()
        counted[0] = True
        queue.append((0, 0))
        while queue:
            cur, count = queue.popleft()
            if cur == K:
                return count
            for coin in coins:
                next = cur + coin
                if next <= K and not counted[next]:
                    counted[next] = True
                    queue.append((next, count + 1))

    min_coins = _bfs()
    return min_coins if min_coins else -1

print(solve_using_bfs())