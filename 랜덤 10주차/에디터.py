import sys

str = sys.stdin.readline().strip()
N = int(sys.stdin.readline().strip())
commands = []
for _ in range(N):
    commands.append(sys.stdin.readline().split())

left = list(str)
right = []
for i in range(N):
    match commands[i][0]:
        case 'L':
            if left:
                right.append(left.pop())
        case 'D':
            if right:
                left.append(right.pop())
        case 'B':
            if left:
                left.pop()
        case 'P':
            left.append(commands[i][1])

print("".join(left + list(reversed(right))))