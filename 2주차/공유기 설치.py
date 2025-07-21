import sys

N, C = map(int, sys.stdin.readline().split())
houses = [int(sys.stdin.readline().strip()) for _ in range(N)]

houses.sort()
def check_available(num):
    count = 1
    last_house = houses[0]
    for i in range(N):
        if houses[i] - last_house >= num:
            count += 1
            last_house = houses[i]
    
    return count >= C

answer = 0
low = 1
high = max(houses) - min(houses)
while low <= high:
    mid = (low + high) // 2
    if check_available(mid):
        answer = mid
        low = mid + 1
    else:
        high = mid - 1

print(answer)