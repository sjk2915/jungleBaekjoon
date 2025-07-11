import sys  
nums = list(map(int, sys.stdin.readline().split()))
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
n = nums[0]
m = nums[1]
print(n+m)
print(n-m)
print(n*m)
print((int)(n/m))
print(n%m)