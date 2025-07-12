import sys

n = int(sys.stdin.readline())
words = [sys.stdin.readline().strip() for _ in range(n)]

words.sort(key=lambda x: (len(x), x))
unique_words = list(dict.fromkeys(words))

for word in unique_words:
    print(word)