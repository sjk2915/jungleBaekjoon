import sys
import heapq
from collections import defaultdict

N, M, X = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(M):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    graph[u].append((v, w))

def Dijkstra(start, end):
    min_costs = [float('inf')] * (N+1)

    min_costs[start] = 0
    queue = [(0, start)]
    while queue:
        cur_cost, cur = heapq.heappop(queue)
        if cur_cost > min_costs[cur]: continue
        for next, cost in graph[cur]:
            if cur_cost + cost < min_costs[next]:
                min_costs[next] = cur_cost + cost
                heapq.heappush(queue, (cur_cost + cost, next))
                
    return min_costs[end]

max_time = 0
for i in range(1, N+1):
    max_time = max(max_time, Dijkstra(i, X) + Dijkstra(X, i))
print(max_time)