import sys

str_a = sys.stdin.readline().strip()
str_b = sys.stdin.readline().strip()

if len(str_a) < len(str_b):
    str_a, str_b = str_b, str_a

prev_row = [0] * (len(str_b) + 1)
cur_row = [0] * (len(str_b) + 1)

max_len = 0
max_idx = 0
for i in range(1, len(str_a)+1):
    for j in range(1, len(str_b)+1):
        if str_a[i-1] == str_b[j-1]:
            cur_row[j] = prev_row[j-1] + 1
            if cur_row[j] > max_len:
                max_len = cur_row[j]
                max_idx = i - 1
        else:
            cur_row[j] = 0

    prev_row = cur_row[:]
    cur_row = [0] * (len(str_b) + 1)

answer = str_a[max_idx - max_len + 1:max_idx + 1]
print(len(answer))
print(answer)