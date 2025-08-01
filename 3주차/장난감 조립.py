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

class Parts:
    def __init__(self):
        self.materials = defaultdict(int)

    def add_material(self, material_id, count: int = 1):
        self.materials[material_id] += count

    def add_parts(self, parts: 'Parts', req_count: int = 1):
        for material_id, count in parts.get_materials():
            self.materials[material_id] += count * req_count

    def get_materials(self):
        return self.materials.items()

parts = [Parts() for _ in range(N+1)]
for node in range(1, N+1):
    if in_degree[node] == 0:
        parts[node].add_material(node)

for node in topological_sort():
    for next_node, req_count in graph[node]:
        parts[next_node].add_parts(parts[node], req_count)

for item in sorted(parts[N].get_materials()):
    print(*item)