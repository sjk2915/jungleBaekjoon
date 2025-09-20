import sys

N, Q = list(map(int, sys.stdin.readline().split()))
A = list(map(int, sys.stdin.readline().split()))
tests = []
for _ in range(Q):
    tests.append(list(map(int, sys.stdin.readline().split())))

A.sort()
prefixsum = [0] * (N+1)
for i in range(N):
    prefixsum[i+1] = prefixsum[i] + A[i]

for L, R in tests:
    print(prefixsum[R] - prefixsum[L-1])