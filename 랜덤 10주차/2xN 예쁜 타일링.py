import sys

N, A, B = list(map(int, sys.stdin.readline().split()))
a_value = list(map(int, sys.stdin.readline().split()))
b_value = list(map(int, sys.stdin.readline().split()))

a_value.sort()
b_value.sort()
remain = N
total_value = 0
while remain > 0:
    if remain >= 2:
        cur_a_value = 0
        cur_b_vaule = 0
        if len(a_value) >= 2:
            cur_a_value = a_value[len(a_value)-1] + a_value[len(a_value)-2]
        if len(b_value) >= 1:
            cur_b_vaule = b_value[len(b_value)-1]
        
        if cur_b_vaule > cur_a_value:
            total_value += b_value.pop()
            remain -= 2
        else:
            total_value += a_value.pop()
            remain -= 1
    else:
        total_value += a_value.pop()
        remain -= 1

print(total_value)