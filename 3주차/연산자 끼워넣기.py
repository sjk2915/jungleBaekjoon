import sys

PLUS = 0
MINUS = 1
MULT = 2
DIV = 3

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
op_counts = list(map(int, sys.stdin.readline().split()))

def calc(to_calc):
    result = None
    last_op = None
    for i in range(len(to_calc)):
        # 짝수면 to_calc[i]가 피연산자
        if i % 2 == 0:
            if result is None:
                result = to_calc[i]
            else:
                if last_op == PLUS:
                    result += to_calc[i]
                elif last_op == MINUS:
                    result -= to_calc[i]
                elif last_op == MULT:
                    result *= to_calc[i]
                # 그지같은 파이썬 나눗셈을 C 나눗셈화
                elif last_op == DIV:
                    if result < 0 and to_calc[i] > 0:
                        result = -(abs(result) // to_calc[i])
                    else:
                        result //= to_calc[i]
        # 홀수면 to_calc[i]가 연산자
        else:
            last_op = to_calc[i]

    return result

min_value = float('inf')
max_value = float('-inf')
to_calc = [nums[0]]
def solve(idx):
    global min_value, max_value
    if len(to_calc) == 2*N - 1:
        result = calc(to_calc)
        min_value = min(min_value, result)
        max_value = max(max_value, result)
        return

    for i in range(len(op_counts)):
        if op_counts[i] > 0:
            op_counts[i] -= 1
            to_calc.append(i)
            to_calc.append(nums[idx])
            solve(idx+1)
            # 백트래킹
            to_calc.pop()
            to_calc.pop()
            op_counts[i] += 1

solve(1)
print(max_value)
print(min_value)