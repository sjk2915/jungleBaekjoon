import sys

n, m = map(int, sys.stdin.readline().split())
trees = list(map(int, sys.stdin.readline().split()))

low = 0
high = max(trees)

result = 0

while low <= high:
    mid = (low + high) // 2

    cut_length = 0
    for tree in trees:
        if tree > mid:
            cut_length += tree - mid

    if cut_length >= m:
        result = mid
        low = mid + 1

    else:
        high = mid - 1

print(result)