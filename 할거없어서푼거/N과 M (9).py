import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
permutations = list(set(itertools.permutations(nums, M)))
permutations.sort()
for permutation in permutations:
    print(*permutation)