import sys

ASCENDING = [1, 2, 3, 4, 5, 6, 7, 8]
DESCENDING = [8, 7, 6, 5, 4, 3, 2, 1]

notes = list(map(int, sys.stdin.readline().split()))
if notes == ASCENDING:
    print('ascending')
elif notes == DESCENDING:
    print('descending')
else:
    print('mixed')