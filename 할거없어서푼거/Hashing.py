import sys

R = 31
M = 1234567891

L = int(sys.stdin.readline().strip())
string = sys.stdin.readline().strip()

hashed_string = 0
for i in range(len(string)):
    inted_char = ord(string[i]) - 96
    hashed_string += inted_char * pow(R, i)
hashed_string = hashed_string % M
print(hashed_string)