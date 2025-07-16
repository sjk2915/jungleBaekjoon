import sys

ALPHABETS = ['a', 'b', 'c', 'd', 'e', 'f',
             'g', 'h', 'i', 'j', 'k', 'l',
             'm', 'n', 'o', 'p', 'q', 'r',
             's', 't', 'u', 'v', 'w', 'x',
             'y', 'z']

word = sys.stdin.readline()
answer = []
for alphabet in ALPHABETS:
    if alphabet in word:
        answer.append(word.index(alphabet))
    else:
        answer.append(-1)

print(*answer)