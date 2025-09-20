import sys
from collections import defaultdict

sys.setrecursionlimit(10**5) 

N, M, R = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    graph[v].append(u)

for i in range(1, N + 1):
    graph[i].sort(reverse=True)

def dfs(start):
    visited = [False] * (N+1)
    node_depth = [-1] * (N+1)
    def _dfs_recursive(node, depth):
        visited[node] = True
        node_depth[node] = depth
        for next in graph[node]:
            if not visited[next]:
                _dfs_recursive(next, depth+1)
    _dfs_recursive(start, 0)
    return node_depth

for answer in dfs(R)[1:]:
    print(answer)