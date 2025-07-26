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

costs = [float('inf')] * (N+1)
def Dijkstra(start):
    queue = []

    costs[start] = 0
    heapq.heappush(queue, (0, start))
    while queue:
        cost, cur = heapq.heappop(queue)
        if cost > costs[cur]: continue
        for next, weight in graph[cur]:
            if cost + weight < costs[next]:
                costs[next] = cost + weight
                heapq.heappush(queue, (cost + weight, next))

Dijkstra(start)
print(costs[end])