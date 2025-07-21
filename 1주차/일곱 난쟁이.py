import sys
import itertools

#난쟁이 9명
n = 9
#키의 합 = 100
sum_height = 100

dwarfs = [int(sys.stdin.readline()) for _ in range(n)]

def combinations(pool, r):
    result = []

    # 단순 재귀로 구현 // 메모리 효율 안좋음
    def recursion(current_combination, start_index):
        # 기저 사례: r개 요소를 모두 선택한 경우
        if len(current_combination) == r:
            result.append(list(current_combination))
            return

        # 재귀 단계: start_index부터 끝까지 탐색
        for i in range(start_index, n):
            recursion(current_combination + [pool[i]], i + 1)
    
    # 백트래킹으로 구현
    def backtrack(current_combination, start_index):
        # 기저 사례: r개 요소를 모두 선택한 경우
        if len(current_combination) == r:
            result.append(list(current_combination))
            return

        # 재귀 단계: start_index부터 끝까지 탐색
        for i in range(start_index, n):
            current_combination.append(pool[i])
            backtrack(current_combination, i + 1)
            # 백트래킹: 현재 조합에서 마지막에 추가한 요소를 제거
            current_combination.pop()

    # 빈 리스트와 0번 인덱스부터 탐색 시작
    backtrack([], 0)
    return result

#파이썬 내장함수
#all_combination = list(itertools.combinations(dwarfs, 7))
#백트래킹으로 구현한 함수
all_combination = list(combinations(dwarfs, 7))
answer = []
for combination in all_combination:
    if sum(combination) == sum_height:
        answer = list(combination)
        break

answer.sort()
for dwarf in answer:
    print(dwarf)