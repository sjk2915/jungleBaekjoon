import sys

N = int(sys.stdin.readline().strip())
trees = list(map(int, sys.stdin.readline().split()))

def product(arr):
    ret = 1
    for x in arr:
        ret *= x
    return ret

max_P = 0
for i in range(1, N-2):
    for j in range(i+1, N-1):
        for k in range(j+1, N):
            cur_P = product(trees[:i]) + product(trees[i:j]) \
                  + product(trees[j:k]) + product(trees[k:])
            max_P = max(max_P, cur_P)

print(max_P)