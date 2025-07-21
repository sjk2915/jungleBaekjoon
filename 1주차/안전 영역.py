import sys
sys.setrecursionlimit(10**6)

N = int(sys.stdin.readline())
area = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

def dfs(x, y, area):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    area[x][y] = 0

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < N and 0 <= ny < N:
            if area[nx][ny] >= 1:
                dfs(nx, ny, area)

def dfs_using_stack(x, y, area):
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]

    stack = []
    stack.append([x, y])
    while stack:
        cx, cy = stack.pop()
        area[cx][cy] = 0
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            if 0 <= nx < N and 0 <= ny < N:
                if area[nx][ny] >= 1:
                    stack.append([nx, ny])

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
    for i in range(N):
        for j in range(N):
            if safe_area[i][j] >= 1:
                now_safe += 1
                dfs_using_stack(i, j, safe_area)

    max_safe = max(max_safe, now_safe)

print(max_safe)