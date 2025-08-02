import sys
import re

equation = sys.stdin.readline().strip()
parts = re.split(r'([+-])', equation)

answer = 0
is_plus = True
for part in parts:
    if part == '+': continue
    if part == '-': is_plus = False
    else:
        if is_plus:
            answer += int(part)
        else:
            answer -= int(part)
print(answer)