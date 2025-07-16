import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(range(1, N+1))
permutations = list(itertools.permutations(nums, M))
for permutation in permutations:
    print(*permutation)