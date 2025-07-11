import sys
numbers = [(int)(sys.stdin.readline()) for i in range(3)]

a, b, c = numbers
product = a * b * c

for i in range(10):
    cnt = 0
    for num in map(int, str(product)):
        if num == i:
            cnt += 1
    print(cnt)