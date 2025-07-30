import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
campus = [list(sys.stdin.readline().strip()) for _ in range(N)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
def bfs():
    visited = [[False] * M for _ in range(N)]
    queue = deque()
    meet_count = 0

    for i in range(N):
        for j in range(M):
            if campus[i][j] == 'I':
                visited[i][j] = True
                queue.append((i, j))

    while queue:
        r, c = queue.popleft()
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if (0 <= nr < N and 0 <= nc < M
                and campus[nr][nc] != 'X'
                and not visited[nr][nc]):
                if campus[nr][nc] == 'P':
                    meet_count += 1
                
                visited[nr][nc] = True
                queue.append((nr, nc))
                
    return meet_count
    
answer = bfs()
print(answer if answer > 0 else 'TT')