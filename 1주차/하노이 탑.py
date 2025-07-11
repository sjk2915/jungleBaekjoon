import sys

n = int(sys.stdin.readline())

count = 0
log = []
def hanoi(n, start, end, via):
    global count
    if n == 1:
        log.append(f'{start} {end}')
        count += 1
    else:
        hanoi(n-1, start, via, end)
        log.append(f'{start} {end}')
        count += 1
        hanoi(n-1, via, end, start)

if n > 20:
    count = 2**n - 1
    print(count)
else:
    hanoi(n, 1, 3, 2)
    print(count)
    for item in log:
        print(item)