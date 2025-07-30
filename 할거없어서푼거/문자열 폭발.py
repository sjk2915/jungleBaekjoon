import sys

str = sys.stdin.readline().strip()
explode = sys.stdin.readline().strip()

stack = []
for char in str:
    stack.append(char)
    while stack[-len(explode):] == list(explode):
        for _ in range(len(explode)):
            stack.pop()

if stack:
    print(''.join(stack))
else:
    print('FRULA')