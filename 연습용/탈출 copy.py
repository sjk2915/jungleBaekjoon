import sys
import heapq

R, C = list(map(int, sys.stdin.readline().split()))
TWforest = [list(sys.stdin.readline().strip()) for _ in range(R)]

WATER = 0
HEDGEHOG = 1
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]
# 퍼펙트한 알고리즘이지만 큐에서 메모리초과로 침수됨
def bfs():
    visited = [[False] * C for _ in range(R)]
    flooded = [[False] * C for _ in range(R)]
    queue = []

    for i in range(R):
        for j in range(C):
            if TWforest[i][j] == '*':
                flooded[i][j] = True
                heapq.heappush(queue, (0, WATER, i, j))
            elif TWforest[i][j] == 'S':
                visited[i][j] = True
                heapq.heappush(queue, (0, HEDGEHOG, i, j))
    
    while queue:
        time, obj, r, c = heapq.heappop(queue)
        if obj == HEDGEHOG and TWforest[r][c] == 'D':
            return time
        
        # 홍수가 일어날 지점 구하기
        if obj == WATER:
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < R and 0 <= nc < C and not flooded[nr][nc] \
                   and (TWforest[nr][nc] == '.' or TWforest[nr][nc] == 'S'):
                    flooded[nr][nc] = True
                    heapq.heappush(queue, (time + 1, WATER, nr, nc))

        # 고슴도치가 움직이기
        elif obj == HEDGEHOG:
            for i in range(4):
                nr = r + dx[i]
                nc = c + dy[i]
                if 0 <= nr < R and 0 <= nc < C and not visited[nr][nc] \
                and (TWforest[nr][nc] == '.' or TWforest[nr][nc] == 'D') \
                and not flooded[nr][nc]:
                    heapq.heappush(queue, (time + 1, HEDGEHOG, nr, nc))

answer = bfs()
print(answer if answer else 'KAKTUS')