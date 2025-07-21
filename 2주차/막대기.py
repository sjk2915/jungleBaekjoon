import sys

N = int(sys.stdin.readline().strip())
sticks = [int(sys.stdin.readline().strip()) for _ in range(N)]

highest_stick = sticks.pop()
count = 1
while sticks:
    stick = sticks.pop()
    if stick > highest_stick:
        highest_stick = stick
        count += 1

print(count)