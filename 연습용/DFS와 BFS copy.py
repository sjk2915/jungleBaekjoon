import sys
from collections import deque, defaultdict

N, M, V = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

def dfs(start):
    visited = [False] * (N+1)
    dfs_path = []
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
    bfs_path.append(start)
    visited[start] = True
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for next in sorted(graph[cur]):
            if not visited[next]:
                bfs_path.append(next)
                visited[next] = True
                queue.append(next)
    return bfs_path

dfs_path = dfs(V)
bfs_path = bfs(V)
print(*dfs_path)
print(*bfs_path)