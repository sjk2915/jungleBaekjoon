import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
permutations = list(itertools.permutations(nums, M))
for permutation in permutations:
    print(*permutation)