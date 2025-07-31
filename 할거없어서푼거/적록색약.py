import sys
from collections import deque

N = int(sys.stdin.readline().strip())
image = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def normal_check():
    visited = [[False] * N for _ in range(N)]
    def _normal_bfs(row, col, color):
        queue = deque()

        visited[row][col] = True
        queue.append((row, col))
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < N and 0 <= nc < N \
                   and not visited[nr][nc] and image[nr][nc] == color:
                    visited[nr][nc] = True
                    queue.append((nr, nc))
    
    chunk = 0
    for i in range(N):  
        for j in range(N):
            if not visited[i][j]:
                chunk += 1
                _normal_bfs(i, j, image[i][j])

    return chunk

def color_weakness_check():
    visited = [[False] * N for _ in range(N)]
    def _color_weakness_bfs(row, col, color):
        queue = deque()

        visited[row][col] = True
        queue.append((row, col))
        while queue:
            r, c = queue.popleft()
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < N and 0 <= nc < N \
                   and not visited[nr][nc]:
                    if color == 'R' or color == 'G':
                        if image[nr][nc] == 'R' or image[nr][nc] == 'G':
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                    else:
                        if image[nr][nc] == color:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
    
    chunk = 0
    for i in range(N):  
        for j in range(N):
            if not visited[i][j]:
                chunk += 1
                _color_weakness_bfs(i, j, image[i][j])

    return chunk

answer = []
answer.append(normal_check())
answer.append(color_weakness_check())
print(*answer)