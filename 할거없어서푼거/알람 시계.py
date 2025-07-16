import sys

n, m = list(map(int, sys.stdin.readline().split()))
m -= 45
if m < 0:
    n -= 1
    m += 60
if n < 0:
    n += 24

print(f'{n} {m}')