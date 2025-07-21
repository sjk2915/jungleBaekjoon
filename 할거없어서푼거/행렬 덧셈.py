import sys

N, M = map(int, sys.stdin.readline().split())

matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
matrix_b = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

matrix_sum = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        matrix_sum[i][j] = matrix_a[i][j] + matrix_b[i][j]

for row in matrix_sum:
    print(*row)