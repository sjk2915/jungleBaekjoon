import sys
import bisect

M, N, L = map(int, sys.stdin.readline().split())
shoot_ranges = list(map(int, sys.stdin.readline().split()))
animals = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

count = 0
shoot_ranges.sort()
def solve_using_bisect():
    global count
    for animal in animals:
        x, y = animal
        idx = bisect.bisect_left(shoot_ranges, x)
        
        dist_from_left = float('inf')
        dist_from_right = float('inf')

        if idx > 0:
            left_shoot_range = shoot_ranges[idx - 1]
            dist_from_left = abs(left_shoot_range - x) + y

        if idx < M:
            right_shoot_range = shoot_ranges[idx]
            dist_from_right = abs(right_shoot_range - x) + y

        if L >= min(dist_from_left, dist_from_right):
            count += 1

def solve_using_super_self_maked_binary_search():
    global count
    for animal in animals:
        def _super_self_maked_binary_search(list, num) -> int:
            low = 0
            high = len(list) - 1
            while low <= high:
                mid = (low + high) // 2
                if list[mid] >= num:
                    high = mid - 1
                elif list[mid] < num:
                    low = mid +1
            return low
        
        x, y = animal
        idx = _super_self_maked_binary_search(shoot_ranges, x)

        dist_from_left = float('inf')
        dist_from_right = float('inf')

        if idx > 0:
            left_shoot_range = shoot_ranges[idx - 1]
            dist_from_left = abs(left_shoot_range - x) + y

        if idx < M:
            right_shoot_range = shoot_ranges[idx]
            dist_from_right = abs(right_shoot_range - x) + y

        if L >= min(dist_from_left, dist_from_right):
            count += 1

solve_using_super_self_maked_binary_search()
print(count)