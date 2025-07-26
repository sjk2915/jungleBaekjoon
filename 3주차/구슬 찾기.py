import sys
from collections import deque, defaultdict

N, M = list(map(int, sys.stdin.readline().split()))
beads = defaultdict(list)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    beads[u].append(v)

weight_counts = [[0, 0] for _ in range(N+1)]
def bfs(start):
    visited = [False] * (N+1)
    visited[start] = True
    queue = deque([start])
    while queue:
        cur = queue.popleft()
        if cur in beads:
            for next in beads[cur]:
                if not visited[next]:
                    # start에 start보다 가벼운거 개수 +1
                    weight_counts[start][0] += 1
                    # next에 next보다 무거운거 개수 +1
                    weight_counts[next][1] += 1
                    visited[next] = True
                    queue.append(next)

# 모든 구슬마다 bfs를 돌리고
for i in range(1, N+1):
    bfs(i)

cant_middle_beads = 0
# 구슬 마다 상태체크
for i in range(1, N+1):
    if (weight_counts[i][0] >= N // 2 + 1      # 나보다 가벼운거의 개수가 N // 2+1 을 넘거나
        or weight_counts[i][1] >= N // 2 + 1): # 나보다 무거운거의 개수가 N // 2+1 을 넘으면
        cant_middle_beads += 1                 # 중간에 갈 수 없는 구슬이다

print(cant_middle_beads)