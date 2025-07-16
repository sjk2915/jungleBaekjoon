import sys
import itertools

N, M = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))
nums.sort()
products = list(itertools.product(nums, repeat=M))
for product in products:
    print(*product)