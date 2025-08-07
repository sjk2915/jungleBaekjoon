import sys
import heapq

N = int(sys.stdin.readline().strip())
lectures = []
for _ in range(N):
    idx, start, end = list(map(int, sys.stdin.readline().split()))
    # (시간, 1:시작 0:종료, idx)
    heapq.heappush(lectures, (start, 1, idx))
    heapq.heappush(lectures, (end, 0, idx))

use_rooms = [-1] * (N+1)
classrooms = []
room_count = 0
while lectures:
    time, is_start, idx = heapq.heappop(lectures)
    if is_start:
        # 사용 가능한 강의실이 있을때
        if classrooms:
            room_num = classrooms.pop()
            use_rooms[idx] = room_num
        # 없으면 만들기
        else:
            room_count += 1
            use_rooms[idx] = room_count
    # 강의 종료시 리스트에 반납
    else:
        classrooms.append(use_rooms[idx])

print(room_count)
for i in use_rooms[1:]:
    print(i)