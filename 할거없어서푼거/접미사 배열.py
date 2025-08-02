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

suffix_array = get_suffix_array(string)
for suffix in suffix_array:
    print(string[suffix:])