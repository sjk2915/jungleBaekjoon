import sys

N = int(sys.stdin.readline().strip())
strings = []
for _ in range(N):
    strings.append(sys.stdin.readline().strip())

for i in range(N):
    words = strings[i].split()
    word = " ".join(reversed(words))
    print(f"Case #{i+1}: {word}")