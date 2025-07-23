import sys
from collections import deque, defaultdict

V, E = list(map(int, sys.stdin.readline().split()))
K = int(sys.stdin.readline().strip())
vertexs = defaultdict(list)
for _ in range(E):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    vertexs[u].append((v, w))

min_dist_list = [float('inf')] * (V + 1)
def bfs(start):
    min_dist_list[start] = 0
    queue = deque([(start, 0)])
    while queue:
        cur, dist = queue.popleft()
        if cur in vertexs:
            for v, w in vertexs[cur]:
                if min_dist_list[v] > dist + w:
                    min_dist_list[v] = dist + w
                    queue.append((v, dist + w))

bfs(K)
print(min_dist_list)