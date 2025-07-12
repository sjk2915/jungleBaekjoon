import sys
import itertools

#난쟁이 9명
n = 9
#키의 합 = 100
sum_height = 100

dwarfs = [int(sys.stdin.readline()) for _ in range(n)]

def combinations(pool, r):
    result = []
    
    # 백트래킹(재귀) 함수 정의
    # current_combination: 현재까지 선택된 요소들
    # start_index: 다음 요소를 탐색할 시작 인덱스
    def backtrack(current_combination, start_index):
        # 기저 사례: r개 요소를 모두 선택한 경우
        if len(current_combination) == r:
            result.append(list(current_combination))
            return

        # 재귀 단계: start_index부터 끝까지 탐색
        for i in range(start_index, n):
            # i번째 요소를 선택합니다.
            current_combination.append(pool[i])
            
            # 다음 요소를 선택하기 위해 재귀 호출
            # i + 1을 시작 인덱스로 사용하여 중복 선택을 방지하고 순서를 유지합니다.
            backtrack(current_combination, i + 1)
            
            # 백트래킹: 현재 조합에서 마지막에 추가한 요소를 제거합니다.
            current_combination.pop()

    # 빈 리스트와 0번 인덱스부터 탐색 시작
    backtrack([], 0)
    return result

#파이썬 내장함수
all_combination = list(itertools.combinations(dwarfs, 7))
#백트래킹으로 구현한 함수
#all_combination = list(combinations(dwarfs, 7))
answer = []
for combination in all_combination:
    if sum(combination) == sum_height:
        answer = list(combination)
        break

answer.sort()
for dwarf in answer:
    print(dwarf)