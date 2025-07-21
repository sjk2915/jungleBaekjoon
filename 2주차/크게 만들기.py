import sys

N, K = map(int, sys.stdin.readline().split())
num = sys.stdin.readline().strip()

stack = []
erase_count = K
for digit in num:
    while (stack and erase_count > 0 
           and digit > stack[-1]):
        stack.pop()
        erase_count -= 1
            
    stack.append(digit)

while erase_count > 0:
    stack.pop()
    erase_count -= 1

answer = int(''.join(stack))
print(answer)