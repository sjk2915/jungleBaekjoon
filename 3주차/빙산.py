import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
icebergs = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def melting_icebergs():
    to_melt = [[0] * M for _ in range(N)]

    for i in range(N):
        for j in range(M):
            # 해당 칸이 빙산이면
            if icebergs[i][j] > 0:
                # 상하좌우 체크후 바다면 녹일양 +1
                for k in range(4):
                    nr = i + dx[k]
                    nc = j + dy[k]
                    if 0 <= nr < N and 0 <= nc < M \
                       and icebergs[nr][nc] == 0:
                        to_melt[i][j] += 1
    
    # 탐색 완료 후 녹이기
    for i in range(N):
        for j in range(M):
            icebergs[i][j] = max(0, icebergs[i][j] - to_melt[i][j])

def check_icebergs():
    def _check_icebergs_bfs(row, col):
        queue = deque()

        visited[row][col] = True
        queue.append((row, col))
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < N and 0 <= nc < M \
                   and not visited[nr][nc]:
                    # 빙산일때만 처리
                    if icebergs[nr][nc] > 0:
                        visited[nr][nc] = True
                        queue.append((nr, nc))
    
    # 코드 시작
    chunk = 0
    visited = [[False] * M for _ in range(N)]
    for i in range(N):  
        for j in range(M):
            if icebergs[i][j] > 0 and not visited[i][j]:
                chunk += 1
                _check_icebergs_bfs(i, j)

    return chunk

year = 0
is_splited = False
cur_icebergs = check_icebergs()
prev_icebergs = cur_icebergs
while prev_icebergs != 0:
    year += 1
    melting_icebergs()
    cur_icebergs = check_icebergs()
    if cur_icebergs > prev_icebergs:
        is_splited = True
        break
    prev_icebergs = cur_icebergs

if not is_splited:
    year = 0

print(year)