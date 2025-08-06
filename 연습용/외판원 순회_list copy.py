import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = defaultdict(lambda: -1)
def tsp_top_down(cur, visited: list):
    # 모든 도시를 방문했을 경우
    if visited == [True] * N:
        # 시작점(0번 도시)으로 돌아오는 비용을 반환
        return graph[cur][0] if graph[cur][0] != 0 else float('inf')

    # 이미 계산된 값이 있는 경우
    if dp[(cur, tuple(visited))] != -1:
        return dp[(cur, tuple(visited))]

    # 계산되지 않은 경우, 최소 비용을 찾기
    min_cost = float('inf')
    for next in range(N):
        if not visited[next] and graph[cur][next] != 0:
            # 재귀적으로 다음 도시로 이동하는 비용을 계산
            new_visited = visited[:]
            new_visited[next] = True
            cost = graph[cur][next] + tsp_top_down(next, new_visited)
            min_cost = min(min_cost, cost)
    
    # 계산된 최소 비용을 DP 테이블에 저장
    dp[(cur, tuple(visited))] = min_cost
    return min_cost

start_visited = [False] * N
start_visited[0] = True
result = tsp_top_down(0, start_visited)
print(result)