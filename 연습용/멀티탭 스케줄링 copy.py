import sys
from collections import Counter

N, M = list(map(int, sys.stdin.readline().split()))
schedule = list(map(int, sys.stdin.readline().split()))

left_uses = Counter(schedule)
plugeds = set()
pop_count = 0
for next in schedule:
    left_uses[next] -= 1
    # 이미 꼽혀있으면 넘어가기
    if next in plugeds: continue
    # 안 꼽혀있으면
    else:
        # 멀티탭이 비어있으면
        if len(plugeds) < N:
            # 꼽기
            plugeds.add(next)
        # 멀티탭이 꽉차있으면
        else:
            # 가장 덜쓸거 뽑기
            min_count = float('inf')
            for pluged in plugeds:
                if left_uses[pluged] < min_count:
                    min_count = left_uses[pluged]
                    to_pop = pluged
            plugeds.remove(to_pop)
            pop_count += 1
            # 꼽기
            plugeds.add(next)

print(pop_count)