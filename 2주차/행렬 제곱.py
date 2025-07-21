import sys

N, B = map(int, sys.stdin.readline().split())
matrix_a = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
matrix_a = [[elem % 1000 for elem in row] for row in matrix_a]

def get_row(matrix, r):
    return matrix[r]

def get_col(matrix, c):
    return [row[c] for row in matrix]

def dot_product(row, col):
    sum = 0
    for i in range(N):
        sum += row[i] * col[i]
    return sum % 1000

def matrix_product(matrix_a, matrix_b):
    matrix_product = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
           matrix_product[i][j] = dot_product(get_row(matrix_a, i), get_col(matrix_b, j))

    return matrix_product

def identity_matrix():
    identity_matrix = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                identity_matrix[i][j] = 1

    return identity_matrix

def matrix_pow(matrix, b):
    # 행렬^0 은 항?등?행?렬이 나와야함
    # 항등행렬 = 대각선 요소가 모두 1이고 나머지 요소가 0인 행렬
    if b == 0:
        return identity_matrix()
    elif b == 1:
        return matrix
    else:
        half_pow = matrix_pow(matrix, b//2)
        squared_half_pow = matrix_product(half_pow, half_pow)
        if b % 2 == 0:
            return squared_half_pow
        else:
            return matrix_product(matrix, squared_half_pow)

matrix_answer = matrix_pow(matrix_a, B)
for row in matrix_answer:
    print(*row)