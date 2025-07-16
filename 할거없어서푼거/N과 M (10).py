import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
combinations = list(set(itertools.combinations(nums, M)))
combinations.sort()
for combination in combinations:
    print(*combination)