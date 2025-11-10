# Day 01 - LeetCode 208: Implement Trie (Prefix Tree)
# Write your solution here.
class Trie:
    def __init__(self):
        self.trie = dict()
    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if not c in trie: trie[c] = dict()
            trie = trie[c]
        trie['tag'] = None

    def search(self, word: str) -> bool:
        trie = self.trie
        for c in word:
            if not c in trie:
                return False
            trie = trie[c]
        return 'tag' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for c in prefix:
            if not c in trie:
                return False
            trie = trie[c]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)