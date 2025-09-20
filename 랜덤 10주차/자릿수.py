import sys
import math

a, b = list(map(int, sys.stdin.readline().split()))

num_digits = math.floor(b * math.log10(a)) + 1
print(num_digits)