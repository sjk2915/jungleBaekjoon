import sys

N = int(sys.stdin.readline().strip())
inputs = [int(sys.stdin.readline().strip()) for _ in range(N)]

my_stack = []
for val in inputs:
    # pop
    if val == 0:
        my_stack.pop()
    # push
    else:
        my_stack.append(val)

print(sum(my_stack))