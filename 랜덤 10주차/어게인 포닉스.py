import sys

N = int(sys.stdin.readline().strip())
strings = []
for _ in range(N):
    strings.append(sys.stdin.readline().strip())

for i in range(N):
    print(strings[i].replace('PO', 'PHO'))