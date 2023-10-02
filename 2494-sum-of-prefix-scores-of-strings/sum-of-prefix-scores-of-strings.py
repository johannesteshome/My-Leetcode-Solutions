class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        self.isEndOfWord = False

        self.count = 0


class Solution:
    def sumPrefixScores(self, words: List[str]) -> List[int]:
        root = TrieNode()
        def insert(word):
            curr = root
            for char in word:
                pos = ord(char) - 97
                if not curr.children[pos]:
                    curr.children[pos] = TrieNode()
                curr = curr.children[pos]
                curr.count += 1
            curr.isEndOfWord = True
        
        dic = {}

        
        def dfs(curr, word, length):
            
            for i in range(26):
                if curr.children[i]:
                    dfs(curr.children[i], word+chr(i+97), length+curr.children[i].count)
            
            if curr.isEndOfWord:
                dic[word] = length
        
        
        for word in words:
            insert(word)
                
        dfs(root, "", 0)

        answer = []
        for word in words:
            answer.append(dic[word])
        return answer