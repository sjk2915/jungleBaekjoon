import sys
from collections import defaultdict, deque

N = int(sys.stdin.readline().strip())
buildings = [0] + [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
construct_time = [0] * (N+1)
in_degree = [0] * (N+1)
graph = defaultdict(list)
for i in range(1, N+1):
    construct_time[i] = buildings[i][0]
    for req in buildings[i][1:-1]:
        graph[req].append(i)
        in_degree[i] += 1

def topological_sort():
    total_construct_time = [0] * (N+1)
    queue = deque()
    for i in range(1, N+1):
        if in_degree[i] == 0:
            total_construct_time[i] = construct_time[i]
            queue.append(i)
    while queue:
        cur = queue.popleft()
        for next in graph[cur]:
            total_construct_time[next] = max(total_construct_time[next], total_construct_time[cur] + construct_time[next])
            in_degree[next] -= 1
            if in_degree[next] == 0:
                queue.append(next)

    return total_construct_time[1:]

print(*topological_sort())