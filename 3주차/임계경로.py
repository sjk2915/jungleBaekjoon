import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = defaultdict(list)
reverse_graph = defaultdict(list)
in_degree = [0] * (N+1)
for _ in range(M):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    graph[u].append((v, w))
    reverse_graph[v].append((u, w))
    in_degree[v] += 1
start, end = list(map(int, sys.stdin.readline().split()))

max_time = [0] * (N+1)
max_route = set()
def topological_sort():
    # 정방향 탐색
    queue = deque()
    queue.append(start)
    while queue:
        cur = queue.popleft()
        for dest, time in graph[cur]:
            in_degree[dest] -= 1
            if max_time[dest] < max_time[cur] + time:
                max_time[dest] = max_time[cur] + time

            if in_degree[dest] == 0:
                queue.append(dest)

    # 역방향 탐색
    visited = [False] * (N+1)
    queue = deque()
    visited[end] = True
    queue.append(end)
    while queue:
        cur = queue.popleft()
        for dest, time in reverse_graph[cur]:
            if max_time[dest] + time == max_time[cur]:
                max_route.add((dest, cur))
                if not visited[dest]:
                    visited[dest] = True
                    queue.append(dest)

topological_sort()
print(max_time[end])
print(len(max_route))