class TrieNode:
    def __init__(self):
        self.children = [None for _ in range(26)]

        self.isEndOfWord = False
     


class Solution:
    def longestWord(self, words: List[str]) -> str:
        root = TrieNode()
        
        def longest():
            curr = root
            Max = 0
            answer = ""

            def dfs(curr, word):
                nonlocal Max
                nonlocal answer
                Max = max(Max, len(word))
                if len(word) == Max and len(answer) < len(word):
                    answer = word
                
                for i in range(26):
                    if curr.children[i] and curr.children[i].isEndOfWord:
                        dfs(curr.children[i], word+chr(i+97))

            dfs(curr, "")
            return answer

        def insert(word):
            curr = root
            for char in word:
                pos = ord(char) - 97
                if not curr.children[pos]:
                    curr.children[pos] = TrieNode()
                curr = curr.children[pos]
            curr.isEndOfWord = True

        for word in words:
            insert(word)
        

        # def show():
        #     queue = deque([root])
        #     while queue:
        #         print("level")
        #         for _ in range(len(queue)):
        #             currs  = queue.popleft()
        #             for i in range(len(currs.children)):
        #                 if currs.children[i]:
        #                     print(chr(i+97), currs.children[i].isEndOfWord)
        #                     queue.append(currs.children[i])
        # show()

        return longest()

        
        