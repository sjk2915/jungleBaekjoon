import sys  
nums = list(map(int, sys.stdin.readline().split()))

x, y, w, h = nums
left = x - 0
right = w - x
up = h - y
down = y - 0
min = min(left, right, up, down)
print(min)