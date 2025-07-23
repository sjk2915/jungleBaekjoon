import sys

n = int(sys.stdin.readline())

count = 0
num = 0
while count < n:
    num += 1
    if '666' in str(num):
        count += 1
    
print(num)