import sys
from collections import deque

n, m = list(map(int, sys.stdin.readline().split()))
MAX_VALUE = 100000

def bfs(n, m):
    visited = [False] * (MAX_VALUE + 1)

    queue = deque([(n, 0)])
    visited[n] = True
    while queue:
        current_pos, time = queue.popleft()
        if current_pos == m:
            print(time)
            return
        
        #*2 연산
        next_pos = current_pos * 2
        if 0 <= next_pos <= MAX_VALUE and not visited[next_pos]:
            visited[next_pos] = True
            queue.appendleft((next_pos, time))

        #-1 연산
        next_pos = current_pos - 1
        if 0 <= next_pos <= MAX_VALUE and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, time + 1))

        #+1 연산
        next_pos = current_pos + 1
        if 0 <= next_pos <= MAX_VALUE and not visited[next_pos]:
            visited[next_pos] = True
            queue.append((next_pos, time + 1))

bfs(n, m)