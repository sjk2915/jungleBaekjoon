import sys
from collections import Counter

N, M = list(map(int, sys.stdin.readline().split()))
schedule = list(map(int, sys.stdin.readline().split()))

plugeds = set()
pop_count = 0
for i, next in enumerate(schedule):
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
            # 가장 나중에 쓸거 뽑기
            to_pop = -1
            max_next_use = -1
            for pluged in plugeds:
                try:
                    # pluged 는 next_use 이후 사용
                    next_use = schedule[i+1:].index(pluged) + 1
                    if next_use > max_next_use:
                        max_next_use = next_use
                        to_pop = pluged
                # 리스트내에서 못찾아서 ValueError가 나면 앞으로 안쓸거라는 것
                except ValueError:
                    to_pop = pluged
                    break
            plugeds.remove(to_pop)
            pop_count += 1
            # 꼽기
            plugeds.add(next)

print(pop_count)