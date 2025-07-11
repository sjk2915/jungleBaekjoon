import sys  
nm = list(map(int, sys.stdin.readline().split()))
nums = list(map(int, sys.stdin.readline().split()))

n, m = nm
answer = [num for num in nums if num < m]

print(*answer, sep=' ')