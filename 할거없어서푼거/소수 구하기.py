import sys
import math

M, N = list(map(int, sys.stdin.readline().split()))

for num in range(M, N + 1):
    is_prime = True
    #1은 소수가아님
    if num == 1:
        continue
    #2는 소수
    if num == 2:
        print(num)
        continue
    for i in range(2, int(math.sqrt(num) + 1)):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        print(num)