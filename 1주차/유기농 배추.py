import sys
sys.setrecursionlimit(10**6)

def dfs(x, y, M, N, field):
    # 4방향 델타 (상, 하, 좌, 우)
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    
    # 현재 위치의 배추를 방문 처리 (0으로 변경)
    field[x][y] = 0
    
    # 4방향 인접 검사 및 탐색
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        # 1. 경계 조건 확인 (배추밭 범위 내)
        if 0 <= nx < M and 0 <= ny < N:
            # 2. 인접한 곳에 배추가 있는지 확인 (field[nx][ny] == 1)
            if field[nx][ny] == 1:
                # 인접한 배추가 있으면 DFS 재귀 호출
                dfs(nx, ny, M, N, field)

answers = []
t = int(sys.stdin.readline())
for _ in range(t):
    m, n, k = map(int, sys.stdin.readline().split())
    field = [[0] * n for _ in range(m)]

    for _ in range(k):
        cabbage = list(map(int, sys.stdin.readline().split()))
        # 배추 심기
        field[cabbage[0]][cabbage[1]] = 1

    worm_count = 0
    for i in range(m):
        for j in range(n):
            if field[i][j] == 1:
                worm_count += 1
                dfs(i, j, m, n, field)

    answers.append(worm_count)

for answer in answers:
    print(answer)