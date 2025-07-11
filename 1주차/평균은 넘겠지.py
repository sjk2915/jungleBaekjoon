import sys  
n = (int)(sys.stdin.readline())
cases = [list(map(int, sys.stdin.readline().split())) for i in range(n)]

for case in cases:
    studentCount = case[0]
    sum = 0
    for i in range(1, studentCount+1):
        sum += case[i]
    avg = sum / studentCount

    aboveAvgCount = 0
    for i in range(1, studentCount+1):
        if case[i] > avg:
            aboveAvgCount += 1

    ratio = (aboveAvgCount / studentCount) * 100
    print(f'{ratio:.3f}%')