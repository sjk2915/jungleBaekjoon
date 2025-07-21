import sys

N, M = map(int, sys.stdin.readline().split())
matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
M, K = map(int, sys.stdin.readline().split())
matrix_b = [list(map(int, sys.stdin.readline().split())) for _ in range(M)]

def get_row(matrix, r):
    return matrix[r]
def get_col(matrix, c):
    return [row[c] for row in matrix]
def dot_product(row, col):
    sum = 0
    for i in range(M):
        sum += row[i] * col[i]
    return sum

matrix_product = [[0 for _ in range(K)] for _ in range(N)]
for i in range(N):
    for j in range(K):
        matrix_product[i][j] = dot_product(get_row(matrix_a, i), get_col(matrix_b, j))

for row in matrix_product:
    print(*row)