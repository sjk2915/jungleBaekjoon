import sys

sugar = int(sys.stdin.readline().strip())

for i in range(sugar // 5, -1, -1):
    remain_sugar = sugar - (i * 5)

    if remain_sugar % 3 == 0:
        j = remain_sugar // 3
        remain_sugar = 0
        print(i + j)
        break

if remain_sugar:
    print(-1)