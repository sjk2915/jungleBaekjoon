import sys

N = int(sys.stdin.readline().strip())
roads = list(map(int, sys.stdin.readline().split()))
fuel_costs = list(map(int, sys.stdin.readline().split()))

cur = 0
total_cost = 0
while cur < N-1:
    dist = 0
    for i in range(cur+1, N):
        dist += roads[i-1]
        if fuel_costs[i] < fuel_costs[cur] \
           or i == N-1:
            total_cost += fuel_costs[cur] * dist
            cur = i
            break

print(total_cost)