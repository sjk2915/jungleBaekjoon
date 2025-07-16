import sys

t = int(sys.stdin.readline())
testcases = [list(map(int, sys.stdin.readline().split())) for _ in range(t)]

for testcase in testcases:
    h, w, n = testcase
    answer = (((n - 1) % h + 1) * 100) + ((n - 1) // h + 1)
    print(answer)