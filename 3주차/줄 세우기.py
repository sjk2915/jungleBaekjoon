import sys
from collections import deque, defaultdict
sys.setrecursionlimit(10**5)

N, M = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
in_degree = [0] * (N+1)
for _ in range(M):
    u, v = list(map(int, sys.stdin.readline().split()))
    graph[u].append(v)
    in_degree[v] += 1

def solve_using_Kahn():
    sorting_result = []
    queue = deque()
    # 1. 진입 차수가 0인 모든 노드를 큐에 추가한다.
    for i in range(1, N+1):
        if in_degree[i] == 0:
            queue.append(i)
    
    # 5. 큐가 빌 때까지 2~4를 반복한다.
    while queue:
        # 2. 큐에서 노드 하나를 꺼내서 정렬 결과 리스트에 추가한다.
        node = queue.popleft()
        sorting_result.append(node)
        # 3. 꺼낸 노드에서 나가는 모든 간선 u→v에 대해, v의 진입 차수를 1 감소시킨다.
        for dest in graph[node]:
            in_degree[dest] -= 1
            # 4. 만약 v의 진입 차수가 0이 되면, v를 큐에 추가한다.
            if in_degree[dest] <= 0:
                queue.append(dest)
    
    return sorting_result

def solve_using_dfs():
    stack = []
    visited = [False] * (N+1)
    # 4. 모든 노드를 방문할 때까지 2~3을 반복한다.
    for i in range(1, N+1):
        # 1. 진입 차수가 0인 임의의 노드하나를 고른다.
        # 3. 만약 더이상 갈 수 있는 곳이 없다면 다시 진입 차수가 0인 임의의 노드를 골라 2로 돌아간다.
        if not visited[i] and in_degree[i] == 0:
            # 2-1. DFS를 수행하여 그래프를 탐색하면서
            visited[i] = True
            dfs(i)

    def dfs(node):
        for dest in graph[node]:
            if not visited[dest]:
                visited[dest] = True
                dfs(dest)
        # 2-2. 더 이상 방문할 자식 노드가 없는 노드들을 스택에 넣는다.
        stack.append(node)

    # 5. 모든 노드를 방문한 후에 스택에든 결과를 꺼낸 순서대로 정렬하면 정렬 결과가 된다.
    return list(reversed(stack))

print(*solve_using_Kahn())