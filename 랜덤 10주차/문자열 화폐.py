import sys

N, X = list(map(int, sys.stdin.readline().split()))

# 문자열의 가치가 가능한 범위를 벗어나는 경우
min_x = N * 1
max_x = N * 26
if not (min_x <= X <= max_x):
    print("!")

else:
    result = []
    remain_x = X
    for i in range(N):
        remain_n = N - (i + 1)
        char_val = max(1, remain_x - remain_n * 26)
        result.append(chr(ord('A') + char_val - 1))
        remain_x -= char_val
    print("".join(result))