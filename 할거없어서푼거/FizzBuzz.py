import sys

cases = [sys.stdin.readline().strip() for _ in range(3)]
idx = 0

for case in cases:
    try:
        idx = int(case)
    except ValueError:
        pass
    idx += 1
    
answer = ''
if idx % 3 == 0:
    answer += 'Fizz'
if idx % 5 ==0:
    answer += 'Buzz'

if answer == '':
    print(idx)
else:
    print(answer)