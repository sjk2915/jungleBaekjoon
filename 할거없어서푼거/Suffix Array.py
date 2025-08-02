import sys

string = sys.stdin.readline().strip()

def get_suffix_array(string):
    n = len(string)
    string += '$'
    rank = [ord(char) for char in string]
    suffix_array = list(range(n + 1))
    
    k = 1
    while k <= n:
        suffix_array.sort(key=lambda i: (rank[i], rank[i + k] if i + k <= n else -1))

        new_rank = [0] * (n + 1)
        prev_rank_pair = (-1, -1)
        rank_val = 0
        for i in range(n + 1):
            current_rank_pair = (rank[suffix_array[i]], rank[suffix_array[i] + k] if suffix_array[i] + k <= n else -1)
            if current_rank_pair != prev_rank_pair:
                rank_val += 1
            
            new_rank[suffix_array[i]] = rank_val
            prev_rank_pair = current_rank_pair
        
        rank = new_rank
        if rank_val == n + 1:
            break
        
        k *= 2
        
    return suffix_array[1:]

def get_lcp_array(s, sa):
    n = len(s)
    rank = [0] * n
    for i in range(n):
        rank[sa[i]] = i
    
    lcp = ['x'] * n
    height = 0
    for i in range(n):
        if rank[i] == 0: continue
            
        j = sa[rank[i] - 1]        
        while i + height < n and j + height < n and s[i + height] == s[j + height]:
            height += 1
            
        lcp[rank[i]] = height

        if height > 0:
            height -= 1
            
    return lcp

suffix_array = get_suffix_array(string)
lcp_array = get_lcp_array(string, suffix_array)
# 0-base -> 1-base
for i in range(len(suffix_array)):
    suffix_array[i] += 1

print(*suffix_array)
print(*lcp_array)