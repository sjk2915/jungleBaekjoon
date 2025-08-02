import sys

str_a = sys.stdin.readline().strip()
str_b = sys.stdin.readline().strip()
str_c = str_a+'#'+str_b

def get_suffix_array(s):
    n = len(s)
    # 각 접미사의 랭크를 저장할 배열. 초기에는 문자의 아스키 코드 값을 사용.
    rank = [ord(c) for c in s]
    
    # 접미사 배열. 초기에는 인덱스 순서대로 정렬됨.
    sa = list(range(n))
    
    k = 1
    while k < n:
        # 튜플 정렬을 이용해 랭크를 기준으로 접미사를 정렬
        # (현재 위치의 랭크, k칸 뒤의 랭크)를 쌍으로 정렬한다.
        sa.sort(key=lambda i: (rank[i], rank[i + k] if i + k < n else -1))
        
        # 새로운 랭크를 부여
        new_rank = [0] * n
        new_rank[sa[0]] = 0
        
        for i in range(1, n):
            prev_sa = sa[i-1]
            cur_sa = sa[i]
            
            # 이전 접미사와 현재 접미사의 랭크가 같다면 같은 순위 부여
            # k칸 뒤의 문자가 없을 경우 -1로 비교하여 IndexError 방지
            if (rank[prev_sa], rank[prev_sa + k] if prev_sa + k < n else -1) == \
               (rank[cur_sa], rank[cur_sa + k] if cur_sa + k < n else -1):
                new_rank[cur_sa] = new_rank[prev_sa]
            else:
                new_rank[cur_sa] = new_rank[prev_sa] + 1
        
        rank = new_rank
        k *= 2
        
        # 모든 랭크가 유일해졌다면 정렬이 완료된 것
        if rank[sa[-1]] == n - 1:
            break
            
    return sa

def get_lcp_array(s, sa):
    n = len(s)
    # 1. 랭크(rank) 배열 구축
    # rank[i]는 s[i:] 접미사가 접미사 배열에서 몇 번째에 있는지 저장
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    
    lcp = [0] * n
    height = 0  # 이전 LCP 값을 저장하는 변수
    
    # 2. Kasai의 알고리즘으로 LCP 배열 계산
    for i in range(n):
        # i번째 인덱스에서 시작하는 접미사가 접미사 배열에서 첫 번째(가장 작은) 접미사인 경우
        # 이전 접미사가 없으므로 LCP는 0
        if rank[i] == 0:
            continue
            
        # rank[i] - 1은 i번째 접미사의 바로 앞 접미사 인덱스
        prev_rank = rank[i] - 1
        j = sa[prev_rank]
        
        # i번째 접미사와 j번째 접미사(i의 이전 접미사)의 LCP 계산
        # height 값을 재활용하여 효율성 극대화
        while i + height < n and j + height < n and s[i + height] == s[j + height]:
            height += 1
            
        lcp[rank[i]] = height
        
        # LCP가 1 이상이면 다음 인덱스에서는 최소한 height-1만큼은 LCP가 보장됨
        if height > 0:
            height -= 1
            
    return lcp

suffix_array = get_suffix_array(str_c)
lcp_array = get_lcp_array(str_c, suffix_array)

max_len = 0
lcs_start_idx = -1

# LCP 배열을 순회하며 LCS의 길이와 시작 인덱스 찾기
for i in range(1, len(lcp_array)):
    # 인접한 두 접미사가 서로 다른 원본 문자열에서 온 것인지 확인
    sa_idx_1 = suffix_array[i-1]
    sa_idx_2 = suffix_array[i]
    
    # str_a 접미사: 인덱스가 0 ~ len_a-1
    # str_b 접미사: 인덱스가 len_a+1 ~ len(str_c)-1
    is_from_a = sa_idx_1 < len(str_a)
    is_from_b = sa_idx_2 > len(str_a)
    
    # 두 접미사가 다른 문자열에서 왔을 때
    if (is_from_a and is_from_b) or (not is_from_a and not is_from_b):
        if lcp_array[i] > max_len:
            max_len = lcp_array[i]
            # LCS의 시작 인덱스 중 하나를 저장. 여기서는 짧은 쪽으로 선택
            lcs_start_idx = min(sa_idx_1, sa_idx_2)

print(max_len)
print(str_c[lcs_start_idx : lcs_start_idx + max_len])