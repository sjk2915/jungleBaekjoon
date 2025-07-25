import sys
import heapq
from collections import defaultdict

V, E = list(map(int, sys.stdin.readline().split()))
graph = defaultdict(list)
for _ in range(E):
    a, b, w = list(map(int, sys.stdin.readline().split()))
    graph[a].append((b, w))
    graph[b].append((a, w))

mst = defaultdict(list)
nodes_in_mst = set()
heap_for_edge = []
total_weight = 0

node = next(iter(graph))
nodes_in_mst.add(node)
for dest_node, weight in graph[node]:
    heapq.heappush(heap_for_edge, (weight, node, dest_node))
node_count = 1

while node_count < V:
    weight, source_node, dest_node = heapq.heappop(heap_for_edge)

    if dest_node in nodes_in_mst:
        continue

    total_weight += weight
    mst[source_node].append((dest_node, weight))
    mst[dest_node].append((source_node, weight))

    node = dest_node
    nodes_in_mst.add(node)
    for dest_node, weight in graph[node]:
        heapq.heappush(heap_for_edge, (weight, node, dest_node))
    node_count += 1

print(total_weight)