import sys
import itertools

n = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def permutation(pool):
    result = []
    in_used = []
    
    # 단순 재귀로 구현 // 메모리 효율 안좋음
    def recursion(current_permutation, in_used):
        if len(current_permutation) == len(pool):
            result.append(list(current_permutation))
            return
        
        for i in range(len(pool)):
            if i in in_used:
                continue

            recursion(current_permutation + [pool[i]], in_used + [i])

    #백트래킹으로 구현
    def backtrack(current_permutation):
        if len(current_permutation) == len(pool):
            result.append(list(current_permutation))
            return
        
        for i in range(len(pool)):
            if i in in_used:
                continue
            current_permutation.append(pool[i])
            in_used.append(i)
            
            backtrack(current_permutation)
            
            current_permutation.pop()
            in_used.remove(i)

    recursion([], in_used)
    return result

#파이썬 내장함수
#all_permutations = list(itertools.permutations(nums))
#백트래킹으로 구현한 함수
all_permutations = list(permutation(nums))

answer = 0
for permutations in all_permutations:
    dif_sum = 0
    for i in range(len(permutations)-1):
        dif_sum += abs(permutations[i]-permutations[i+1])
    if dif_sum > answer:
        answer = dif_sum

print(answer)