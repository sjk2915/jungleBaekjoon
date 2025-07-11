import sys  
num = (int)(sys.stdin.readline())

if (num >= 90):
    print('A')
elif (num >= 80):
    print('B')
elif (num >= 70):
    print('C')
elif (num >= 60):
    print('D')
else:
    print('F')