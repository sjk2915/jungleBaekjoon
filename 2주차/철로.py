import sys
import heapq

N = int(sys.stdin.readline().strip())
peoples = []
for i in range(N):
    value_1, value_2 = map(int, sys.stdin.readline().split())
    peoples.append((min(value_1, value_2), max(value_1, value_2)))
D = int(sys.stdin.readline().strip())
peoples.sort(key=lambda x: (x[1], x[0]))

min_heap = []
max_people = 0
for people in peoples:
    start, end = people
    if end - D <= start:
        heapq.heappush(min_heap, people)
    while min_heap and min_heap[0][0] < end - D:
        heapq.heappop(min_heap)
    max_people = max(max_people, len(min_heap))

print(max_people)