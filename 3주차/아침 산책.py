import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
is_indoor = list(map(int, sys.stdin.readline().strip()))
is_indoor.insert(0, 0)
edges = defaultdict(list)
for _ in range(N-1):
    u, v = map(int, sys.stdin.readline().split())
    edges[u].append(v)
    edges[v].append(u)

visited = [False] * (N+1)
def dfs(start):
    linked_indoor = 0
    stack = []
    visited[start] = True
    stack.append(start)
    while stack:
        node = stack.pop()
        for neighbor in edges[node]:
            if not visited[neighbor]:
                if is_indoor[neighbor]:
                    linked_indoor += 1
                else:
                    visited[neighbor] = True
                    stack.append(neighbor)
    return linked_indoor

total_path = 0
# 실내->실내 계산
for i in range(1, N+1):
    if is_indoor[i]:
        for node in edges[i]:
            if is_indoor[node]:
                total_path += 1

for i in range(1, N+1):
    # 방문하지 않은 실외노드에서 dfs 탐색
    if not visited[i] and not is_indoor[i]:
        linked_indoor = dfs(i)
        # 서브트리내에서 총 경로수는 연결된실내의 순열개수
        total_path += linked_indoor * (linked_indoor - 1)

print(total_path)