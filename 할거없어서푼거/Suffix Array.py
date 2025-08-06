import sys

string = sys.stdin.readline().strip()

def get_suffix_array(string):
    n = len(string)
    # 이걸 안붙이면 어떤 접미사가 다른 접미사의 접두사일때 구별이 어려워짐
    # 예시 'ababababababab', 'aaaaaaaaaaaaaaaa'
    string += '$'
    # 먼저, 문자열의 모든 접미사를 첫 번째 문자(길이 1의 접두사)를 기준으로 정렬
    # 각 접미사에 정렬된 순서에 따라 랭크(Rank)를 부여
    rank = [ord(char) for char in string]
    suffix_array = list(range(n + 1))
    
    # 반복 단계 (길이 k -> 2k)
    k = 1
    while k <= n:
        # 이전 단계(k)에서 얻은 랭크를 사용해 접미사의 길이를 두 배로 확장하여 정렬
        # 접미사를 (현재 랭크, k칸 뒤의 랭크) 쌍으로 표현하여 정렬
        # 이 랭크 쌍을 비교하는 것은 결국 길이 2k의 접두사를 비교하는 것과 동일한 효과를 냄
        suffix_array.sort(key=lambda i: (rank[i], rank[i + k] if i + k <= n else -1))

        # 정렬된 순서에 따라 랭크 갱신
        # 이전 랭크쌍과 현재 랭크쌍을 비교
        new_rank = [0] * (n + 1)
        prev_rank_pair = (-1, -1)
        rank_val = 0
        for i in range(n + 1):
            current_rank_pair = (rank[suffix_array[i]], rank[suffix_array[i] + k] if suffix_array[i] + k <= n else -1)
            # 랭크쌍이 다르면: 랭크 쌍이 이전 접미사의 것과 다르다면, 랭크 값을 1 증가시켜 새로운 랭크를 부여
            if current_rank_pair != prev_rank_pair:
                rank_val += 1
            
            # 랭크쌍이 같으면: 현재 접미사의 랭크 쌍이 바로 이전 접미사의 랭크 쌍과 동일하다면, 같은 랭크 값을 부여
            new_rank[suffix_array[i]] = rank_val
            prev_rank_pair = current_rank_pair
        
        # 이 과정을 통해 2k 길이의 접두사까지 고려된 새로운 랭크 배열이 만들어짐
        # 이 새로운 랭크 배열은 다음 단계에서의 랭크 쌍 정렬에 사용됨
        rank = new_rank

        # 이 과정을 반복하다 보면 모든 접미사가 고유한 랭크를 갖게 되고
        # 최종적으로 정렬된 접미사들의 시작 인덱스가 접미사 배열이 됨
        if rank_val == n + 1:
            break
        
        k *= 2
    
    return suffix_array[1:]

def get_lcp_array(string, sa):
    n = len(string)
    # isa 배열 만들기: 먼저, 접미사 배열(SA)을 이용하여 역접미사 배열(Inverse Suffix Array, isa)을 만든다.
    # isa[i]는 i번째 접미사가 접미사 배열에서 몇 번째 위치에 있는지 나타낸다.
    isa = [0] * n
    for i in range(n):
        isa[sa[i]] = i
    
    lcp = ['x'] * n
    # LCP 계산 시작: height라는 변수를 0으로 초기화한다.
    # 이 height에는 이전 단계에서 계산된 LCP 값의 길이를 저장한다.
    height = 0
    for i in range(n):
        if isa[i] == 0: continue
            
        j = sa[isa[i] - 1]
        # height 값을 재활용하여 LCP[isa[i]]를 계산한다.
        while i + height < n and j + height < n and string[i + height] == string[j + height]:
            height += 1
            
        lcp[isa[i]] = height
        # LCP[isa[i]]가 x라면, LCP[isa[i+1]]는 적어도 x-1 이상의 값을 가진다.
        # 따라서 height를 max(0, height-1)로 초기화하고 LCP[isa[i+1]]를 계산한다.
        height = max(0, height-1)
            
    return lcp

suffix_array = get_suffix_array(string)
lcp_array = get_lcp_array(string, suffix_array)
# 0-base -> 1-base
for i in range(len(suffix_array)):
    suffix_array[i] += 1

print(*suffix_array)
print(*lcp_array)