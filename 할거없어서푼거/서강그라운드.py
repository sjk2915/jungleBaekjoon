import sys

N, M, R = list(map(int, sys.stdin.readline().split()))
items = [0]
items += list(map(int, sys.stdin.readline().split()))
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
for _ in range(R):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    graph[u][v] = w
    graph[v][u] = w

def Floyd_Warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

Floyd_Warshall()
max_item = 0
for start in range(1, 1+N):
    cur_item = 0
    for end in range(1, 1+N):
        if graph[start][end] <= M:
            cur_item += items[end]
    max_item = max(max_item, cur_item)
print(max_item)