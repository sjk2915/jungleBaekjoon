import sys
from collections import deque

M, N = map(int, sys.stdin.readline().split())
tomatos = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def bfs(tomatos):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    max_days = 0

    queue = deque()
    for r in range(N):
        for c in range(M):
            if tomatos[r][c] == 1:
                queue.append((r, c, 0))

    while queue:
        r, c, days = queue.popleft()
        max_days = max(max_days, days)
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]

            if 0 <= nr < N and 0 <= nc < M and tomatos[nr][nc] == 0:
                tomatos[nr][nc] = 1
                queue.append((nr, nc, days + 1))

    if check_tomatos(tomatos):
        return max_days
    else:
        return -1

def check_tomatos(tomatos):
    for i in range(N):
        for j in range(M):
            if tomatos[i][j] == 0:
               return False
    return True

print(bfs(tomatos))