import sys
from collections import defaultdict
import heapq

N = int(sys.stdin.readline().strip())
graph = defaultdict(list)
out_degree = [0] * (N+1)
for i in range(1, N+1):
    node = list(map(int, sys.stdin.readline().strip()))
    for j in range(1, N+1):
        if node[j-1]:
            graph[j].append(i)
            out_degree[i] += 1

def topological_sort():
    max_heap = []
    for i in range(1, N + 1):
        if out_degree[i] == 0:
            heapq.heappush(max_heap, -i)
    result = [-1] * (N+1)
    num = N
    while max_heap:
        cur = -heapq.heappop(max_heap)
        result[cur] = num
        num -= 1
        for dest in graph[cur]:
            out_degree[dest] -= 1
            if out_degree[dest] == 0:
                heapq.heappush(max_heap, -dest)

    if -1 in result[1:]:
        return []
    else:
        return result[1:]

answer = topological_sort()
if answer:
    print(*answer)
else:
    print(-1)