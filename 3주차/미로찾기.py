import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[False] * (M) for _ in range(N)]
    queue = deque()

    visited[0][0] = True
    queue.append((0, 0, 1))

    while queue:
        r, c, cell_count = queue.popleft()
        if r == N-1 and c == M-1:
            return cell_count
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if (0 <= nr < N and 0 <= nc < M
               and maze[nr][nc] != 0
               and not visited[nr][nc]):
                visited[nr][nc] = True
                queue.append((nr, nc, cell_count + 1))

print(bfs())