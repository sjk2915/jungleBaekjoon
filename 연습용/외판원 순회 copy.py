import sys

N = int(sys.stdin.readline().strip())
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

dp = [[-1] * (1 << N) for _ in range(N)]
def tsp_top_down(cur, visited):
    # 1. 모든 도시를 방문했을 경우 (모든 비트가 1)
    if visited == (1 << N) - 1:
        # 시작점(0번 도시)으로 돌아오는 비용을 반환
        return graph[cur][0] if graph[cur][0] != 0 else float('inf')

    # 2. 이미 계산된 값이 있는 경우
    if dp[cur][visited] != -1:
        return dp[cur][visited]

    # 3. 계산되지 않은 경우, 최소 비용을 찾기
    min_cost = float('inf')

    for next_city in range(N):
        # next_city를 아직 방문하지 않았고, current_city에서 next_city로 가는 경로가 있다면
        if not (visited & (1 << next_city)) and graph[cur][next_city] != 0:
            # 재귀적으로 다음 도시로 이동하는 비용을 계산
            cost = graph[cur][next_city] + tsp_top_down(next_city, visited | (1 << next_city))
            min_cost = min(min_cost, cost)
    
    # 계산된 최소 비용을 DP 테이블에 저장
    dp[cur][visited] = min_cost
    return min_cost

def tsp_bottom_up():
    # 1. 초기 상태 설정: 시작점(0번 도시)에서 시작하는 비용은 0
    # 비트마스크: 1 (0번 도시만 방문)
    dp[0][1] = 0

    # 2. 모든 상태(visited_mask)를 순회하며 DP 테이블 채우기
    # 0001 (1) 부터 1111 (15)까지
    for visited in range(1, 1 << N):
        for cur in range(N):
            # 현재 도시를 방문한 상태라면
            if dp[cur][visited] != float('inf'):
                # 다음으로 방문할 도시를 선택
                for next in range(N):
                    # next_city를 아직 방문하지 않았고, 경로가 있을 경우
                    if not (visited & (1 << next)) and graph[cur][next] != 0:
                        # 다음 상태(비트마스크)와 도시로 업데이트
                        next_visited = visited | (1 << next)
                        new_cost = dp[cur][visited] + graph[cur][next]

                        dp[next][next_visited] = min(dp[next][next_visited], new_cost)
    
    # 3. 모든 도시를 방문한 상태에서 시작점(0번 도시)으로 돌아오는 최소 비용 찾기
    min_cost = float('inf')
    final_visited = (1 << N) - 1

    # 마지막 방문 도시에서 시작점으로 돌아오는 비용을 계산
    for cur in range(N):
        # 모든 도시를 방문했고, current_city에 있을 때
        if dp[cur][final_visited] != float('inf') and graph[cur][0] != 0:
            cost = dp[cur][final_visited] + graph[cur][0]
            min_cost = min(min_cost, cost)
            
    return min_cost

result = tsp_bottom_up()
# result = tsp_top_down(0, 1)
print(result)