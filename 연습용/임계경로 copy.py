import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = defaultdict(list)
in_degree = [0] * (N+1)
for _ in range(M):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    graph[u].append((v, w))
    in_degree[v] += 1
start, end = list(map(int, sys.stdin.readline().split()))

# max_route 메모리 초과 역방향 연산으로 선별 필요
max_time = [0] * (N+1)
max_route = [set() for _ in range(N+1)]
def topological_sort():
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for dest, time in graph[cur]:
            in_degree[dest] -= 1
            if max_time[dest] < max_time[cur] + time:
                max_time[dest] = max_time[cur] + time
                max_route[dest] = set.union(max_route[cur], [(cur, dest)])
            elif max_time[dest] == max_time[cur] + time:
                max_route[dest] = set.union(max_route[dest], max_route[cur], [(cur, dest)])
            if in_degree[dest] == 0:
                queue.append(dest)

topological_sort()
print(max_time[end])
print(len(max_route[end]))