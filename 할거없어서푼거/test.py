def sum(n):
    total_sum = 0
    for i in range(n+1):
        total_sum += i
    return total_sum

def sum_recursion(n):
    if n == 0:
        return 0
    else:
        return n + sum_recursion(n-1)

def sum_recursion_tail(n, sum):
    if n == 0:
        return sum
    else:
        return sum_recursion_tail(n-1, sum+n)

def exp(b, n):
    if n == 0:
        return 1
    else:
        return b * exp(b, n-1)
    
def better_exp(b, n):
    if n == 0:
        return 1
    else:
        #even
        if b % 2 == 0:
            return better_exp(b, n/2) * better_exp(b, n/2)
        #odd
        else:
            return b * better_exp(b, n-1)

print(exp(2, 4))