import sys
import bisect

N = int(sys.stdin.readline())
n_nums = list(map(int, sys.stdin.readline().split()))
M = int(sys.stdin.readline())
m_nums = list(map(int, sys.stdin.readline().split()))

def solve_using_set():
    set_nums = set(n_nums)
    for m_num in m_nums:
        if m_num in set_nums:
            print(1)
        else:
            print(0)

def solve_using_binary():
    def _binary_search(list = list, num = int) -> bool:
        low = 0
        high = len(list) - 1
        while low <= high:
            mid = (low + high) // 2
            if list[mid] == num:
                return True
            elif list[mid] > num:
                high = mid - 1
            elif list[mid] < num:
                low = mid +1
        return False

    n_nums.sort()
    for m_num in m_nums:
        if _binary_search(n_nums, m_num):
            print(1)
        else:
            print(0)

def solve_using_bisect():
    n_nums.sort()
    for m_num in m_nums:
        idx = bisect.bisect_left(n_nums, m_num)
        if 0 <= idx < N and n_nums[idx] == m_num:
            print(1)
        else:
            print(0)

solve_using_binary()