import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(range(1, N+1))
combinations_with_replacement = list(itertools.combinations_with_replacement(nums, M))
for combination_with_replacement in combinations_with_replacement:
    print(*combination_with_replacement)