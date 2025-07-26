import sys
from collections import deque, defaultdict

N, M, K, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)

def bfs(start):
    visited = [False] * (N+1)
    queue = deque()

    visited[start] = True
    queue.append((start, 0))
    while queue:
        cur, dist = queue.popleft()
        for next in graph(cur):
            visited[next] = True
            queue.append((next, dist + 1))

print(bfs())