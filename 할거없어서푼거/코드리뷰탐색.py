import sys
from collections import deque

input = sys.stdin.readline

case = int(input())

for _ in range(case):
    hm, x = map(int, input().split())
    papers = list(map(int, input().split()))
    queue = deque(papers)
    
    idx_list = deque()
    for n in range(hm):
        idx_list.append(n)
    
    answer = 0
    while queue:    
        a = queue[0]
        if idx_list[0] == x and a == max(queue): 
            answer += 1
            break
        elif idx_list[0] != x and a == max(queue):
            answer += 1
            queue.popleft()
            idx_list.popleft()
        else:
            queue.append(queue.popleft())
            idx_list.append(idx_list.popleft())

    print(answer)