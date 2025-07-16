import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(range(1, N+1))
combinations = list(itertools.combinations(nums, M))
for combination in combinations:
    print(*combination)