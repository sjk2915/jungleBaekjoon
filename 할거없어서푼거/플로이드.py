import sys

N = int(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
graph = [[float('inf')] * (N+1) for _ in range(N+1)]
for i in range(1, N+1):
    graph[i][i] = 0
for _ in range(M):
    u, v, w = list(map(int, sys.stdin.readline().split()))
    graph[u][v] = min(graph[u][v], w)

def Floyd_Warshall():
    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

Floyd_Warshall()
for i in range(1, N+1):
    for j in range(1, N+1):
        if graph[i][j] == float('inf'):
            print(0, end=" ")
        else:
            print(graph[i][j], end=" ")
    print()