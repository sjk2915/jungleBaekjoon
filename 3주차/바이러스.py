import sys
from collections import deque, defaultdict

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())

computers = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    computers[u].append(v)
    computers[v].append(u)

def bfs(start):
    is_visit = [False] * (N+1)
    queue = deque()
    infect = 0
    is_visit[start] = True
    queue.append(start)
    while queue:
        node = queue.popleft()
        for next in computers[node]:
            if not is_visit[next]:
                infect += 1
                is_visit[next] = True
                queue.append(next)

    return infect

print(bfs(1))