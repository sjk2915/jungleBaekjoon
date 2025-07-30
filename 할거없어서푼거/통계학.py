import sys
import math
from collections import Counter

N = int(sys.stdin.readline())
nums = [int(sys.stdin.readline()) for _ in range(N)]

# 산술평균
print(math.floor(sum(nums) / N + 0.5))
# 중앙값
print(sorted(nums)[N // 2])
# 최빈값
counter = Counter(nums)
all_most_common = counter.most_common()
most_common = [a for a, b in all_most_common if b == all_most_common[0][1]]
most_common.sort()
print(most_common[0] if len(most_common) < 2 else most_common[1])
# 범위
print(max(nums)-min(nums))