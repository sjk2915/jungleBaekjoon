import sys

n = int(sys.stdin.readline())

MAX_VALUE = 10000
counts = [0] * (MAX_VALUE + 1)

for _ in range(n):
    num = int(sys.stdin.readline())
    counts[num] += 1

for i in range(MAX_VALUE+1):
    if counts[i] > 0:
        for _ in range(counts[i]):
            sys.stdout.writelines(f'{i}\n')