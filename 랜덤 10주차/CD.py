import sys

end_case = [0, 0]
testcases = []
answers = []
input_case = list(map(int, sys.stdin.readline().split()))
while input_case != end_case:
    n, m = input_case
    cd_sangun = set()
    cd_sunyung = set()
    for _ in range(n):
        cd_sangun.add(int(sys.stdin.readline().strip()))
    for _ in range(m):
        cd_sunyung.add(int(sys.stdin.readline().strip()))
    sell_count = len(cd_sangun & cd_sunyung)
    answers.append(sell_count)
    input_case = list(map(int, sys.stdin.readline().split()))

print(*answers)