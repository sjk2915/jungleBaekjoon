import sys
from collections import deque, defaultdict

N, M, V = list(map(int, sys.stdin.readline().split()))
nodes = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    nodes[u].append(v)
    nodes[v].append(u)

dfs_path = []
def dfs(start):
    visited = [False] * (N+1)
    stack = []
    stack.append(start)
    while stack:
        cur = stack.pop()
        if not visited[cur]:
            dfs_path.append(cur)
            visited[cur] = True
            for next in sorted(nodes[cur], reverse=True):
                stack.append(next)

bfs_path = []
def bfs(start):
    visited = [False] * (N+1)
    bfs_path.append(start)
    visited[start] = True
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        for next in sorted(nodes[cur]):
            if not visited[next]:
                bfs_path.append(next)
                visited[next] = True
                queue.append(next)

dfs(V)
print(*dfs_path)
bfs(V)
print(*bfs_path)