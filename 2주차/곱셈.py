import sys

A, B, C = map(int, sys.stdin.readline().split())

def recursion(a, b, c):
    if b == 0:
        return 1
    elif b == 1:
        return a % c
    else:
        half_pow = recursion(a, b//2, c)
        squared_half_pow = (half_pow * half_pow) % c
        if b % 2 == 0:
            return squared_half_pow
        else:
            return ((a % c) * squared_half_pow) % c

print(recursion(A, B, C))