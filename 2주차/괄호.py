import sys

N = int(sys.stdin.readline().strip())
cases = [sys.stdin.readline().strip() for _ in range(N)]

answer = []
for case in cases:
    my_stack = []
    is_VPS = True
    for char in case:
        # push
        if char == '(':
            my_stack.append(char)
        # pop
        elif char == ')':
            if my_stack:
                my_stack.pop()
            # 닫는데 연적이 없는 경우
            else:
                is_VPS = False
                break
    # 괄호가 다 안닫힌 경우
    if my_stack:
        is_VPS = False

    if is_VPS:
        answer.append('YES')
    else:
        answer.append('NO')

print(*answer)