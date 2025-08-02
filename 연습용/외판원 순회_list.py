import sys
from collections import defaultdict

N = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = defaultdict(lambda: float('inf'))
def tsp_bottom_up():
    # 0번 도시만 방문한 상태 리스트 생성
    start_visited = [False] * N
    start_visited[0] = True
    dp[(0, tuple(start_visited))] = 0

    for i in range(1, 2**N):
        # 현재 방문 상태 리스트 생성
        visited = [bool(i & (1 << j)) for j in range(N)]
        for cur in range(N):
            if visited[cur] and dp[(cur, tuple(visited))] != float('inf'):
                for next in range(N):
                    if not visited[next] and graph[cur][next] != 0:
                        # 다음 방문 상태 리스트 생성
                        next_visited = visited[:]
                        next_visited[next] = True
                        
                        new_cost = dp[(cur, tuple(visited))] + graph[cur][next]
                        
                        # 다음 상태로 업데이트
                        dp[(next, tuple(next_visited))] = min(dp[(next, tuple(next_visited))], new_cost)
    
    # 모든 도시를 방문한 상태에서 시작점(0번 도시)으로 돌아오는 최소 비용 찾기
    min_cost = float('inf')
    final_visited = [True] * N

    # 마지막 방문 도시에서 시작점으로 돌아오는 비용을 계산
    for cur in range(N):
        # 모든 도시를 방문했고, current_city에 있을 때
        if dp[(cur, tuple(final_visited))] != float('inf') and graph[cur][0] != 0:
            cost = dp[(cur, tuple(final_visited))] + graph[cur][0]
            min_cost = min(min_cost, cost)
            
    return min_cost

result = tsp_bottom_up()
print(result)