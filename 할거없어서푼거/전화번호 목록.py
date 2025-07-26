import sys

T = int(sys.stdin.readline().strip())
testcases = []
for _ in range(T):
    N = int(sys.stdin.readline().strip())
    phone_dir = [sys.stdin.readline().strip() for _ in range(N)]
    testcases.append(phone_dir)

class TrieNode:
    def __init__(self):
        self.child = {}
        self.end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        for char in word:
            if char not in cur.child:
                cur.child[char] = TrieNode()
            cur = cur.child[char]
        cur.end_of_word = True
    
    def is_consist(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.child:
                return True
            cur = cur.child[char]
            if cur.end_of_word:
                return False
        return False

for testcase in testcases:
    trie = Trie()
    is_consist = True
    for phone_num in testcase:
        if trie.is_consist(phone_num):
            trie.insert(phone_num)
        else:
            print('NO')
            is_consist = False
            break
    if is_consist:
        print('YES')