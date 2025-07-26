import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
cheeses = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def melting_cheeses():
    visited = [[False] * M for _ in range(N)]
    to_melt = [[0] * M for _ in range(N)]
    queue = deque()

    visited[0][0] = True
    queue.append((0, 0))
    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < M \
                and not visited[nr][nc]:
                if cheeses[nr][nc] == 1:
                    to_melt[nr][nc] += 1
                else:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    
    # 탐색 완료 후 녹이기
    for i in range(N):
        for j in range(M):
            # 2번 이상탐색되면 (2면이 외부에서 시작한 bfs에 의해 탐색되면)
            if to_melt[i][j] >= 2:
                cheeses[i][j] = 0

def is_cheeses():
    for i in range(N):  
        for j in range(M):
            if cheeses[i][j] == 1:
                return True
    return False

hour = 0
while is_cheeses():
    hour += 1
    melting_cheeses()

print(hour)