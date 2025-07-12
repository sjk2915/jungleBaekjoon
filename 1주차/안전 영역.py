import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, N, area):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    area[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if area[nx][ny] >= 1:
                dfs(nx, ny, N, area)

n = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

max_height = max(max(row) for row in area)

safe_areas = []
for i in range(1, max_height):
    safe_area = []
    for row in area:
        new_row = []
        for local in row:
            if local > i:
                new_row.append(local)
            else:
                new_row.append(0)
        safe_area.append(new_row)
    safe_areas.append(safe_area)

# for safe_area in safe_areas:
#     print('-----------------')
#     for row in safe_area:
#         print(row)

#비가 안오는 경우:height=0 일 수 있으므로 안전구역은 최소 1개
max_safe = 1
for safe_area in safe_areas:
    now_safe = 0
    for i in range(n):
        for j in range(n):
            if safe_area[i][j] >= 1:
                now_safe += 1
                dfs(i, j, n, safe_area)

    max_safe = max(max_safe, now_safe)

print(max_safe)