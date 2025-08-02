import sys
import heapq

N, K = list(map(int, sys.stdin.readline().split()))
gems = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
knapsacks = [int(sys.stdin.readline().strip()) for _ in range(K)]

gems.sort(key=lambda x: -x[0])
knapsacks.sort()
queue = []

total_value = 0
for knapsack in knapsacks:
    while gems and gems[-1][0] <= knapsack:
        _, v = gems.pop()
        heapq.heappush(queue, -v)
    if queue:
        total_value += -heapq.heappop(queue)

print(total_value)