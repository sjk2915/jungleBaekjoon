import sys

n = int(sys.stdin.readline())
commands = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]

stack = []
for command in commands:
    #push
    if command[0] == 1:
        stack.append(command[1])
    #pop
    elif command[0] == 2:
        if stack:
            item = stack.pop()
            print(item)
        else:
            print(-1)
    #len
    elif command[0] == 3:
        print(len(stack))
    #is_empty
    elif command[0] == 4:
        if stack:
            print(0)
        else:
            print(1)
    #peek
    elif command[0] == 5:
        if stack:
            item = stack[-1]
            print(item)
        else:
            print(-1)