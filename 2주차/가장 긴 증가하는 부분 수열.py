import sys

N = int(sys.stdin.readline())
nums = list(map(int, sys.stdin.readline().split()))

def solve_using_dp():
    dp = [1] * N
    for i in range(N):
        for j in range(i):
            if nums[j] < nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    print(max(dp))

# else 구문 에서 binary_search 로 num이 들어가야할
# answer_list의 idx를 알아내서 알고리즘 교체가능
def solve_using_linear():
    answer_list = []
    for num in nums:
        if not answer_list or num > answer_list[-1]:
            answer_list.append(num)
        else:
            for i in range(len(answer_list) - 1, -1, -1):
                if answer_list[i] < num:
                    answer_list[i+1] = num
                    break
                elif i == 0 and answer_list[i] > num:
                    answer_list[i] = num

    print(len(answer_list))

solve_using_linear()