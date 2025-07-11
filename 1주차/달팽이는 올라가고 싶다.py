import sys  
import math

case = list(map(int, sys.stdin.readline().split()))
a, b, v = case

if a >= v:
    total_days = 1
else:
    daily_climb = a - b
    remaining_height = v - a

    days_before_last = math.ceil(remaining_height / daily_climb)
    total_days = days_before_last + 1

print(int(total_days))