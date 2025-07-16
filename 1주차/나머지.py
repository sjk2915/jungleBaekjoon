import sys

nums = [int(sys.stdin.readline()) for _ in range(10)]
remainders = [num % 42 for num in nums]
print(len(set(remainders)))