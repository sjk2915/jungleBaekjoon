import sys

N, K = map(int, sys.stdin.readline().split())

queue = []
for i in range(1, N+1):
    queue.append(i)

answer = []
idx = 0
for i in range(N):
    idx = (idx + K - 1) % len(queue)
    answer.append(queue.pop(idx))

print(f"<{', '.join(map(str, answer))}>")