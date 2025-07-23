import sys

isbn = sys.stdin.readline().strip()

check_num = 0
for i in range(len(isbn)):
    try:
        num = int(isbn[i])
        if i % 2 == 0:
            check_num += num
        else:
            check_num += 3*num
    except ValueError:
        to_find_idx = i

if to_find_idx % 2 == 0:
    answer = (10 - (check_num % 10)) % 10 
else:
    answer = ((-check_num % 10) * 7) % 10

print(answer)