import sys

n = int(sys.stdin.readline())

count = 0
for i in range(1, n+1):
    if i < 100:
        count += 1
    elif i < 1000:
        hundred_digit = int(str(i)[0])
        ten_digit = int(str(i)[1])
        one_digit = int(str(i)[2])
        if hundred_digit - ten_digit == ten_digit - one_digit:
            count += 1

print(count)