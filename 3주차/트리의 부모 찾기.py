import sys
import math
from collections import defaultdict

N = int(sys.stdin.readline().strip())
nodes = defaultdict(list)
for _ in range(N-1):
    u, v = list(map(int, sys.stdin.readline().split()))
    nodes[u].append(v)
    nodes[v].append(u)

parents = [-1] * (N)
def dfs(node):
    stack = []
    stack.append(node)
    while stack:
        self = stack.pop()
        childs = nodes[self]
        for child in childs:
            if child != parents[self-1]:
                parents[child-1] = self
                stack.append(child)

dfs(1)
for i in range(1, len(parents)):
    print(parents[i])