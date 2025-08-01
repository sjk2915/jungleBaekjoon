import sys

str_a = sys.stdin.readline().strip()
str_b = sys.stdin.readline().strip()
str_c = sys.stdin.readline().strip()

def one_str_LCS(str_a):
    # 1. 1개의 문자열을 비교하는 LCS배열을 만든다.
    # 2. LCS배열의 0번째 idx는 0으로 채운다. (이 코드에서는 전부 0으로 초기화했다.)
    lcs = [0] * (len(str_a)+1)

    # 6. 3-5 과정을 반복한다.
    for i in range(1, len(str_a)+1):
        # 3. 문자열A를 한 글자씩 스스로 비교해본다.
        if str_a[i-1] == str_a[i-1]:
            # 4. 두 문자가 같다면 이전 LCS값+1을 표시한다.
            lcs[i] = lcs[i-1] + 1
        else:
            # 5. 두 문자가 다르다면 이전 LCS값을 표시한다.
            lcs[i] = lcs[i-1]

    return lcs[len(str_a)]

def two_str_LCS(str_a, str_b):
    # 1. 2개의 문자열을 비교하는 2차원 LCS배열을 만든다.
    # 2. LCS배열의 문자열A의 첫 idx 이거나 문자열B의 첫 idx는 0으로 채운다.
    lcs = [[0] * (len(str_b)+1) for _ in range(len(str_a)+1)]

    # 6. 3-5 과정을 반복한다.
    for i in range(1, len(str_a)+1):
        for j in range(1, len(str_b)+1):
            # 3. 문자열A와 문자열B를 한 글자씩 비교해본다.
            if str_a[i-1] == str_b[j-1]:
                # 4. 두 문자가 같다면 두 문자열 모두의 이전 LCS 값+1을 표시한다.
                lcs[i][j] = lcs[i-1][j-1] + 1
            else:
                # 5. 두 문자가 다르다면 문자열A의 이전 LCS값과 문자열B의 이전 LCS값 중 최대값을 표시한다.
                lcs[i][j] = max(lcs[i-1][j], lcs[i][j-1])

    return lcs[len(str_a)][len(str_b)]

def three_str_LCS(str_a, str_b, str_c):
    lcs = [[[0] * (len(str_c)+1) for _ in range(len(str_b)+1)] for _ in range(len(str_a)+1)]

    for i in range(1, len(str_a)+1):
        for j in range(1, len(str_b)+1):
            for k in range(1, len(str_c)+1):
                if str_a[i-1] == str_b[j-1] == str_c[k-1]:
                    lcs[i][j][k] = lcs[i-1][j-1][k-1] + 1
                else:
                    lcs[i][j][k] = max(lcs[i-1][j][k], lcs[i][j-1][k], lcs[i][j][k-1])
                    
    return lcs[len(str_a)][len(str_b)][len(str_c)]