import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = defaultdict(lambda: -1)
def tsp_top_down(cur, visited):
    # 1. 모든 도시를 방문했을 경우 (모든 비트가 1)
    if visited == [True] * N:
        # 시작점(0번 도시)으로 돌아오는 비용을 반환
        return graph[cur][0] if graph[cur][0] != 0 else float('inf')

    # 2. 이미 계산된 값이 있는 경우
    if dp[(cur, tuple(visited))] != -1:
        return dp[(cur, tuple(visited))]

    # 3. 계산되지 않은 경우, 최소 비용을 찾기
    min_cost = float('inf')

    for next_city in range(N):
        # next_city를 아직 방문하지 않았고, current_city에서 next_city로 가는 경로가 있다면
        if not visited[next_city] and graph[cur][next_city] != 0:
            # 재귀적으로 다음 도시로 이동하는 비용을 계산
            new_visited = visited[:]
            new_visited[next_city] = True
            cost = graph[cur][next_city] + tsp_top_down(next_city, new_visited)
            min_cost = min(min_cost, cost)
    
    # 계산된 최소 비용을 DP 테이블에 저장
    dp[(cur, tuple(visited))] = min_cost
    return min_cost

start_visited = [False] * N
start_visited[0] = True
result = tsp_top_down(0, start_visited)
print(result)