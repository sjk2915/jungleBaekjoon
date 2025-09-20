import sys
from collections import deque

N, M, V = list(map(int, sys.stdin.readline().split()))
graph = {}
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    dfs_path = []
    visited = [False] * (N+1)
    def _dfs_recursive(node):
        visited[node] = True
        dfs_path.append(node)
        for next in sorted(graph[node]):
            if not visited[next]:
                _dfs_recursive(next)
    _dfs_recursive(start)
    return dfs_path

def bfs(start):
    bfs_path = []
    visited = [False] * (N+1)
    queue = deque()
    queue.append(start)
    visited[start] = True
    while queue:
        node = queue.popleft()
        for next in sorted(graph[node]):
            if not visited[next]:
                queue.append(next)
                visited[next] = True
                bfs_path.append(next)

dfs_path = dfs(V)
bfs_path = bfs(V)
print(*dfs_path)
print(*bfs_path)