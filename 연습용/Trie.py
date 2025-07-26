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

    def search(self, word: str) -> bool:
        cur = self.root
        for char in word:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        return cur.end_of_word

    def starts_with(self, prefix: str) -> bool:
        cur = self.root
        for char in prefix:
            if char not in cur.child:
                return False
            cur = cur.child[char]
        return True
    
    def delete(self, word: str) -> bool:
        return self._delete_recursive(self.root, word, 0)

    def _delete_recursive(self, cur: TrieNode, word: str, index: int) -> bool:
        if index == len(word):
            if not cur.end_of_word:
                return False
            cur.end_of_word = False
            return True

        char = word[index]
        child = cur.child.get(char)

        if not child:
            return False

        deleted_in_subtree = self._delete_recursive(child, word, index + 1)
        if deleted_in_subtree:
            if not child.end_of_word and len(child.child) == 0:
                del cur.child[char]
        
        return deleted_in_subtree