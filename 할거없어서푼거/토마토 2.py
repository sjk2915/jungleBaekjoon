import sys
from collections import deque

M, N, H = map(int, sys.stdin.readline().split())
tomatos = [[list(map(int, sys.stdin.readline().split())) for _ in range(N)] for _ in range(H)]
DIR = [
    # dh, dr, dc
    # 앞쪽
    [0, 0, 1],
    # 뒤쪽
    [0, 0, -1],
    # 왼쪽
    [0, 1, 0],
    # 오른쪽
    [0, -1, 0],
    # 위쪽
    [1, 0, 0],
    # 아래쪽
    [-1, 0, 0],
]

def bfs(tomatos):
    max_days = 0

    # 큐에 토마토 넣기
    queue = deque()
    for h in range(H):
        for r in range(N):
            for c in range(M):
                if tomatos[h][r][c] == 1:
                    queue.append((h, r, c, 0))
    
    # 토마토 익히기 시뮬레이션
    while queue:
        h, r, c, days = queue.popleft()
        max_days = max(max_days, days)
        for dh, dr, dc in DIR:
            nh = h + dh
            nr = r + dr
            nc = c + dc
            if 0 <= nh < H and 0 <= nr < N and 0 <= nc < M \
               and tomatos[nh][nr][nc] == 0:
                tomatos[nh][nr][nc] = 1
                queue.append((nh, nr, nc, days + 1))
    
    # 토마토가 다 익었는지 체크
    for i in range(H):
        for j in range(N):
            for k in range(M):
                if tomatos[i][j][k] == 0:
                    return -1
    return max_days

print(bfs(tomatos))