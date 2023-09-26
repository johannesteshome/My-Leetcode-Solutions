class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        self.isEndOfWord = False


class Trie:

    def __init__(self):
        self.root = TrieNode()        

    def insert(self, word: str) -> None:
        curr = self.root
        for char in word:
            pos = ord(char) - 97
            if not curr.children[pos]:
                curr.children[pos] = TrieNode()
            curr = curr.children[pos]
        curr.isEndOfWord = True
                    

    def search(self, word: str) -> bool:
        curr = self.root
        for char in word:
            pos = ord(char) - 97
            if not curr.children[pos]:
                return False
            curr = curr.children[pos]

        if curr.isEndOfWord:
            return True
        return False
        

    def startsWith(self, prefix: str) -> bool:
        # print("Starts")
        curr = self.root
        for char in prefix:
            pos = ord(char) - 97
            if not curr.children[pos]:
                return False
            curr = curr.children[pos]

        return True
        


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)