import sys
import math

code1_count = 0
code2_count = 0

def matrix_path1(m, n): # (1, 1)에서 (n, n)에 이르는 최고 점수를 구한다.
    return matrix_path_rec(m, n, n)

def matrix_path_rec(m, i, j): # (1, 1)에서 (i, j)에 이르는 최고 점수를 구한다.
    if (i == 0 or j == 0):
        global code1_count
        code1_count += 1
        return 0  # 코드1
    else:
        return (m[i-1][j-1] + (max(matrix_path_rec(m, i-1, j), matrix_path_rec(m, i, j-1))))

def matrix_path2(m, n): # (1, 1)에서 (n, n)에 이르는 최고 점수를 구한다.
    d = [[0 for _ in range(n+1)] for _ in range(n+1)]
    for i in range(1, n+1):
        for j in range(1, n+1):
            global code2_count
            code2_count += 1
            d[i][j] = m[i-1][j-1] + max(d[i - 1][j], d[i][j - 1])  # 코드2
    return d[n][n]

N = int(sys.stdin.readline().strip())
M = []
for _ in range(N):
    M.append(list(map(int, sys.stdin.readline().split())))
    
# 직접 계산시 시간초과
# matrix_path1(M, N)
# matrix_path2(M, N)

# 2n!/(n!*(2n-n)!) 을 계산하여 code1_count를 구함
code1_count = math.factorial(2 * N) // (math.factorial(N) * math.factorial(N))
# n*n을 계산하여 code2_count를 구함
code2_count = N*N

print(f'{code1_count} {code2_count}')