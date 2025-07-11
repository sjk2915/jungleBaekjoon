import sys

n = int(sys.stdin.readline())
answer = 1
for i in range(n, 1, -1):
    answer *= i
print(answer)