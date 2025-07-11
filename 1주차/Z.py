import sys

n, r, c = map(int, sys.stdin.readline().split())

def draw_board(n):
    board = [[-1 for _ in range(2**n)] for _ in range(2**n)]
    current_num = 0
    def Z_search(n, row, col):
        nonlocal current_num
        if n == 0:
            board[row][col] = current_num
            current_num += 1
        else:
            Z_search(n-1, row, col)
            Z_search(n-1, row, col + 2**(n-1))
            Z_search(n-1, row + 2**(n-1), col)
            Z_search(n-1, row + 2**(n-1), col + 2**(n-1))
    Z_search(n, 0, 0)
    return board

def Z_indexing(n, r, c):
    if n == 0:
        return 0
    half = (2**n) // 2
    quadrant_size = half * half
     # 1. 왼쪽 위 사분면 (r, c)
    if r < half and c < half:
        return Z_indexing(n - 1, r, c)
    
    # 2. 오른쪽 위 사분면 (r, c-half)
    elif r < half and c >= half:
        return quadrant_size + Z_indexing(n - 1, r, c - half)
    
    # 3. 왼쪽 아래 사분면 (r-half, c)
    elif r >= half and c < half:
        return 2 * quadrant_size + Z_indexing(n - 1, r - half, c)
    
    # 4. 오른쪽 아래 사분면 (r-half, c-half)
    elif r >= half and c >= half:
        return 3 * quadrant_size + Z_indexing(n - 1, r - half, c - half)

print(Z_indexing(n, r, c))