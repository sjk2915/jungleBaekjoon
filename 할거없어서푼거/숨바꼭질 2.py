import sys
from collections import deque

N, M = list(map(int, sys.stdin.readline().split()))
MAX_VALUE = 100000

def bfs(n, m):
    visit_time = [float('inf')] * (MAX_VALUE + 1)

    queue = deque([(n, 0)])
    min_time = float('inf')
    count = 0
    while queue:
        current_pos, time = queue.popleft()
        if time > min_time: continue
        if current_pos == m:
            if time < min_time:
                count = 0
                min_time = time
            count += 1
            continue
        
        #-1 연산
        next_pos = current_pos - 1
        if 0 <= next_pos <= MAX_VALUE and visit_time[next_pos] >= time + 1:
            visit_time[next_pos] = time + 1
            queue.append((next_pos, time + 1))

        #+1 연산
        next_pos = current_pos + 1
        if 0 <= next_pos <= MAX_VALUE and visit_time[next_pos] >= time + 1:
            visit_time[next_pos] = time + 1
            queue.append((next_pos, time + 1))

        #*2 연산
        next_pos = current_pos * 2
        if 0 <= next_pos <= MAX_VALUE and visit_time[next_pos] >= time + 1:
            visit_time[next_pos] = time + 1
            queue.append((next_pos, time + 1))

    print(min_time)
    print(count)

bfs(N, M)