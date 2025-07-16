import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(range(1, N+1))
products = list(itertools.product(nums, repeat=M))
for product in products:
    print(*product)