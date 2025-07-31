import sys
from collections import defaultdict
import heapq

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = defaultdict(list)
for _ in range(M):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    graph[u].append((v, w))
start, end = list(map(int, sys.stdin.readline().split()))

costs = [float('inf') for _ in range(N)]
def dijkstra(start):
    queue = []
    costs[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        total_cost, cur = heapq.heappop(queue)
        for next, cost in graph[cur]:
            if costs[next] > total_cost + cost:
                costs[next] = total_cost + cost
                heapq.heappush(queue, (total_cost + cost, next))