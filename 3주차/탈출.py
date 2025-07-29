import sys
from collections import deque

R, C = list(map(int, sys.stdin.readline().split()))
TWforest = [list(sys.stdin.readline().strip()) for _ in range(R)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs():
    # 홍수가 일어날 시간 구하기
    flooded = [[float('inf')] * C for _ in range(R)]
    queue = deque()
    for i in range(R):
        for j in range(C):
            if TWforest[i][j] == '*':
                flooded[i][j] = 0
                queue.append((i, j, 0))

    while queue:
        r, c, time = queue.popleft()
        for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < R and 0 <= nc < C and flooded[nr][nc] > time + 1 \
                   and (TWforest[nr][nc] == '.' or TWforest[nr][nc] == 'S'):
                    flooded[nr][nc] = time + 1
                    queue.append((nr, nc, time + 1))

    # 고슴도치가 움직이기
    visited = [[False] * C for _ in range(R)]
    queue = deque()
    for i in range(R):
        for j in range(C):
            if TWforest[i][j] == 'S':
                visited[i][j] = True
                queue.append((i, j, 0))

    while queue:
        r, c, time = queue.popleft()
        if TWforest[r][c] == 'D':
            return time
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] \
            and (TWforest[nr][nc] == '.' or TWforest[nr][nc] == 'D') \
            and flooded[nr][nc] > time + 1:
                visited[nr][nc] = True
                queue.append((nr, nc, time + 1))

answer = bfs()
print(answer if answer else 'KAKTUS')