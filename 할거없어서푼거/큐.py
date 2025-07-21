import sys

N = int(sys.stdin.readline().strip())
commands = [sys.stdin.readline().split() for _ in range(N)]

queue = []
for command in commands:
    if command[0] == 'push':
        queue.append(command[1])
    if command[0] == 'pop':
        if queue:
            item = queue[0]
            del queue[0]
            print(item)
        else:
            print(-1)
    if command[0] == 'size':
        print(len(queue))
    if command[0] == 'empty':
        if not queue:
            print(1)
        else:
            print(0)
    if command[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    if command[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)