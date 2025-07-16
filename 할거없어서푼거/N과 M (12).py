import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
combinations_with_replacement = list(set(itertools.combinations_with_replacement(nums, M)))
combinations_with_replacement.sort()
for combination_with_replacement in combinations_with_replacement:
    print(*combination_with_replacement)