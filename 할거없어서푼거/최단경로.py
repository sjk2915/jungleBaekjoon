import sys
from collections import defaultdict
import heapq

V, E = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline().strip())
vertexs = defaultdict(list)
for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    vertexs[u].append((v, w))

min_dist_list = [float('inf')] * (V + 1)
def dijkstra(start):
    min_dist_list[start] = 0
    queue = [(0, start)]
    while queue:
        total_dist, cur = heapq.heappop(queue)
        if total_dist >= min_dist_list[cur]: continue
        for next, dist in vertexs[cur]:
            if min_dist_list[next] > total_dist + dist:
                min_dist_list[next] = total_dist + dist
                heapq.heappush(queue, (total_dist + dist, next))

dijkstra(K)
for answer in min_dist_list[1:]:
    print(answer if answer != float('inf') else 'INF')