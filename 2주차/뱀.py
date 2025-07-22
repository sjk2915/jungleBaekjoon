import sys
from collections import deque

GAME_TIME = 10000
UP = 0
RIGHT = 1
DOWN = 2
LEFT = 3

N = int(sys.stdin.readline().strip())
K = int(sys.stdin.readline().strip())
apples = [tuple(map(int, sys.stdin.readline().split())) for _ in range(K)]
L = int(sys.stdin.readline().strip())
controls = deque(tuple(sys.stdin.readline().split()) for _ in range(L))

snake = deque([(1, 1)])
end_time = 0
cur_dir = RIGHT
for i in range(GAME_TIME):
    end_time += 1
    # 먼저 뱀은 몸길이를 늘려 머리를 다음칸에 위치시킨다.
    y, x = snake[-1]
    if cur_dir == UP:
        y -= 1
    elif cur_dir == DOWN:
        y += 1
    elif cur_dir == LEFT:
        x -= 1
    elif cur_dir == RIGHT:
        x += 1
    head = (y, x)
    snake.append(head)
    # 만약 벽이나 자기자신의 몸과 부딪히면 게임이 끝난다
    if (1 > y or y > N
        or 1 > x or x > N
        or snake.count(head) > 1):
        break
    # 만약 이동한 칸에 사과가 있다면, 그 칸에 있던 사과가 없어지고 꼬리는 움직이지 않는다.
    if head in apples:
        apples.remove(head)
    # 만약 이동한 칸에 사과가 없다면, 몸길이를 줄여서 꼬리가 위치한 칸을 비워준다. 즉, 몸길이는 변하지 않는다.
    else:
        snake.popleft()
    # 뱀의 방향 변환 정보가 주어지는데, 정수 X와 문자 C로 이루어져 있으며 게임 시작 시간으로부터 X초가 끝난 뒤에 왼쪽(C가 'L') 또는 오른쪽(C가 'D')로 90도 방향을 회전시킨다는 뜻이다.
    if controls:
        x, c = controls[0]
        if int(x) == end_time:
            controls.popleft()
            if c == 'L':
                cur_dir = (cur_dir - 1) % 4
            elif c == 'D':
                cur_dir = (cur_dir + 1) % 4

print(end_time)