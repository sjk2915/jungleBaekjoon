import sys
from collections import deque, defaultdict

def is_Bipartite(graph, node_count) -> bool:
    # -1 = 미방문, 0 = 깜장, 1 = 빨강
    color = [-1] * (node_count+1)
    for start in range(1, node_count+1):
        if color[start] == -1:
            queue = deque()
            color[start] = 0
            queue.append(start)
            while queue:
                node = queue.popleft()
                for next in graph[node]:
                    # 안 방문 했으면 색칠하고 가기
                    if color[next] == -1:
                        color[next] = 1 if color[node] == 0 else 0
                        queue.append(next)
                    # 방문했다면 색확인
                    # 내 색 == 다음 색 -> 이분그래프가 아님
                    else:
                        if color[next] == color[node]:
                            return False
    return True

T = int(sys.stdin.readline().strip())
testcases = []
answers = []
for _ in range(T):
    V, E = map(int, sys.stdin.readline().split())
    graph = defaultdict(list)
    for _ in range(E):
        u, v = list(map(int, sys.stdin.readline().split()))
        graph[u].append(v)
        graph[v].append(u)
    answers.append(is_Bipartite(graph, V))

for answer in answers:
    print('YES' if answer else 'NO')