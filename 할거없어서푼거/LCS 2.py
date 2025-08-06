import sys

str_a = sys.stdin.readline().strip()
str_b = sys.stdin.readline().strip()
lcs = [[0] * (len(str_b)+1) for _ in range(len(str_a)+1)]

for i in range(1, len(str_a)+1):
    for j in range(1, len(str_b)+1):
        if str_a[i-1] == str_b[j-1]:
            lcs[i][j] = lcs[i-1][j-1] + 1
        else:
            lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

i = len(str_a)
j = len(str_b)
lcs_string = []
while lcs[i][j] > 0:
    if lcs[i-1][j] == lcs[i][j]:
        i -= 1
    elif lcs[i][j-1] == lcs[i][j]:
        j -= 1
    else:
        lcs_string.append(str_a[i-1])
        i -= 1
        j -= 1
lcs_string.reverse()

print(lcs[len(str_a)][len(str_b)])
print(''.join(lcs_string))