import sys

N = int(sys.stdin.readline().strip())
towers = list(map(int, sys.stdin.readline().split()))

answer = [0] * N
stack = []
for i in range(N):
    tower = towers[i]
    while stack and stack[-1][1] <= tower:
            stack.pop()
    if stack:
          answer[i] = stack[-1][0] + 1
    stack.append([i, tower])

print(*answer)