import sys

T = int(sys.stdin.readline().strip())
nums = []
for _ in range(T):
    nums.append(list(map(int, sys.stdin.readline().split())))

digits = "0123456789ABCDEF"

for A, n in nums:
    mod = []
    remain = A
    while remain > 0:
        mod.append(digits[remain % n])
        remain //= n
    if mod == mod[::-1]:
        print(1)
    else:
        print(0)