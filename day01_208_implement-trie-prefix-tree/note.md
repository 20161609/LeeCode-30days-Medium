# Note

## Link
https://leetcode.com/problems/implement-trie-prefix-tree/

## Code
``` python
class Trie:
    def __init__(self): self.trie = dict()
    def insert(self, word: str) -> None:
        trie = self.trie
        for c in word:
            if not c in trie: trie[c] = dict()
            trie = trie[c]
        trie['tag'] = None

    def search(self, word: str) -> bool:
        trie = self.trie
        for c in word:
            if not c in trie: return False
            trie = trie[c]
        return 'tag' in trie

    def startsWith(self, prefix: str) -> bool:
        trie = self.trie
        for c in prefix:
            if not c in trie: return False
            trie = trie[c]
        return True
```

## Idea
- Key: Trie Algorithm
- How to code:
    - `__init__`: create trie with the type `dict`.
    - `insert`: Iterating through `word`, each character should be inserted into `trie`.
        - Based on Tree structure, it should be coded that each character is pointing each node.
        - To mark the end, string `tag` should be inserted into the last character.
    - `search`: Iterating through `word`, each charater should be checked if it can be matching with `trie`'s node. After the iterating, you should check if there is `tag` in the last thing.
    - `startWith`: Same logic with `search`. But in this function, you don't need to check the string `tag` in the last character.

## Complexity
- Time: O(n)
- Space: O(n)

## Review
- Use Trie Algorithm: If there are too many words included, you can avoid to consider the number of words with this Algorithm. The structure can remember the same prefix.