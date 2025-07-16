import sys
from collections import deque, defaultdict

n, m = list(map(int, sys.stdin.readline().split()))
nodes = list(range(1, n+1))
links = defaultdict(list)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    links[u].append(v)
    links[v].append(u)

def bfs(node, links):
    kevin_bacon = 0
    visited = [False] * (len(nodes) + 1)
    visited[node] = True
    queue = deque([(node, 0)])
    while queue:
        current_node, dist = queue.popleft()
        kevin_bacon += dist
        for next_node in links[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append((next_node, dist + 1))

    return kevin_bacon

bacons = [float('inf')] * (len(nodes) + 1)
for node in nodes:
    bacons[node] = bfs(node, links)

print(bacons.index(min(bacons)))