import sys  
n = (int)(sys.stdin.readline())
cases = [sys.stdin.readline().strip() for i in range(n)]

for case in cases:
    totalScore = 0
    score = 0
    for char in case:
        if char == 'O':
            score += 1
            totalScore += score
        else:
            score = 0
    print(totalScore)