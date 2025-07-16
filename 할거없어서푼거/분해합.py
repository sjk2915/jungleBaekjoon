import sys

n = sys.stdin.readline().strip()

def decomposed_sum(n):
    sum = 0
    sum += int(n)
    for char in n:
        sum += int(char)
    return sum

answer = 0
for i in range(int(n)):
    if decomposed_sum(str(i)) == int(n):
        answer = i
        break
    
print(answer)