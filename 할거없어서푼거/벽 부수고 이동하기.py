import sys
import heapq

N, M = list(map(int, sys.stdin.readline().split()))
maze = [list(map(int, sys.stdin.readline().strip())) for _ in range(N)]
MAX_BREAK = 1
def bfs():
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    # [0][r][c] == 벽을 0번 부수고 r,c 에 간 거리, [1][r][c] == 벽을 1번 부수고 r,c 에 간 거리
    dists = [[[float('inf')] * M for _ in range(N)] for _ in range(MAX_BREAK + 1)]

    dists[0][0][0] = 1
    queue = [(1, 0, 0, 0)]
    while queue:
        dist, break_time, r, c = heapq.heappop(queue)
        if r == N-1 and c == M-1:
            return dist
        if dists[break_time][r][c] < dist: continue
        for i in range(4):
            nr = r + dx[i]
            nc = c + dy[i]
            if 0 <= nr < N and 0 <= nc < M \
               and dists[break_time][nr][nc] > dist + 1:
                # 벽일때
                if maze[nr][nc] == 1:
                    if break_time < MAX_BREAK:
                        dists[break_time + 1][nr][nc] = dist + 1
                        heapq.heappush(queue, (dist + 1, break_time + 1, nr, nc))
                # 길일때
                else:
                    dists[break_time][nr][nc] = dist + 1
                    heapq.heappush(queue, (dist + 1, break_time, nr, nc))
    return -1

print(bfs())