import sys
from collections import deque

N = int(sys.stdin.readline().strip())

queue = deque()
for i in range(1, N+1):
    queue.append(i)

for i in range(N-1):
    queue.popleft()
    card = queue.popleft()
    queue.append(card)

print(queue[0])