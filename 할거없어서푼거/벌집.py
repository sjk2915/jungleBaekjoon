import sys

N = int(sys.stdin.readline().strip())

max_num = 1
cur_layer = 1
while max_num < N:
    max_num += cur_layer * 6
    cur_layer += 1

print(cur_layer)