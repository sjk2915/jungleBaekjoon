import sys
from collections import deque, defaultdict

n, m = list(map(int, sys.stdin.readline().split()))
nodes = list(range(1, n+1))
links = defaultdict(list)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    links[u].append(v)
    links[v].append(u)

visited = [False] * (len(nodes) + 1)
def bfs(node, links):
    global visited
    queue = deque([node])
    visited[node] = True
    while queue:
        current_node = queue.popleft()

        for next_node in links[current_node]:
            if not visited[next_node]:
                visited[next_node] = True
                queue.append(next_node)

node_linked = 0
for node in nodes:
    if visited[node] == False:
        bfs(node, links)
        node_linked += 1

print(node_linked)