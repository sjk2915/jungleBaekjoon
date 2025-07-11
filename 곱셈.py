import sys  
numA = (int)(sys.stdin.readline())
numB = (int)(sys.stdin.readline())

print(numA * int(numB%10))
print(numA * int(numB%100/10))
print(numA * int(numB/100))
print(numA * numB)