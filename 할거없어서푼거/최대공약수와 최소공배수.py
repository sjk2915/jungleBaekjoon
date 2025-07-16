import sys

n, m = list(map(int, sys.stdin.readline().split()))

def gcd(n, m):
    if m == 0: return n
    else: return gcd(m, n % m)

minDiv = gcd(n, m)
maxMult = (n * m) // minDiv

print(minDiv)
print(maxMult)