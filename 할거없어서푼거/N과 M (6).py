import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
combinations = list(itertools.combinations(nums, M))
for combination in combinations:
    print(*combination)