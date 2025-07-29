import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

graph = defaultdict(list)
in_degree = [0] * (N+1)
for _ in range(M):
    x, y, k = list(map(int, sys.stdin.readline().split()))
    graph[y].append((x, k))
    in_degree[x] += 1

def topological_sort():
    def _dfs(node):
        for dest, _ in graph[node]:
            if not visited[dest]:
                visited[dest] = True
                _dfs(dest)
        stack.append(node)

    stack = []
    visited = [False] * (N+1)
    for i in range(1, N+1):
        if not visited[i]:
            visited[i] = True
            _dfs(i)

    return list(reversed(stack))

materials = defaultdict(lambda: defaultdict(int))
for node in range(1, N+1):
    if in_degree[node] == 0:
        # 기본노드 재료는 자기자신
        materials[node][node] += 1

for node in topological_sort():
    for next_node, req_count in graph[node]:
        for material, count in materials[node].items():
                materials[next_node][material] += count * req_count

for item in sorted(materials[N].items()):
    print(*item)