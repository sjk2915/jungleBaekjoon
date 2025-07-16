import sys

n, m = map(int, sys.stdin.readline().split())
cables = [int(sys.stdin.readline().strip()) for _ in range(n)]

low = 1
high = max(cables)

result = 0

while low <= high:
    mid = (low + high) // 2

    cable_count = 0
    for cable in cables:
        cable_count += cable // mid

    if cable_count >= m:
        result = mid
        low = mid + 1

    else:
        high = mid - 1

print(result)