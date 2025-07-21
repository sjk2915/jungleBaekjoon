import sys

N = int(sys.stdin.readline().strip())
commands = [sys.stdin.readline().split() for _ in range(N)]

stack = []
for command in commands:
    if command[0] == 'push':
        stack.append(command[1])
    if command[0] == 'pop':
        if stack:
            item = stack[-1]
            del stack[-1]
            print(item)
        else:
            print(-1)
    if command[0] == 'size':
        print(len(stack))
    if command[0] == 'empty':
        if not stack:
            print(1)
        else:
            print(0)
    if command[0] == 'top':
        if stack:
            print(stack[-1])
        else:
            print(-1)