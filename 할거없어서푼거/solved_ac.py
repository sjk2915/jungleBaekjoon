import sys
import math
from collections import deque

N = int(sys.stdin.readline().strip())
opinions = [int(sys.stdin.readline().strip()) for _ in range(N)]

if N == 0:
    print(0)
else:
    to_cut = math.floor((N * 0.15) + 0.5)
    queue = deque(sorted(opinions))
    for _ in range(to_cut):
        queue.pop()
        queue.popleft()
    opinions = list(queue)
    
    avg = math.floor(sum(opinions) / len(opinions) + 0.5)
    print(avg)