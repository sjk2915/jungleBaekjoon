import sys

n = int(sys.stdin.readline())

board = [-1] * n
solutions = 0

# 충돌 추적 배열 초기화
# 퀸을 놓았는지 추적하는 배열 (True/False)
cols = [False] * n         # 열 사용 여부
# 대각선 추적: r + c의 범위는 0 ~ 2*(N-1)
diag1 = [False] * (2 * n - 1) 
# 대각선 추적: r - c의 범위는 -(N-1) ~ N-1
# 파이썬 리스트 인덱스는 음수가 될 수 없으므로, n-1을 더하여 0부터 시작하도록 조정
diag2 = [False] * (2 * n - 1) 

def backtrack(row):
    global solutions
    # N개의 퀸을 모두 배치
    if row == n:
        solutions += 1
        return

    # 현재 행(row)의 모든 열(col)에 퀸을 놓아봅니다.
    for col in range(n):
        # 충돌 검사 (O(1) 시간)
        # 1. col (열)이 이미 사용되었는가?
        # 2. diag1 (r+c) 대각선이 이미 사용되었는가?
        # 3. diag2 (r-c) 대각선이 이미 사용되었는가? (인덱스 조정: col - row + n - 1)
        if not cols[col] and \
            not diag1[row + col] and \
            not diag2[row - col + n - 1]:
            # 퀸을 놓습니다. (추적 배열 업데이트)
            cols[col] = True
            diag1[row + col] = True
            diag2[row - col + n - 1] = True

            # 다음 행으로 이동하여 재귀 호출
            backtrack(row + 1)

            # 백트래킹: 퀸을 제거하고 추적 배열 상태를 되돌립니다.
            cols[col] = False
            diag1[row + col] = False
            diag2[row - col + n - 1] = False

backtrack(0)
print(solutions)