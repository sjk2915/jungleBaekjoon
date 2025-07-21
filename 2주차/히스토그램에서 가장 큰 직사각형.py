import sys

END_CASE = [0]
testcase = list(map(int, sys.stdin.readline().split()))

def get_max_area(left, right):
    mid = (left + right) // 2
    left_pointer = mid; right_pointer = mid
    max_height = histogram[mid]
    max_area = max_height * (right_pointer - left_pointer + 1)
    while left < left_pointer or right_pointer < right:
        # 양쪽으로 갈수 있음
        if left < left_pointer and right_pointer < right:
            if histogram[left_pointer-1] >= histogram[right_pointer+1]:
                left_pointer -= 1
                max_height = min(max_height, histogram[left_pointer])
            else:
                right_pointer += 1
                max_height = min(max_height, histogram[right_pointer])
        # 한쪽이 막힘
        else:
            # 왼쪽은 갈 수 있음
            if left < left_pointer:
                left_pointer -= 1
                max_height = min(max_height, histogram[left_pointer])
            # 오른쪽은 갈 수 있음
            elif right_pointer < right:
                right_pointer += 1
                max_height = min(max_height, histogram[right_pointer])
        max_area = max(max_area, max_height * (right_pointer - left_pointer + 1))
    return max_area

def recursion(left, right):
    mid = (left + right) // 2
    if left < right:
        return max(recursion(left, mid), recursion(mid+1, right), get_max_area(left, right))
    else:
        return histogram[mid]

while testcase != END_CASE:
    histogram = testcase[1::]
    left = 0
    right = len(histogram) - 1
    mid = (left + right) // 2
    answer = recursion(left, right)
    
    print(answer)
    testcase = list(map(int, sys.stdin.readline().split()))