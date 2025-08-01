import sys

N = int(sys.stdin.readline().strip())
meetings = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
meetings.sort(key = lambda x: (x[1], x[0]))

max_meetings = 0
cur_time = 0
for start, end in meetings:
    if cur_time <= start:
        max_meetings += 1
        cur_time = end

print(max_meetings)