import sys

infix = sys.stdin.readline().strip()

answer = []
stack = []
for item in infix:
    # 연산자 처리
    if item == '(':
        stack.append(item)
    elif item == ')':
        while stack[-1] != '(':
            answer.append(stack.pop())
        stack.pop()
    elif item == '*':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer.append(stack.pop())
        stack.append(item)
    elif item == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            answer.append(stack.pop())
        stack.append(item)
    elif item == '+':
        while stack and (stack[-1] == '*' or stack[-1] == '/' \
                      or stack[-1] == '+' or stack[-1] == '-'):
            answer.append(stack.pop())
        stack.append(item)
    elif item == '-':
        while stack and (stack[-1] == '*' or stack[-1] == '/' \
                      or stack[-1] == '+' or stack[-1] == '-'):
            answer.append(stack.pop())
        stack.append(item)
    # 피연산자 처리
    else:
        answer.append(item)

while stack:
    answer.append(stack.pop())

print("".join(answer))