import sys
from collections import deque

def bfs(N, M, start_x, start_y, board, result_board):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    visited = [[False] * M for _ in range(N)]
    queue = deque([(start_x, start_y, 0)])
    result_board[start_x][start_y] = 0
    visited[start_x][start_y] = True
    
    while queue:
        x, y, dist = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
        
            if (0 <= nx < N and 0 <= ny < M
                and board[nx][ny] == 1
                and not visited[nx][ny]):

                visited[nx][ny] = True
                result_board[nx][ny] = dist + 1
                queue.append((nx, ny, dist + 1))

n, m = map(int, sys.stdin.readline().split())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
result_board = [[-1] * m for _ in range(n)]
start_x, start_y = -1, -1

for i in range(n):
    for j in range(m):
        if board[i][j] == 2:
            start_x, start_y = i, j
        elif board[i][j] == 0:
            result_board[i][j] = 0

bfs(n, m, start_x, start_y, board, result_board)
    
for row in result_board:
    print(*row)