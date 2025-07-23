import sys
from collections import deque

MAX_BOARD = 100

N, M = list(map(int, sys.stdin.readline().split()))
board = {}
for _ in range(N + M):
    u, v = list(map(int, sys.stdin.readline().split()))
    board[u] = v

result = [float('inf')] * (MAX_BOARD+1)
def bfs(start):
    result[start] = 0
    queue = deque([(start, 0)])
    while queue:
        cur, dist = queue.popleft()
        if cur in board:
            next = board[cur]
            if result[next] > dist:
                result[next] = dist
                queue.append((next, dist))
        else:
            for dice_roll in range(1, 7):
                next = cur + dice_roll
                if (next <= MAX_BOARD and result[next] > dist + 1):
                    result[next] = dist + 1
                    queue.append((next, dist + 1))
        
bfs(1)
print(result[100])