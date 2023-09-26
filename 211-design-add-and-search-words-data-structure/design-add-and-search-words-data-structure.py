class TrieNode:

    def __init__(self):
        self.children = [None for _ in range(26)]
        
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        

    def addWord(self, word: str) -> None:
        curr = self.root
        for char in word:
            pos = ord(char) - 97
            if not curr.children[pos]:
                curr.children[pos] = TrieNode()
            curr = curr.children[pos]
        curr.isEndOfWord = True
        

    def search(self, word: str) -> bool:
        
        queue = deque([self.root])

        for i in range(len(word)):
            for _ in range(len(queue)):
                curr = queue.popleft()
                if word[i] == ".":
                    for j in range(26):
                        if curr.children[j]:
                            queue.append(curr.children[j])
                else:
                    pos = ord(word[i]) - 97
                    if curr.children[pos]:
                       queue.append(curr.children[pos])
        
        for curr in queue:
            if curr.isEndOfWord:
                return True
        return False

        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)