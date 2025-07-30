import sys
from collections import defaultdict
import heapq

N = int(sys.stdin.readline().strip())
graph = defaultdict(list)
in_degree = [0] * (N+1)
for i in range(1, N+1):
    node = list(map(int, sys.stdin.readline().strip()))
    for j in range(1, N+1):
        if node[j-1]:
            graph[i].append(j)
            in_degree[j] += 1

def topological_sort():
    queue = []
    for i in range(1, N + 1):
        if in_degree[i] == 0:
            heapq.heappush(queue, i)
    result = [-1] * (N+1)
    num = 1
    while queue:
        cur = heapq.heappop(queue)
        result[cur] = num
        num += 1
        for dest in graph[cur]:
            in_degree[dest] -= 1
            if in_degree[dest] == 0:
                heapq.heappush(queue, dest)

    if -1 in result[1:]:
        return []
    else:
        return result[1:]

answer = topological_sort()
if answer:
    print(*answer)
else:
    print(-1)