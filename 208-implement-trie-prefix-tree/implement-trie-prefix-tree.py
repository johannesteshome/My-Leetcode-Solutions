class TrieNode:

    def __init__(self):
        self.children = defaultdict()
        self.isEndOfWord = False

class Trie:

    def __init__(self):
        self.trie = TrieNode()

    def insert(self, word: str) -> None:
        curr = self.trie
        
        for i in range(len(word)):
            if word[i] not in curr.children:
                newNode = TrieNode()
                curr.children[word[i]] = newNode
            
            curr = curr.children[word[i]]

        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:

        curr = self.trie

        for i in range(len(word)):
            if word[i] in curr.children:
                curr = curr.children[word[i]]
            else:
                return False

        if curr.isEndOfWord:
            return True
        return False 

    def startsWith(self, prefix: str) -> bool:
        curr = self.trie

        for i in range(len(prefix)):
            if prefix[i] in curr.children:
                curr = curr.children[prefix[i]]
            else:
                return False

        return True 


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)