import sys

N = int(sys.stdin.readline().strip())

mul5 = N // 5
mul25 = N // 25
mul125 = N // 125

print(mul5 + mul25 + mul125)