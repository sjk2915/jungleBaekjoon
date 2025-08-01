import sys

N, K = list(map(int, sys.stdin.readline().split()))
coins = [int(sys.stdin.readline().strip()) for _ in range(N)]

remain = K
count = 0

coins.reverse()
for coin in coins:
    if remain < coin:
        continue
    count += remain // coin
    remain %= coin
        
print(count)