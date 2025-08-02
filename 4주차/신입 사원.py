import sys

T = int(sys.stdin.readline().strip())
testcases = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    candidates = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
    testcases.append(candidates)

for candidates in testcases:
    candidates.sort(key = lambda x: x[0])
    high_inerview_rank = float('inf')
    count = 0
    for document_rank, interview_rank in candidates:
        if high_inerview_rank > interview_rank:
            high_inerview_rank = interview_rank
            count += 1
    print(count)