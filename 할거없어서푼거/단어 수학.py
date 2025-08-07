import sys
from enum import Enum
from collections import deque

N = int(sys.stdin.readline().strip())
words = [sys.stdin.readline().strip() for _ in range(N)]
alphabet_num = [-1] * 10
class Index_of_Alphabet(Enum):
    A = 0
    B = 1
    C = 2
    D = 3
    E = 4
    F = 5
    G = 6
    H = 7
    I = 8
    J = 9

def longest_first_extraction(words):
    str_ptr = [(i, 0) for i in range(len(words))]
    
    queue = []
    to_extract = sum(len(word) for word in words)
    while len(queue) < to_extract:
        str_ptr_idx = -1
        max_remain_len = -1
        
        for i, (word_idx, char_idx) in enumerate(str_ptr):
            remain_len = len(words[word_idx]) - char_idx
            
            if remain_len <= 0:
                continue

            if remain_len > max_remain_len:
                max_remain_len = remain_len
                str_ptr_idx = i
        
        word_idx, char_idx = str_ptr[str_ptr_idx]
        queue.append(words[word_idx][char_idx])
        str_ptr[str_ptr_idx] = (word_idx, char_idx + 1)
    
    return queue

queue = deque(longest_first_extraction(words))
num = 9
while queue and num > -1:
    char = queue.popleft()
    if alphabet_num[Index_of_Alphabet[char].value] == -1:
        alphabet_num[Index_of_Alphabet[char].value] = num
        num -= 1

int_words = []
for word in words:
    num_word = ''
    for char in word:
        num_word += str(alphabet_num[Index_of_Alphabet[char].value])
    int_words.append(int(num_word))

print(sum(int_words))