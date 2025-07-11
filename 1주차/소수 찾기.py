import sys

n = int(sys.stdin.readline())
case = list(map(int, sys.stdin.readline().split()))

count = 0
for num in case:
    is_prime = True
    #1은 소수가아님
    if num == 1:
        continue
    #2는 소수
    if num == 2:
        count +=1
        continue
    for i in range(2, num):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        count +=1

print(count)