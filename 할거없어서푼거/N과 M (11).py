import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
products = list(set(itertools.product(nums, repeat=M)))
products.sort()
for product in products:
    print(*product)