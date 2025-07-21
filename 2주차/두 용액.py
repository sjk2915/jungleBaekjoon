import sys

N = int(sys.stdin.readline())
solutions = list(map(int, sys.stdin.readline().split()))

solutions.sort()

left_solution = 0
right_solution = 0
min_sum = float('inf')

low = 0
high = N - 1
while low < high:
    solution_sum = solutions[low] + solutions[high]
    if abs(solution_sum) < abs(min_sum):
        min_sum = solution_sum
        left_solution = solutions[low]
        right_solution = solutions[high]

    if solution_sum > 0:
        high -= 1
    elif solution_sum < 0:
        low += 1
    elif solution_sum == 0:
        break

print(left_solution)
print(right_solution)