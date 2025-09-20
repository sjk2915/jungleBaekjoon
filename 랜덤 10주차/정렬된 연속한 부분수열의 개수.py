import sys

N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

total_pairs = 0
current_length = 1

# 인덱스 0부터 N-2까지 순회 (마지막 원소 직전까지 비교)
for i in range(N - 1):
    # 다음 원소가 현재 원소보다 크면
    if A[i] < A[i+1]:
        current_length += 1
    else:
        # 오름차순 구간이 끝났다면
        total_pairs += current_length * (current_length + 1) // 2
        current_length = 1

# 마지막 오름차순 구간에 대한 계산
total_pairs += current_length * (current_length + 1) // 2

print(total_pairs)