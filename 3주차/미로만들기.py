import sys
from collections import deque

N = int(sys.stdin.readline().strip())
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]

break_times = [[float('inf')] * N for _ in range(N)]
def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    queue = deque()

    break_times[0][0] = 0
    queue.append((0, 0, 0))
    while queue:
        r, c, break_time = queue.popleft()
        if break_time > break_times[r][c]: continue
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < N:
                cur_break_time = break_time
                # 벽일때는 부수고 들어가기
                if maze[nr][nc] == 0:
                    cur_break_time += 1
                # 다익스트라에서 빌려온 아이디어
                if cur_break_time < break_times[nr][nc]:
                    break_times[nr][nc] = cur_break_time
                    queue.append((nr, nc, cur_break_time))

bfs()
print(break_times[N-1][N-1])