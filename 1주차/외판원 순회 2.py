import sys
import itertools

n = int(sys.stdin.readline())
travel_costs = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

cities = list(range(1, n))
travel_routes = list(itertools.permutations(cities))

answer = float('inf')
for travel_route in travel_routes:
    #0번 도시에서 시작해서 0번 도시로
    new_travel_route = [0] + list(travel_route) + [0]

    total_cost = 0
    for i in range(len(new_travel_route)-1):
        start_city = new_travel_route[i]
        end_city = new_travel_route[i+1]
        cost = travel_costs[start_city][end_city]

        # 경로 없음
        if cost == 0:
            cost = float('inf')

        total_cost += cost

    answer = min(total_cost, answer)

print(answer)