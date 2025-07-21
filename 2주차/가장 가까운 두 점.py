import sys

N = int(sys.stdin.readline().strip())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots.sort(key = lambda x: (x[0], x[1]))

def get_dist(dot1, dot2):
    return (dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2

# 로직 수정 필요
# 현재방법으로는 시간복잡도가 너무 높음
def get_min_dist_crossing_mid(low, high, mid):
    left_dots = [dot for dot in dots[low:mid+1]]
    right_dots = [dot for dot in dots[mid+1:high+1]]

    min_dist = float('inf')
    for left_dot in left_dots:
        for right_dot in right_dots:
            min_dist = min(min_dist, get_dist(left_dot, right_dot))
    return min_dist

def get_closest(low, high):
    mid = (low + high) // 2
    if high - low == 0:
        return float('inf')
    if high - low == 1:
        return get_dist(dots[low], dots[high])
    elif low < high:
        return min(get_closest(low, mid), get_closest(mid+1,high), get_min_dist_crossing_mid(low, high, mid))
    
if len(dots) == 1:
    print(0)
else:
    print(get_closest(0, N-1))