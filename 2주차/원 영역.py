import sys

START_CIRCLE = 0
END_CIRCLE = 1

N = int(sys.stdin.readline().strip())
points = []
for _ in range(N):
    x, r = map(int, sys.stdin.readline().split())
    points.append([START_CIRCLE, x-r])
    points.append([END_CIRCLE, x+r])
points.sort(key=lambda x: (x[1], -x[0]))

area = 1
stack = []
for i in range(len(points)):
    case, cur_x = points[i]
    if case == START_CIRCLE:
        #안에 원이 있으면 연속 가능
        if stack and stack[-1][0] == cur_x:
            stack[-1][1] = True
        stack.append([cur_x, False])
    elif case == END_CIRCLE:
        #연속이 유지 되었으면 +2 아니면 +1
        if stack.pop()[1]:
            area += 2
        else:
            area += 1
        #다음 케이스의 연속 검증
        if i < len(points)-1:
            if points[i+1][1] != cur_x:
                stack[-1][1] = False

print(area)