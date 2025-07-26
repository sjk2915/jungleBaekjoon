import sys
from collections import deque, defaultdict

N, M, K, X = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)

city_at_K = []
def bfs(start):
    visited = [False] * (N+1)
    queue = deque()

    visited[start] = True
    queue.append((start, 0))
    while queue:
        cur, dist = queue.popleft()
        if dist == K:
            city_at_K.append(cur)
        for next in graph[cur]:
            if not visited[next]:
                visited[next] = True
                queue.append((next, dist + 1))

bfs(X)
city_at_K.sort()
if city_at_K:
    for item in city_at_K:
        print(item)
else:
    print(-1)