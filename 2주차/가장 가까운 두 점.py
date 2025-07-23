import sys

N = int(sys.stdin.readline().strip())
dots = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dots.sort(key = lambda x: (x[0], x[1]))

def get_dist(dot1, dot2):
    return (dot2[0] - dot1[0])**2 + (dot2[1] - dot1[1])**2

def get_min_dist_crossing_mid(low, high, min_dist):
    mid = (low + high) // 2
    dots_for_compare = [dot for dot in dots[low:high+1]
                        if (dot[0]-dots[mid][0])**2 < min_dist]
    
    dots_for_compare.sort(key = lambda x: x[1])
    for i in range(len(dots_for_compare)):
        for j in range(i+1, len(dots_for_compare)):
            if (dots_for_compare[i][1] - dots_for_compare[j][1])**2 >= min_dist:
                break
            min_dist = min(min_dist, get_dist(dots_for_compare[i], dots_for_compare[j]))

    # left_dots = [dot for dot in dots[low:mid+1] 
    #              if (dot[0]-dots[mid][0])**2 < min_dist]
    # right_dots = [dot for dot in dots[mid+1:high+1]
    #               if (dot[0]-dots[mid][0])**2 < min_dist]
    # for left_dot in left_dots:
    #     compare_dots = [right_dot for right_dot in right_dots if (left_dot[1] - right_dot[1])**2 < min_dist]
    #     for compare_dot in compare_dots:
    #         min_dist = min(min_dist, get_dist(left_dot, compare_dot))

    # left_dots.sort(key = lambda x: x[1])
    # right_dots.sort(key = lambda x: x[1])
    # for left_dot in left_dots:
    #     for right_dot in right_dots:
    #         if (left_dot[1] - right_dot[1])**2 >= min_dist:
    #             continue
    #         min_dist = min(min_dist, get_dist(left_dot, right_dot))

    return min_dist

def get_closest(low, high):
    mid = (low + high) // 2
    if high - low == 0:
        return float('inf')
    if high - low == 1:
        return get_dist(dots[low], dots[high])
    elif low < high:
        shorter_dist = min(get_closest(low, mid), get_closest(mid+1, high))
        return min(shorter_dist, get_min_dist_crossing_mid(low, high, shorter_dist))
    
if len(dots) == 1:
    print(0)
else:
    print(get_closest(0, N-1))