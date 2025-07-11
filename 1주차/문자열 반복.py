import sys
n = int(sys.stdin.readline())
cases = [sys.stdin.readline().split() for i in range(n)]

for case in cases:
    answer = ''
    for char in case[1]:
        answer += char * int(case[0])
    print(answer)