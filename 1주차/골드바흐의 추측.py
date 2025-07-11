import sys

n = int(sys.stdin.readline())
case = [int(sys.stdin.readline()) for i in range(n)]

def is_prime(num):
    #1은 소수가아님
    if num == 1:
        return False
    #2는 소수
    elif num == 2:
        return True
    else:
        for i in range(2, num):
            if num % i == 0:
                return False
        return True
    
# 짝수의 절반부터 시작해서
# num = prime_number + (num-primenumber) 이니까
# prime_number 와 (num-prime_number)가 둘다 소수면 됨

for num in case:
    for i in range(num // 2, 1, -1):
        if is_prime(i) and is_prime(num-i):
            print(f'{i} {num-i}')
            break