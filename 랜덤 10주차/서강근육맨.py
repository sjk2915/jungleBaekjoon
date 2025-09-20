import sys

N = int(sys.stdin.readline().strip())
t = list(map(int, sys.stdin.readline().split()))
t.sort()

max_loss = 0
if N % 2 == 1:
    max_loss = t.pop()
    N -= 1

for i in range(N):
    cur_loss = t[i] + t[N-1-i]
    if cur_loss > max_loss:
        max_loss = cur_loss

print(max_loss)